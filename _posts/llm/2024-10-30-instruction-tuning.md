---
title: "[LLM] Instruction Tuning 이란?"
date: 2024-10-30 18:24:28 +0900
categories: llm
tags: llm
header:
  teaser: "../../img/cover/llm_logo.png"
---

LLM 은 어떻게 질문에 잘 대답할까? <br>
Instruction tuning에 대해 알아보자

## **Training** = **Pre-Training** or **Fine-Tuning**

![](/img/2024-07-30/inst-1.png)
<center><small><em>출처 : Clive Gomes(Medium)</em></small> </center>

<br>

### Training과 in-context Learning

- Training(Pre-training, Fine-tuning) → Parameter Update !
    
- In-context learning → Parameter Update X
    
    - Zero-shot, one-shot, Few-shot 예시를 프롬프트에 주는 것


In-context learning + Fine tuning

- In-context learning의 **지시 이행 효과**와 Fine tuning의 **내용** **학습 효과**를 모두 누리고 싶다

⇒ **Instruction tuning** !

----

## Instruction Tuning 이 언급된 논문
### 1. Finetuned Language Models are zero-shot learners(2022년 구글)

![](/img/2024-07-30/inst-2.png)


- “instruction tuning” → instruction을 주는 형태로 **“파인튜닝”** 하는 것
- 파인튜닝이기 때문에 당연히 **Parameter Update**

------

### 2. Instruction tuning with gpt-4 (2023년 마이크로소프트)

- Self-instruct: LLM 모델이 스스로 생성한 결과로 Instruction Dataset을 만들고(본 연구에서는 gpt-4가 생성하도록 함),
- LLaMA 7B에 instruction tuning 함 (Supervised fine-tuning)

![](/img/2024-07-30/inst-3.png)
<center><small><em> 출처 : SELF-INSTRUCT: Aligning Language Models with Self-Generated Instructions (2023)</em></small></center>

<br>

![](/img/2024-07-30/inst-4.png)
<center><small><em> 출처 :https://moon-walker.medium.com/chatgpt%EC%97%90-%EC%A0%81%EC%9A%A9%EB%90%9C-rlhf-%EC%9D%B8%EA%B0%84-%ED%94%BC%EB%93%9C%EB%B0%B1-%EA%B8%B0%EB%B0%98-%EA%B0%95%ED%99%94%ED%95%99%EC%8A%B5-%EC%9D%98-%EC%9B%90%EB%A6%AC-eb456c1b0a4a </em></small></center>

<br>

> Instruction Tuning할 때 보상 모델(reward model)로 <br>
> 강화학습 방법론 RLHF(Reinforcement learning with Human Feedback)을 함께 쓰는 경우가 많은데, <br>
> 이것도 Instruction Tuning의 필수요소인가?

=> RLHF는 더 좋은 답변을 골라 내주는 역할을 할 뿐, 
LLM 모델을 fine-tuning하는 부분의  Instruction Tuning은 같다.
다른 자료에서는 어떻게 설명하는지 살펴보자.

----------

## Instruction Tuning 관련 자료와 논문
### 1. IBM 발표 자료

![](/img/2024-07-30/inst-5.png)

### 2. **Visual Instruction Tuning  - LLaVA(2023)**

![](/img/2024-07-30/inst-6.png)

Encoder(Vision model) + Vicuna에 instruction-following dataset 학습

![](/img/2024-07-30/inst-7.png)

### 3. **Multimodal Instruction Tuning with Conditional Mixture of LoRA** (2024)

![](/img/2024-07-30/inst-8.png)


MLLM을 instruction tuning 할때도 LoRA를 쓰고, 이 논문에서는 mixLoRA라는 새로운 방법을 도입
RLHF 등 다른 방법 언급 없음

### 4. LLaMoCo: Instruction Tuning of Large Language Models for Optimization Code Generation (2024)

![](/img/2024-07-30/inst-9.png)


Instruction Tuning(IT), Alignment Tuning (AT) 은 별개다. 같이 쓸 수 있을 뿐

Aligment Tuning → RLHF, DPO 등 방법

-------
