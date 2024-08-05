---
layout: post
title: 멀티모달 LLM - PLLaVA 데모
date: 2024-08-05 22:25 +0900
categories:
  - LLM
  - 멀티모달
tags: 
math: true
---
<https://github.com/magic-research/PLLaVA?tab=readme-ov-file>

## PLLaVA-7b, 13b, 34b

- Multi Modal LLM 모델

![](https://i.imgur.com/UvMDbGw.png)


- 이미지 인코더(Vision Transformer) + LLM(Vicuna)를 결합

- 이미지 or 영상 인풋 + 텍스트 지시 ⇒ 텍스트 아웃풋


> Video-based Generative Performance 벤치마크들에서 SOTA
> Zero-shot Video Question Answering 벤치마크들에서 최상위권

## DEMO

### Model 출처

[ermu2001/pllava-13b · Hugging Face](<https://huggingface.co/ermu2001/pllava-13b>)

![](https://i.imgur.com/30ERuvT.png)


### SystemPrompt

```python
SYSTEM="""You are a powerful Video Magic ChatBot, a large vision-language assistant. 
You are able to understand the video content that the user provides and assist the user in a video-language related task.
The user might provide you with the video and maybe some extra noisy information to help you out or ask you a question. Make use of the information in a proper way to be competent for the job.
### INSTRUCTIONS:
1. Follow the user's instruction.
2. Be critical yet believe in yourself.
3. What you are watching is a Video, not an image.
4. Do not say something like "It is not clear", just be confident.
"""

```

모델의 한국어 능력은 떨어지는 상태. 영어로 입출력하고, 입력 출력 단계에서 번역 프로세스 추가


```python
parser = StrOutputParser()
model = ChatOpenAI(model="gpt-4o-mini")

def translate_ko(human_input):
    messages = [
        SystemMessage(content="다음 내용을 그대로 영어로 번역해줘"),
        HumanMessage(content=human_input),
    ]

    chain = model | parser
    return chain.invoke(messages)

def translate_en(model_output):
    messages = [
        SystemMessage(content="Please translate this into Korean. 존댓말로 해줘."),
        HumanMessage(content=model_output),
    ]

    chain = model | parser
    return chain.invoke(messages)

```

### Gradio

![](https://i.imgur.com/UP0hTj8.png)

영상 업로드 - Chat 시작 - 지시(질문) 입력 - 출력 확인


> 입력: 영상에서 무슨 일이 생겼어?

>출력: 영상에서는 기계와 장비가 있는 산업 환경이 보입니다. 한 사람이 바닥에 누워 있는데, 아마도 넘어지거나 사고를 당한 것으로 보입니다. 이미지만으로는 정확한 상황을 파악하기 어렵지만, 주의가 필요한 사건이 발생한 것으로 보입니다.


### 영상 examples

![500](https://i.imgur.com/JJJmVMK.png)

공사/공장 현장 영상에서 사고 발생 유무를 확인하고, 상황 설명을 들을 수 있는 데모 프로그램 구현