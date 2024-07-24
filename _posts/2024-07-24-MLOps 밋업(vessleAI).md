---
layout: post
title: MLOps 밋업(vessleAI)
date: 2024-07-24 21:51 +0900
categories:
  - LLM
  - MLOps
tags: 
math: true
---

## Session 1. Building AI-native applications with Weaviate (Bob van Luijt)


### AI-native database

머신러닝이 핵심인 애플리케이션의 DB. 이 애플리케이션에서 모델을 빼면 의미가 없을 때의 DB

이는 곧 VectorDB인데, Weaviate는 기존 VectorDB의 한계를 극복하는 방식

- VectorDB는 Query와 저장된 vector들 각각의 distance를 비교
- VecorDB가 커지면 비교 시간 ↑, 저장 용량 ↑
- New algorithm 도입해서 속도 업, 클라우드 기반으로 vectorDB를 불러올 수 있게 해서 용량 효율

종합적으로 Weaviate는 VectorDB 사용 용이성, 저장 공간, 필터링, 속도 측면에서
LLM 서비스 프로덕션을 쉽게 해준다

LLM과 RAG 시스템 + VectorDB 인터그레이션 제공

-------------------------------
------------
-----------

## Session 2. LLMOps에서 AGI까지 - 산업별 2024년 최신 사례(Vessl AI)

- 고객이 가진 자료로 학습시킨 LLM 모델을 쉽게 만들도록 돕는 서비스 (ex. Diffy)

MLOps의 미래는 범용 인공지능 시스템


현재: AI agent/pipeline : Model A 임무 수행(ex. search) 결과 반환 -> Model B action

다음: 특정 영역에 특화된 AI 시스템 구축

미래: 각 영역에 특화된 AI 시스템을 통합하여 범용 인공지능 시스템으로 도약


참고: Meta의 Arcadia "end-to-end AI system simulator"
- AI 시스템의 컴퓨팅, 메모리, 네트워크 성능 평가 및 최적화
- 설계 및 운영 효율성 증대


-----
------
------

## Session 3. 처음부터 다시 LLM 애플리케이션을 개발한다면(Liner)
허훈 - 11월에 mlops now 유튜브도 확인


이전부터 LLM 애플리케이션 개발언어로 Go를 선택. 그러나 다시 한다면 Python으로 할 것
- Python의 개발 생태계 성장은 놀라울 정도
- AI 서비스 구축을 위해 Python은 모든 기능을 쉽게 시도해 볼 수 있음

LLM 애플리케이션 개발 시 고려해야 할 3가지
"Ochestration", "Cost Operation", "Fine-Tuning"

----

### Ochestration

어떤 모델을 쓸 것인가?
- Factor(성능, 속도, 비용)  고려해서 모델 선택 or 사용자가 원하는 모델 선택

Fall back 상황
 - 지나치게 긴 요청
 - rate limit
 - 막상 성능보다는 속도나 비용이 중요할 때
 - 사용자가 원하는 모델을 선택하고 싶을 때
 - 원치 않는데 모델별 필터링 걸림

OpenAI, Anthropic, Google 의 SDK 에러핸들링 방법이 다름

고려하는 라이브러리
"LiteLLM"
: 요청에 따라 다른 모델을 호출할 수 있도록 분기
: budgetmanager 메소드 - 특정 사용자가 얼마나 쓰고 있는지 확인

"RouteLLM"
: Ideal Router는 싸면서 퍼포먼스는 어느정도 나오는 것
답변 쉬운 쿼리는 쉬운거 처리하는 router(모델)로 분기
쿼리에 따라 유연하게 처리해서 궁극적으로는 속도 업


------

### Cost Operation

LLM 비용관리
SW 비용 구조에서 기존에는 고정비로 들어가야 하지만, LLM cost를 변동비로 설정

미시적 관점의 관리
컴포넌트(agent)별로 비용 확인
- 어떤 기능에서 비용이 많은지

거시적 관점의 관리
- OpenAI(GPT-4o)는 3시간 유료 사용자 80 requests, 무료 사용자 40 requests로 제한
- 이는 랜덤하게 설정한 게 아닌, 한 명의 사용자에게서 얻을 수 있는 가치, LTV(LifeTime Value) 고려한 것
- Ideal Router 사용해서 비용 확인하고, 적정 투자 가능 수치를 적용


-------

### Fine-tuning

Fine-tuning을 시도할 단계

phase 1. openai, anthropic - PEFT
- 좋은 모델에 쉽게 FT할 수 있도록 구성

phase 2. Fireworks AI, Together AI - PEFT
- 사용자가 원하는 방향으로 FT할 수 있도록 도움

phase 3. Lambda - PEFT, Full-paramter tuning, post-training
- GPT 클러스터 확보해서 직접 학습, 서빙 최적화

FT 해야만 하는 이유가 있다면 하자
1.  만약 FT해서 쓰는게 API보다 더 비용 적게 든다면
2.  기술적으로 특정 태스크를 FT로 훨씬 잘하게 할 수 있다면
3.  우리만이 가지고 있는 DATA를 사용하는 경우 이득을 취할 수 있는 경우


----------------

























































