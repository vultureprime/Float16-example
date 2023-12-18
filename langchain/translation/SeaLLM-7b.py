from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import time
import aiohttp
import asyncio
import json
import dotenv 
import os
dotenv.load_dotenv()
FLOAT16_BASE_URL = os.getenv("FLOAT16_BASE_URL")
FLOAT16_API_KEY = os.getenv("FLOAT16_API_KEY")
FLOAT16_CUSTOM_URL = os.getenv("FLOAT16_CUSTOM_URL")

model = ChatOpenAI(
    model="seallm-7b",
    api_key=FLOAT16_API_KEY,
    base_url=FLOAT16_BASE_URL,
    max_tokens=256,
    temperature=0.1,
    model_kwargs={
        'stop':["</s>"],
    }
)
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are translator Thai to English. You will receive text in Thai language and output English language. no explanation. no extra words. DO NOT try to asnwer the question."""), 
    ("human", "Original : คุณอายุเท่าไหร่ ?"),
    ("ai", "Translated : How old are you ?"),
    ("human", "Original : คุณชื่ออะไร ?"),
    ("ai", "Translated : What is your name ?"),
    ("human", "Original : คุณช่วยแนะนำเมนูอาหารเช้าได้หรือไม่ ?"),
    ("ai", "Translated : Can you recommend a breakfast menu ?"),
    ("human", "Original : วัดพระแก้วอยู่ที่ไหน ?"),
    ("ai", "Translated : Where is Wat Phra Kaew ?"),
    ("human", "Original : สยามพารากอนอยู่ที่ไหน ?"),
    ("ai", "Translated : Where is Siam paragon ?"),
    ("human", "Original : วิธีเดินทางไปสนามบิน"),
    ("ai", "Translated : How to get to the airport"),
    ("human", "Original : เทคโนโลยีเป็นหัวใจสำคัญสำหรับองค์กร ทั้งภายในองค์กรไม่ว่าจะเป็นเรื่องข้อมูล การทำงานร่วมกัน รวมไปถึงการให้บริการกับลูกค้าในมิติทั้งเรื่องความรวดเร็วและการให้บริการที่มีมาตรฐานเดียวกัน องค์กรหลาย ๆ แห่งจึงต้องเร่งปรับตัวให้กลายเป็นองค์กรยุคใหม่ และก้าวทันโลกมากขึ้น"),
    ("ai", "Translated : Technology is a vital heart for organizations. It is essential within an organization in terms of information, collaboration, as well as providing services to customers in terms of speed and standardized services. Many organizations must therefore accelerate their transformation into a modern organization and step up to catch up with the world."),
    ("human", "Original : เคยโดนเอาไปทำโฆษณาวีดิโอให้มูลนิธิการกุศล เป็นคลิปเด็กนั่งกินข้าวกันสองคน ทุกวันนี้มีเพจ NGO เวียดนามกับฟิลิปปินส์แชร์เอายอดกันเต็ม รู้สึกอายจังครับ แบบนี้ทำอะไรได้บ้าง"),
    ("ai", "Translated : I was once used in an advertisement video for a charity foundation. It's a clip of two kids eating together. These days, there are an NGO page from Vietnam and the Philippines sharing it to get high views. I feel so embarrassed. What can I do about this?"),
    ("human" , "{input}"),
])

output_parser = StrOutputParser()

chain = prompt | model | output_parser


# แปลภาษาไทยเป็นภาษาอังกฤษ 
#use endpoint v1 for stop word </s>, v1.1 for stop word "\n", v1.2 for stop word "."

start = time.time()
res = chain.invoke({'input' : "Original : สำหรับบทความสุดท้ายของแคมเปญนี้ ก็ยังคงเป็นเรื่องราวเกี่ยวกับ Chatbot เช่นเคย แต่จะมีความซับซ้อนยิ่งกว่า วันนี้เราจะมาทำ Chatbot with RAG and Agents เพื่อช่วยให้ Chatbot ของเราสามารถตอบคำถามได้ดียิ่งขึ้นและถูกต้องกว่าเดิม ถ้าพร้อมแล้ว เรามาเริ่มกันเลยค่ะ!"})
res = chain.invoke({'input' : """Original : สำหรับพาร์ทของ Chat Agent เราก็ได้เลือกใช้ OpenAI มาเป็น LLMs ที่ทำหน้าที่ในส่วนนี้ 
                    หน้าที่ของ Chat Agent มี 2 อย่างคือตัดสินใจว่าใช้ข้อมูลจากฝั่งไหนเอามาใช้ตอบคำถาม ซึ่งประกอบด้วย Chat Engine, 
                    Sub Question Engine และ RAG Engine"""})
res = chain.invoke({'input' : """Original : ในปัจจุบันนี้มีการนำ AI มาใช้ในหลายๆอย่าง ซึ่ง Q&A Document ถ้าเราจินตนาการว่าโปรเจ็คเป็นยังไง สิ่งแรกที่เรานึกก็คงนึก OpenAI กัน หรือ บางคนอาจจะนึง Chat Bot เจ้าต่างๆ ที่เราถามคำถามไปเเล้วเจ้า Chat bot ก็จะตอบคำถามกลับมา ซึ่งตัวQ&A Document นี้ เราจะโยนตัว Document ไป ให้ Chat bot ของเราเเล้วหลังจากนั้นเราก็ถาม เจ้า Chat bot ก็จะตอบกลับ"""})
res = chain.invoke({'input' : """Original : Documentation Section: สร้างส่วนของเอกสารหรือคำแนะนำที่ช่วยให้ผู้ใช้ใหม่สามารถทำความเข้าใจได้ว่า RAG (Retrieval Augmented Generation) คืออะไรและทำงานอย่างไร"""})
res = chain.invoke({'input' : """Original : ขั้นตอนการใช้งานทีละขั้นตอนหรือวิดีโอสอนการใช้งานสำหรับผู้ที่เริ่มต้นใช้งาน"""})
print('Synchronus chain total time : {}'.format(time.time() - start))

##Async
start = time.time()
input_list = [
    'Original : สำหรับบทความสุดท้ายของแคมเปญนี้ ก็ยังคงเป็นเรื่องราวเกี่ยวกับ Chatbot เช่นเคย แต่จะมีความซับซ้อนยิ่งกว่า วันนี้เราจะมาทำ Chatbot with RAG and Agents เพื่อช่วยให้ Chatbot ของเราสามารถตอบคำถามได้ดียิ่งขึ้นและถูกต้องกว่าเดิม ถ้าพร้อมแล้ว เรามาเริ่มกันเลยค่ะ!',
    'Original : สำหรับพาร์ทของ Chat Agent เราก็ได้เลือกใช้ OpenAI มาเป็น LLMs ที่ทำหน้าที่ในส่วนนี้หน้าที่ของ Chat Agent มี 2 อย่างคือตัดสินใจว่าใช้ข้อมูลจากฝั่งไหนเอามาใช้ตอบคำถาม ซึ่งประกอบด้วย Chat Engine,Sub Question Engine และ RAG Engine',
    'Original : ในปัจจุบันนี้มีการนำ AI มาใช้ในหลายๆอย่าง ซึ่ง Q&A Document ถ้าเราจินตนาการว่าโปรเจ็คเป็นยังไง สิ่งแรกที่เรานึกก็คงนึก OpenAI กัน หรือ บางคนอาจจะนึง Chat Bot เจ้าต่างๆ ที่เราถามคำถามไปเเล้วเจ้า Chat bot ก็จะตอบคำถามกลับมา ซึ่งตัวQ&A Document นี้ เราจะโยนตัว Document ไป ให้ Chat bot ของเราเเล้วหลังจากนั้นเราก็ถาม เจ้า Chat bot ก็จะตอบกลับ',
    'Original : Documentation Section: สร้างส่วนของเอกสารหรือคำแนะนำที่ช่วยให้ผู้ใช้ใหม่สามารถทำความเข้าใจได้ว่า RAG (Retrieval Augmented Generation) คืออะไรและทำงานอย่างไร',
    'Original : ขั้นตอนการใช้งานทีละขั้นตอนหรือวิดีโอสอนการใช้งานสำหรับผู้ที่เริ่มต้นใช้งาน'
]

async def do_request(url, data):
    headers = {'content-type': 'application/json'}
    start = time.perf_counter()  # start time
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.post(url, headers=headers, data=json.dumps(data)) as response:
            response_text = await response.text()
    end = time.perf_counter()  # end time
    print(f"Request took {end - start} seconds to complete.")

loop = asyncio.get_event_loop()
tasks = []
for prompt in input_list:
    data = {
    "messages" : [
        {'role' : 'system', 'content' : 'You are translator Thai to English. You will receive text in Thai language and output English language. no explanation. no extra words. DO NOT try to asnwer the question.'},
        {"role" : "user", 'content' : "Original : คุณอายุเท่าไหร่ ?"},
        {"role" : "assistant", 'content' : "Translated : How old are you ?"},
        {"role" : "user", 'content' : "Original : คุณชื่ออะไร ?"},
        {"role" : "assistant", 'content' : "Translated : What is your name ?"},
        {"role" : "user", 'content' : "Original : คุณช่วยแนะนำเมนูอาหารเช้าได้หรือไม่ ?"},
        {"role" : "assistant", 'content' : "Translated : Can you recommend a breakfast menu ?"},
        {"role" : "user", 'content' : "Original : วัดพระแก้วอยู่ที่ไหน ?"},
        {"role" : "assistant", 'content' : "Translated : Where is Wat Phra Kaew ?"},
        {"role" : "user", 'content' : "Original : สยามพารากอนอยู่ที่ไหน ?"},
        {"role" : "assistant", 'content' : "Translated : Where is Siam paragon ?"},
        {"role" : "user", 'content' : "Original : วิธีเดินทางไปสนามบิน"},
        {"role" : "assistant", 'content' : "Translated : How to get to the airport"},
        {"role" : "user", 'content' : "Original : เทคโนโลยีเป็นหัวใจสำคัญสำหรับองค์กร ทั้งภายในองค์กรไม่ว่าจะเป็นเรื่องข้อมูล การทำงานร่วมกัน รวมไปถึงการให้บริการกับลูกค้าในมิติทั้งเรื่องความรวดเร็วและการให้บริการที่มีมาตรฐานเดียวกัน องค์กรหลาย ๆ แห่งจึงต้องเร่งปรับตัวให้กลายเป็นองค์กรยุคใหม่ และก้าวทันโลกมากขึ้น"},
        {"role" : "assistant", 'content' : "Translated : Technology is a vital heart for organizations. It is essential within an organization in terms of information, collaboration, as well as providing services to customers in terms of speed and standardized services. Many organizations must therefore accelerate their transformation into a modern organization and step up to catch up with the world."},
        {"role" : "user", 'content' : "Original : เคยโดนเอาไปทำโฆษณาวีดิโอให้มูลนิธิการกุศล เป็นคลิปเด็กนั่งกินข้าวกันสองคน ทุกวันนี้มีเพจ NGO เวียดนามกับฟิลิปปินส์แชร์เอายอดกันเต็ม รู้สึกอายจังครับ แบบนี้ทำอะไรได้บ้าง"},
        {"role" : "assistant", 'content' : "Translated : I was once used in an advertisement video for a charity foundation. It's a clip of two kids eating together. These days, there are an NGO page from Vietnam and the Philippines sharing it to get high views. I feel so embarrassed. What can I do about this?"},
        {"role" : "user", 'content' : prompt },
    ],
    "model" : 'SeaLLM-7b'
    }
    task = loop.create_task(do_request(FLOAT16_CUSTOM_URL, data))
    tasks.append(task)
loop.run_until_complete(asyncio.gather(*tasks))
print('Asynchronus chain total time : {}'.format(time.time() - start))