### RAG (Retrieval-Augmented Generation)

- 외부 지식 기반으로 LLM에 문맥을 제공하여 답변 품질을 높이고 근거 기반을 확보하는 방법

- **Naive RAG**(기본 RAG 방식): Query(유저의 입력)과 벡터 유사도가 높은 Document(문서 뭉치)를 Knowledge base(벡터 DB) 에서 가져와 LLM 답변 생성의 문맥으로 활용

- **Advanced RAG**: RAG 과정을 고도화하여 흐름을 구성하는 방식. Pre-retrieval, retrieval, Post-retrieval, Generation 단계로 구분. 각 단계에 여러 방법론 존재
    - **Pre-retrieval**: Query를 Document 검색에 이용하기 전에, 더 잘 가져올 수 있도록 변환하는 단계
    - **Retrieval**: 실제: 최종 Query를 Document 검색에 이용할 방법을 선정하는 단계
    - **Post-retrieval**: Document 검색 후, 검색해 온 Document들을 LLM의 Context로 이용하도록 변환하는 단계
    - **Generation**: 프롬프트 엔지니어링 등을 활용하여 LLM이 Context를 입력받아 답변을 생성하는 단계

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/2b11c2d2-0032-4cda-b906-bfadd0101ab8/Untitled.png)

### Autorag

- Advanced RAG의 각 단계에서 최적의 방법론을 쉽게 판단할 수 있도록 구조화한 프레임워크
- 각 단계를 Node로 구성해 비교 적용할 방법론을 설정
- 적용할 도메인 자료들을 선정하고, Corpus(자료→ 문서 뭉치), QA(질문 쿼리와 답변) 으로 구성
- 테스트 실행, 결과 확인

### 테스트 데이터셋

- 한국자동차연구원 프로젝트에서 활용하는 자료들로 Corpus와 QA셋 제작
    
- 자료
    

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/67475fd4-5647-4432-a85c-37f66321bb5a/Untitled.png)

- QA (평가 데이터셋)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/1578ba60-0121-44b9-82db-3276dbf7d95d/Untitled.png)

- 162개 → 127개
    
    - Autorag이 생성한 QA 테스트셋 중, 직접 인간 확인하여 127개 선정
        
    - 제외 예시
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/777f6669-3abe-4b44-9da5-56edd59c33d1/Untitled.png)
        
- 평가 대상(방법론) 설정
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/ac9fa969-bf01-42bc-b71a-0d13af78755c/Untitled.png)
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/4cbda966-7701-4da4-bc4a-649de686aaa9/Untitled.png)
    
- 실험 설정
    
    - config.yaml
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/3a6f48af-2883-4c6d-8a15-c39665300285/Untitled.png)
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/be8b3a3a-294e-4acf-973d-7ecdd9df8bc6/Untitled.png)
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/8664ac11-3dc6-420b-83ae-c3ccd25909a3/Untitled.png)
    
- 실험 결과
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/352ba54e-ccdc-454f-b7f9-9a8d27768211/Untitled.png)
    
    - Pre-retrieval
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/ff2cdbda-e172-444b-a8c2-aa7518c348cc/Untitled.png)
        
        - Hyde: Query에 대한 가정적 답변을 만들고, 이 답변을 수정된 Query로 활용
        - Multi-query: 실제 Query와 유사하지만 다른 여러 Query를 만들고 실제 query와 함께 활용
        - **Pass: 수정하지 않은 원본 query 활용** ✅
    - Retrieval
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/f0ba0227-32b6-45ff-b5be-541f1d8a3066/Untitled.png)
        
        - bm25: TF-IDF 계열 검색 알고리즘으로, Query에 나온 단어들이 가장 많이 등장한 문서를 가져오는 개념
            
        - VectorDB: Embedding Model을 이용하여 Document를 벡터화하여 저장하고, Query를 벡터화하여 유사도를 측정해 가장 유사한 문서를 가져오는 개념
            
            - Embedding Model 후보: Openai (ada-002), infloat_inst, bge_m3
                
            - RAG 위한 한국어 embedding model 순위
                
                [GitHub - Atipico1/Kor-IR: Kor-IR: Korean Information Retrieval Benchmark](https://github.com/Atipico1/Kor-IR)
                
                ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/664bd81a-973d-44ea-9be2-ad8570387f4a/Untitled.png)
                
            - **BM25가 가장 좋은 성능 ✅,** bge_m3가 그 다음이었고, Hybrid 에서는 bm25에 가중치를 더 크게 부여할수록 높은 성능
                
        - Hybrid CC: 두 방법을 섞어서 쓰는 방법(각각에 가중치 부여)
            
    - Post-retrieval
        
        - Reranker: 검색해온 문서들을 유사도가 높은 순서로 Re ranking 하는 것
            
            Query와 문서 뭉치를 한번에 모델에 넣어 점수를 계산. 한국어 성능이 좋은 모델로 랭킹을 다시 매기는 개념
            
        - Reranker를 쓰지 않는 경우(pass) 보다 쓰는 경우가 좋음 ✅
            
            ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/d044429b-f2e1-4863-a550-1c0412f860b5/Untitled.png)
            
        - Compressor: 검색한 문서들을 압축하는 방법
            
            - 이 실험에서는 Tree-summarize 이용. 바텀업 방식으로 문서들을 요약해나간 후 context로 활용
                
                ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/63484f11-fba5-4103-b531-90ae51e06671/Untitled.png)
                
            - Compressor를 쓰지 않는 경우(pass)가 좋음 → 요약할 경우, 정보의 손실이 일어나기 때문 ✅
                
        - Long-context-reorder: 논문에 따르면 중요한 정보가 프롬프트의 시작과 끝에 있을 때 생성 성능이 높음
            
            ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/1d6d718f-f6c6-4f1b-853e-6d44bc16faa5/Untitled.png)
            
        - 처음과 끝에 재배치 후에 성능이 더 높음
            
            ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1078a8e6-6061-4d42-9121-a6b29d21abb2/72860304-9246-4d00-827f-cedceba5cab5/Untitled.png)
            
- 결론
    
    - 한자연 자료의 경우, Query는 변형해서 사용하기보다 원본을 이용하는 것이 더 유리
    - embedding 유사도 검색보다 키워드 기반 검색이 더 유리 (BM25). 하지만, 키워드 기반에 가중치를 더 부여하면서 하이브리드로 적용하는 것이 좋을 것
    - Reranker가 더 유리하며, 더 성능이 좋다고 알려진 bge-m3모델로 reranking하면 더욱 좋을 것
    - Compressor(요약)는 정보를 손실해 성능을 낮추지만, 토큰 수를 줄여 비용을 줄이기 때문에 Trade-off 고려하여 선택
    - Long-context-reorder: 처음과 끝에 중요도가 높은 문서 배치하는 것이 좋을 것
- 보완점
    
    - 평가 데이터셋을 구축하는 과정에서 Loader와 Chunking, 전처리가 깊게 다뤄지지는 않음
    - 평가 데이터셋을 구축하는 것이 중요하지만, 이는 그 자체만으로 새로운 연구주제로 선정해야 할만큼 공을 들여야 할 일