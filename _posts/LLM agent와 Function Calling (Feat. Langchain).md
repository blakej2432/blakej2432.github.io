---
layout: post
title: ""
date: 2024-07-25 21:56 +0900
categories:
  - LLM
  - Agent
tags: 
math: true
---
### Function Calling과 Agents

- Function Calling이란?
    - LLM이 상황에 맞게 외부의 Function(tool)과 소통하도록 하는 것
- LLM Agents란?
    - 답변을 위해 스스로 생각하고, 도구를 활용해 답을 얻고 스스로의 생각을 조정하면서 최종 답변에 이르는 일련의 과정을 거치는 LLM 주체

![](https://i.imgur.com/5EzFyYk.png)


1. 유저가 Prompt 입력

2. App이 Prompt와 Function 선언 → LLM에 전달

3. Model은 이 상황에 필요한 Function과 이에 필요한 Parameter value 반환

4. App은 이 Model의 response 바탕으로 API 호출

5. API 응답

6. API response를 Model에 전달

7. Model Response 반환

8. app은 유저에게 최종 답변 전달
    

### Agent Chatbot Architecture

![](https://i.imgur.com/ShTdDVk.png)


- 유저 입력을 받으면 답변을 위해 Reasoning 하면서 Functions(get_items, purchase_item, rag_pipeline_func) 중 어떤 걸 쓸지 스스로 판단
- 모델이 위 function을 호출하면, RDB, VectorDB, websearch 등을 수행하여 얻은 결과 값을 활용한 후 다음 thought 단계로 진행
-----

### Langchain 에서 사용하기

[Build an Agent | 🦜️🔗 LangChain](https://python.langchain.com/v0.2/docs/tutorials/agents/#installation)

```python
from langchain_community.vectorstores import Chroma from langchain_community.document_loaders import PyPDFium2Loader from langchain_text_splitters import RecursiveCharacterTextSplitter from langchain_openai import OpenAIEmbeddings 

embedding_function = OpenAIEmbeddings() 

# 데이터 로드 
loader = PyPDFium2Loader("국가안전시스템 개편 종합대책 대국민 보고(12.31. 기준).pdf") documents = loader.load() 
documents 

# 벡터 DB 
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=30) 
docs = text_splitter.split_documents(documents)
db = Chroma.from_documents(docs, embedding_function) 

from langchain_community.vectorstores import Chroma 
from langchain.agents.agent_toolkits import create_retriever_tool 
from langchain.agents import initialize_agent, AgentType, Tool 

chroma_retriever = db.as_retriever(search_type="mmr", search_kwargs={"k": 2}) 

# agent가 사용할 Tool 설정 
retriever_tool = create_retriever_tool( 
   chroma_retriever, 
   name="doc_search", 
   description="답변을 위한 정보를 담은 문서를 찾아옵니다.",
    ) 
tools = [retriever_tool] 

from langchain import hub 

# agent 용 prompt 불러오기
prompt = hub.pull("hwchase17/react-json") 

from langchain_openai import ChatOpenAI llm = ChatOpenAI(model="gpt-4o", temperature=0) from langchain.agents import AgentExecutor, create_react_agent 
from langchain.agents.output_parsers import ReActJsonSingleInputOutputParser 
from langchain.tools.render import render_text_description_and_args 

# agent 생성 
agent = create_react_agent( 
   llm, 
   tools, 
   prompt, 
   tools_renderer=render_text_description_and_args,
	output_parser=ReActJsonSingleInputOutputParser(),
	 ) 
	 
 from langchain.agents import AgentExecutor 

# agent 선언 후 실행
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True) 
response = agent_executor.invoke({"input": "119 구급 스마트시스템 개발·운영을 시작한 년도의 시군구 지역안전관리위원회 개최 횟수는? 횟수만 출력해줘"}) 

response
```

- Agent는 답변을 위해 추론을 진행하면서 사용할 수 있는 Tool(이 예시에서는 Retriever)을 활용해 답변
