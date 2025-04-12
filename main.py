# 환경 변수(예: API 키)를 가져오기 위해 사용하는 
# 파이썬 기본 모듈. 코드에서 불러올 수 있게 도와주는 도구.
import os

# dotenv : .env 파일에 저장된 환경 변수를 파이썬 코드에서
# 사용할 수 있게 해주는 파이썬 라이브러리
# load_dotenv() 함수: .env 파일을 찾아서 그 안의 내용을
# 운영체제의 환경 변수로 등록해줌.
from dotenv import load_dotenv

# openai 라이브러리 안의 OpenAI 클래스를 불러옴.
# OpenAI나 호환 API(Together 등)에 접속할 수 있는 클라이언트 역할.
from openai import OpenAI

# 현재 디렉토리에 있는 .env 파일을 불러와서, 그 안의 환경 변수들을
# os.environ에서 사용할 수 있게 만들어줌.
load_dotenv()

# .env 파일에서 "API_KEY"라는 이름의 환경 변수를 가져와서 API_KEY에 저장.
API_KEY = os.environ["API_KEY"]

# "SYSTEM_MESSAGE"도 마찬가지로 불러오는데, 
# 만약 없으면 "You are a helpful assistant."라는 기본 문장을 대신 사용.
SYSTEM_MESSAGE = os.environ["SYSTEM_MESSAGE"]

# Together API의 기본 주소를 설정.
BASE_URL = "https://api.together.xyz"

# 사용할 모델 이름을 설정 (LLaMA 3.1 70B 모델)
MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"

# OpenAI 클라이언트 객체 생성. 이 객체를 이용해 API를 호출할 수 있음.
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 대화 기록을 저장하는 리스트
messages = [
 {"role": "system", "content": SYSTEM_MESSAGE}
]

# 사용자에게 챗봇 사용 안내 문구 출력.
print("챗봇을 시작합니다! (종료하려면 'exit' 또는 'quit 입력)")

## 대화 시작
while True:
 user_input = input("You: ") # 사용자에게 입력을 받음음
 if user_input.lower() in ["exit", "quit"]:
    print("챗봇을 종료합니다.")
    break
 
# 사용자의 입력을 messages 리스트에 추가해서, 대화 히스토리에 반영.
 messages.append({"role": "user", "content": user_input})


 response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    temperature = 0.7 ## 응답의 창의성(0에 가까울수록 논리적) 0.0 ~ 1.0 / 0.8에서 0.9부터 헛소리 시작
)

 AI_answer = response.choices[0].message.content ## 응답에서 실제 텍스트 메시지만 뽑아옴.
 # choices[0] : 첫 번째 응답 (보통 하나만 있음)
 # .message.content: 그 응답의 텍스트 내용
 print("AI_answer: ", AI_answer) # 챗봇의 응답을 출력

# 챗봇의 응답도 대화 히스토리에 추가
 messages.append({"role": "assistant", "content": AI_answer})


#----write down my idea-----
# 지구과학 교사와 여행 전문가인 챗봇으로,
# 아이들의 교육기관에서(유치원, 초등학교 등)
# 교사의 부재 시 아이들이 부담없이 질문할 수 있다.
# 음성인식을 하여 스스로 자연어 처리만 가능하다면,
# 교육기관에서 충분히 실용성이 있다고 생각한다.
#---------------------------