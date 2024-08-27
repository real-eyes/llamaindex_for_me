# Vector 지정
from llama_index.core import VectorStoreIndex

# Web Reader
from llama_index.readers.web import BeautifulSoupWebReader

# openai 정의
from llama_index.llms.openai import OpenAI
# Anthropic 정의
from llama_index.llms.anthropic import Anthropic

import pandas as pd

df = pd.read_excel('./input_url.xlsx')
my_input = list(zip(df['link']))
my_output = []


# 로더 정의
loader = BeautifulSoupWebReader()

# input_url = "https://google.com/report/20200909", 접근 예시

for input_url in my_input:
    documents = loader.load_data(urls=[input_url])

    llm = OpenAI(temperature=0.3, model="gpt-4o", max_tokens=2048, api_key=os.getenv("OPENAI_API_KEY"))
    # llm = Anthropic(model="claude-3-5-sonnet-20240620") # 만약, Claude로 변경을 원할 시

    index = VectorStoreIndex.from_documents(documents)
    chat_engine = index.as_chat_engine(llm=llm)

    script_ready = [
        "해당 문서의 중요 포인트와 문서의 중요한 파트를 순서대로 서술하시오.",
        "네가 했던 답변을 한 문장으로 이어지는 한국어로 100~200자 정도로 요약하시오. 주의점은 공격 설명과 공격 체인을 따로 설명하지 않을 것."
    ]

    for question in script_ready:
        streaming_response = chat_engine.stream_chat(question)
        # print(f"user: {question}") # python notebook 환경 한정.
        print("answer: ",end="")
        for token in streaming_response.response_gen:
            print(token, end="")
        print("\r\n")   # 개행처리
    my_output.append(streaming_response.response)
