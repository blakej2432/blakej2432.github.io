---
layout: post
title: 로컬 LLM 구동, 배포하기 with OLLaMA
date: 2024-09-02 23:44 +0900
categories:
  - LLM
  - MLOps
tags: 
math: true
---



## Ollama 설치와 실행

### Ollama 란?

- Optimized LLaMA, llama.cpp를 기반 엔진으로 하여 빠른 추론 속도와 더 낮은 메모리 사용량으로 양자화 버전(.gguf)의 LLM을 사용할 수 있게 해줌
    - llama.cpp는 C++ 기반이기 때문에, python 구현체에 비해 빠르다
- 모델 로드 및 언로드: API 클라이언트 요청에 따라 필요한 모델을 자동으로 로드하고 사용하지 않을 때 언로드 → 리소스 효율적 활용


![](https://i.imgur.com/FiYNJgN.png)


### Ollama 설치, 실행

````markdown
# Ollama 설치
- ollama.com

# akallama-llama3-70B 모델파일(huggingface) 다운로드
- wget <https://huggingface.co/mirlab/AkaLlama-llama3-70b-v0.1-GGUF/resolve/main/AkaLlama-llama3-70b-v0.1.Q5_K_M.gguf>

## STEP 2. Modelfile 작성

```bash
FROM AkaLlama-llama3-70b-v0.1.Q5_K_M.gguf

TEMPLATE """{{- if .System }}
<|begin_of_text|>system {{ .System }}<|end_of_text|>
{{- end }}
<|begin_of_text|>user
{{ .Prompt }}<|end_of_text|>
<|begin_of_text|>assistant
"""

SYSTEM """A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions."""

PARAMETER temperature 0
PARAMETER num_ctx 4096
PARAMETER stop <|begin_of_text|>
PARAMETER stop <|end_of_text|>2
PARAMETER stop <|eot_id|>
PARAMETER stop <|end_of_text|>
````

## STEP 3. Ollama 모델 생성

```bash
ollama create llama3-instruct-70b -f Modelfile
```

## STEP 4. 잘 만들어 졌는지 확인

```bash
ollama list
```

출력되는 결과에 내가 만든 모델이 뜨는지 확인해 주세요.

## STEP 5. Ollama 실행

```bash
ollama run llama3-instruct-70b
```



### Ollama 모델 관리 디렉토리 변경하기

- .gguf 파일 외에도 ollama는 모델 관련 blobs(모델 크기와 같음)를 저장하게 됨 → 디렉토리를 용량이 넉넉한 곳으로 바꿔줘야 함
    
    ```bash
    sudo systemctl edit ollama
    ```
    
    추가 (디렉토리 용량 큰곳으로)
    
    ```bash
    [Service]
    Environment="OLLAMA_MODELS=/data/jmc/models"
    
    ```
    
    저장할 디렉토리 권한 ollama에게 주기 
    
    ```bash
    sudo chown -R ollama:ollama /data/jmc/models
    ```
    
    ollama restart
    
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl restart ollama
    ```
    
    ### Chain 구성 예시
    
    ```python
    from langchain_community.chat_models import ChatOllama
    from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
    from langchain_core.callbacks.manager import CallbackManager
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain_core.output_parsers import StrOutputParser
    
    llm = ChatOllama(
        model="akallama-llama3-70b:latest",
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
        num_gpu=100,
        num_predict=-1,
        temperature=0.1,
        keep_alive=-1
    )
    
    # Prompt 설정
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                '''You are a helpful, smart, kind, and efficient AI assistant named '랩큐라마'. You always fulfill the user's requests to the best of your ability. You must generate an answer in Korean.
                When I ask a question that you don't know the answer for it, just say that you don't know. 
                ''',
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    
    chain = prompt | llm | StrOutputParser()
    ```
    

## 실행 환경

- 70B(50GB), H100 기준
    - num_gpu 설정 없이 추론 → gpu 2.4GB 점유
    - num_gpu=10 → gpu 8GB 점유
    - num_gpu=50 → gpu 32GB 점유
    - num_gpu=80 → gpu 50GB 점유 (모델의 크기와 일치. 이보다 더 큰 num_gpu는 의미 없어짐)
    - 
    - 처음 ollama create 를 하는 경우 ram의 buff/cache가 120GB 까지 올라갔다가 작업이 끝나면 80GB 수준 도달 → ram이 적으면 적은대로 맞춰서 할당 (70B 최소기준 64gb)
    - gpu가 모델 크기 100퍼센트 할당 되었을 경우, 추론시 gpu 50GB 점유 외에 다른 리소스 활용은 없음

## 모델 배포하기

### FastAPI + Langserve

- Langserve는 LLM을 서빙하기 위해 챗형식 등의 UI를 제공해주고, 쉽게 chain을 구성하도록 돕는 라이브러리
- FastAPI 웹 프레임워크로 애플리케이션을 실행 → 그 내부에서 Langserve가 llm Chain 구성, UI 제공 → 서버에서 Ollama를 통해 동작되는 70B 모델을 Langserve에서 호출
- langserve RemoteRunnable → API 형태로 ngrok URL로 모델을 호출해 사용할 수 있게 해줌

### ngrok

- 로컬 서버를 쉽게 외부에서 접근할 수 있도록 설정하게 해주는 라이브러리
- 계정당 한개 도메인 할당 제공
- [localhost:8000](<http://localhost:8000>) → <https://perfect-nationally-bass.ngrok-free.app/llm/playground/>
- 챗봇 형태의 랩큐라마 사용 가능
