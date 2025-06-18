---
title: "[LLM] Advanced RAG - Hyde, Rerank, Hybrid search 구현"
date: 2025-06-10 18:24:28 +0900
categories: llm
tags: llm RAG hyde rerank 
header:
  teaser: "../../img/cover/llm_logo.png"
---

LLM + Advanced RAG로 최적의 답변을 받아내는 방법

### RAG (Retrieval-Augmented Generation) 란?

- 외부 지식 기반으로 LLM에 문맥을 제공하여 답변 품질을 높이고 근거 기반을 확보하는 방법<br>

- **Naive RAG(기본 RAG 방식)**: Query(유저의 입력)과 벡터 유사도가 높은 Document(문서 뭉치)를 Knowledge base(벡터 DB) 에서 가져와 LLM 답변 생성의 문맥으로 활용<br>

- **Advanced RAG**: RAG 과정을 고도화하여 흐름을 구성하는 방식. Pre-retrieval, retrieval, Post-retrieval, Generation 단계로 구분. 각 단계에 여러 방법론 존재
    - **Pre-retrieval**: Query를 Document 검색에 이용하기 전에, 더 잘 가져올 수 있도록 변환하는 단계
    - **Retrieval**: 실제: 최종 Query를 Document 검색에 이용할 방법을 선정하는 단계
    - **Post-retrieval**: Document 검색 후, 검색해 온 Document들을 LLM의 Context로 이용하도록 변환하는 단계
    - **Generation**: 프롬프트 엔지니어링 등을 활용하여 LLM이 Context를 입력받아 답변을 생성하는 단계
<br>

----------


### Hyde (Hypothetical Document Embeddings)

pre-retrieval의 한 기법으로 문서를 검색하는 쿼리에 변형을 준다.

- 주어진 질의를 기반으로, 해당 질의를 더 잘 설명하거나 확장할 수 있는 가상의 문서를 생성하는 방식
- 문제 상황: **vectorDB search** 시, **query**(”손흥민 업적 알려줘”)와 **DB 문서**(”대한민국 축구 역사 관련 문서”) 의 괴리로 유사도 검색이 힘들다.
- 만약 **query**(“손흥민은 아시안게임, 올림픽, 월드컵 등 다양한 국가대표 경기에서 활약했다.”)를 기준으로 DB문서를 검색한다면 더 정확하게 가져올 수 있을 것.
- → **query**에 대한 **가정적(가짜) 답변**을 일단 생성하고, 이 답변을 쿼리로 이용해 검색하는 방법

- 이슈
    - ~~쿼리 뿐만 아니라 기존 document까지 hyde 해버린다 → 해결~~
    - 현재 개발중인 서비스에 적용된 Multiquery 방식과 유사. query에 해당하는 비슷한 다른 쿼리들도 만들어서 검색 → 어떤 것이 더 나을까? 혹은 둘 다 적용 가능
    - LLM을 한번 더 거친다 (비용문제) 현 상태의 Multiquery와 비슷한 수준의 토큰 비용

--------


### Hyde 코드 구현 with Langchain

```python
# llm과 base_embedding 설정하기
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", n=4)
base_embeddings = OpenAIEmbeddings()

prompt_template = """Please write only a passage to answer the question in korean 
Question: {question}
Passage:"""

prompt = PromptTemplate(input_variables=["question"], template=prompt_template)
llm_chain = LLMChain(llm=llm, prompt=prompt)

# hyde embedding 설정하기
from langchain.chains import HypotheticalDocumentEmbedder
hyde_embeddings = HypotheticalDocumentEmbedder(
	llm_chain=llm_chain, base_embeddings=base_embeddings
	)

                                                  
# vectorDB 생성하기
from langchain_community.vectorstores import Chroma

vectorstore = Chroma.from_documents(documents=splits,
                                   collection_name='collection-1',
                                   embedding=hyde_embeddings)
                                   
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# Hyde 적용된 vectorDB 쿼리하고 답변 생성하기
from langchain.schema.runnable import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate, ChatPromptTemplate

template = """Answer the following question based on this context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
def format_docs(docs):
   return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
   {"context": retriever | format_docs, "question": RunnablePassthrough()}
   | prompt
   | llm
   | StrOutputParser()
)
response = rag_chain.invoke("What are different Chain of Thought(CoT) prompting?")
print(response)
```

### Rerank 이해 및 구현

post-retrieval의 한 기법으로 검색해 온 문서의 입력 순서를 재조정(정렬)한다.


- **초기 검색**: 사용자가 질의를 입력하면, 모델은 이 질의를 기반으로 여러 문서를 검색. 이 단계에서는 단순한 유사도나 키워드 매칭을 통해 초기 후보 문서들 선택
- **재정렬 (Reranking)**: 초기 검색된 문서들 중에서 가장 관련성이 높은 문서를 선택하기 위해 추가적인 평가를 수행. 이를 위해 더 복잡한 알고리즘이나 더 고도화된 언어 모델을 사용하여 각 문서의 점수를 다시 매기고, 이 점수에 따라 문서를 재정렬

- 관련성 높은 컨텍스트를 **프롬프트의 어디에 위치시키는가**도 성능에 영향을 줌
    
    ![](/img/2025-06-10/0610-1.png)

    

- search 해 온 documents를 모두 컨텍스트로 넣는 것은 토큰 비효율적.
1. **기존의 벡터 검색 방식으로 대규모 문서 중 질문과 관련성이 높을 것 같은 후보군을 검색**하고,  2. 검색된 문서들에 대해 **reranker기반으로 관련성을 재 측정** 
- 여기서 rerank하는 모델을 한국어 잘하는 reranker 로컬 모델을 불러와서 씀
    - 🔗[ko-reranker](https://huggingface.co/Dongjin-kr/ko-reranker "https://huggingface.co/Dongjin-kr/ko-reranker")
    - 🔗[bge-m3](https://huggingface.co/BAAI/bge-m3 "https://huggingface.co/BAAI/bge-m3")

- 한국어 RAG 임베더 순위

- reranker는 쿼리와 후보 컨텍스트가 한 입력으로 들어가 유사도 점수를 내는 방식.

- 이슈
    - retriever 가 가져온 닥스들을 rerank → 그럼 지금처럼 4개 안가져오고 20개 가져와서 rerank해서 4개만 쓰는 방식 고려

    <br>

    **Rerank 코드구현 with transformers**
    
    ```python
    # context 후보군 1차 선정(현 Prop 시스템과 같음)
    
    query = '메타버스 서비스 예시'
    cand_docs = retriever.get_relevant_documents(query)
    
    # Reranker 적용
    import torch
    import numpy as np
    
    # 정규화 소프트맥스 함수 -> 최종 reranking 점수 산출
    def exp_normalize(x):
        b = x.max()
        y = np.exp(x - b)
        return y / y.sum()
        
    # rerank 모델 불러오기 
    from transformers import AutoModelForSequenceClassification, AutoTokenizer
    
    model_path = "Dongjin-kr/ko-reranker"
    
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    model.eval()
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    # 후보 컨텍스트 준비
    cand_texts = [doc.page_content for doc in cand_docs]
    cand_source = [doc.metadata['source'] for doc in cand_docs]
    
    # [query, 후보1], [query, 후보2, ...]
    pairs = list(map(lambda x: [query, x], cand_texts)) 
    
    # Reranking score 계산
    with torch.no_grad():
        inputs = tokenizer(pairs, padding=True, truncation=True, return_tensors='pt', max_length=512)
        scores = model(**inputs, return_dict=True).logits.view(-1, ).float()
        scores = exp_normalize(scores.numpy())
        print(scores)
        
    # Reranking 후, 상위 4개 선정
    import pandas as pd
    
    df = pd.DataFrame({
        'texts': cand_texts,
        'scores': scores
    })
    
    sorted_df = df.sort_values(by='scores', ascending=False)
    sorted_df[:4]['texts'].to_list()
    
    ```
    

### **BM25 Retriever**

BM25는 키워드 기반의 랭킹 알고리즘으로, 이를 이용해 유사한 문서를 찾아오는 방식

BM25(a.k.a Okapi BM25)는 주어진 쿼리에 대해 문서와의 연관성을 평가하는 랭킹 함수로 사용되는 알고리즘으로,TF-IDF 계열의 검색 알고리즘 중 SOTA 인 것으로 알려져 있음

IR 서비스를 제공하는 대표적인 기업인 엘라스틱 서치에서도 ElasticSearch 5.0서부터 기본(default) 유사도 알고리즘으로 BM25 알고리즘을 채택

- 의미 유사성이 아닌 단어가 많이 나왔는가를 보는 **Sparse Retriever**

<br>

**BM25 알고리즘 구현**

```python
import jsonlines
import pandas as pd
from rank_bm25 import BM25Okapi

def read_jsonl(path):
    data = list()
    with jsonlines.open(path) as f:
        for line in f:
            data.append(line)
    return data

train_data = read_jsonl('./data/nikluge-sa-2022-train.jsonl')
corpus = [data['sentence_form'] for data in train_data]
tokenized_corpus = [doc.split(" ") for doc in corpus] # 띄어쓰기 기준 구분

for idx, doc in enumerate(tokenized_corpus): # 데이터 예시
    if idx < 5:
        print(doc)
        
        
bm25 = BM25Okapi(tokenized_corpus)
query = "촉촉하고 부드럽다"
tokenized_query = query.split(" ") 
doc_scores = bm25.get_scores(tokenized_query)
result = pd.DataFrame({
    'text': corpus,
    'score': doc_scores
})
result.sort_values(['score'], ascending=False)
```

### BM25 Retriever 구현 및 한국어 토크나이저 활용법

```python
from kiwipiepy import Kiwi

kiwi = Kiwi()

class ChromaHandler(BaseVectorDBHandler):
    def _kiwi_tokenize(text):
      return [token.form for token in kiwi.tokenize(text)]
      
    def search_db(self, query: str, vectordb_prompt: PromptTemplate, k=4, file_type='Ref'):
        db = self._connect(file_type)
        
        retriever = db.as_retriever(search_type="mmr", search_kwargs={"k": k})
        
        if file_type == 'Ref':
            documents = [Document(page_content=doc, metadata=meta) for doc, meta in zip(db.get()['documents'], db.get()['metadatas'])]
            
            bm25_retriever = BM25Retriever.from_documents(documents, preprocess_func=self._kiwi_tokenize)
            bm25_retriever.k = k

            retriever = EnsembleRetriever(
                retrievers=[bm25_retriever, retriever], weights=[0.25, 0.75]
            )
    
```

- Sparse retriever와 dense retriever를 결합해 Hybrid Search를 하면 더욱 도움
- 앙상블 기법의 일종으로, 각 방법에 가중치를 주어 문서 검색