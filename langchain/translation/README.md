# Our Example is Based on the Float16.cloud Model 

[Float16.cloud](https://float16.cloud)

## Why? 

Each model comes with a unique architecture, size, compatibility, and database of knowledge, making it necessary to adapt prompts based on the model being used.

## How? 

We employ techniques from prompt engineering to tailor prompts for the model. These techniques include:

- Few-shot learning
- Chain of Thought (CoT)
- Tree of Thought (ToT)
- Reason + Act (ReACT)

## Model

- SeaLLM-7b

For machine translation tasks, few-shot learning needs to be employed. Even though translating the entire content is possible, we often need to translate one paragraph at a time. Nevertheless, we have not yet tested this model's effectiveness with long-form content. 

In certain translation tasks (e.g., Thai-to-English) and specific sentence structures like **question** sentences, **the model attempts to answer the question** rather than simply translating it. This phenomenon occurs with other models like ChatGPT (GPT-3.5). The current solution to prevent this issue involves adding more few-shot examples.

To further enhance the quality of translations, we could potentially utilize the Chain of Thought (CoT) and Tree of Thought (ToT) techniques. However, we have not yet tested these techniques with the SeaLLM-7b model.

### Results 
| Original | Translated | Language |
| --- | --- | --- |
| Original : สำหรับบทความสุดท้ายของแคมเปญนี้ ก็ยังคงเป็นเรื่องราวเกี่ยวกับ Chatbot เช่นเคย แต่จะมีความซับซ้อนยิ่งกว่า วันนี้เราจะมาทำ Chatbot with RAG and Agents เพื่อช่วยให้ Chatbot ของเราสามารถตอบคำถามได้ดียิ่งขึ้นและถูกต้องกว่าเดิม ถ้าพร้อมแล้ว เรามาเริ่มกันเลยค่ะ! | Translated : For the last article of this campaign, we will still be talking about Chatbots, but it will be more complex than before. Today, we will create a Chatbot with RAG and Agents to help our Chatbot answer questions more accurately and correctly than before. Are you ready? Let's start! | Thai-to-English 
Original : สำหรับพาร์ทของ Chat Agent เราก็ได้เลือกใช้ OpenAI มาเป็น LLMs ที่ทำหน้าที่ในส่วนนี้ หน้าที่ของ Chat Agent มี 2 อย่างคือตัดสินใจว่าใช้ข้อมูลจากฝั่งไหนเอามาใช้ตอบคำถาม ซึ่งประกอบด้วย Chat Engine, Sub Question Engine และ RAG Engine | Translated: For the part of Chat Agent, we have chosen to use OpenAI as the LLMs (Language Models) that work in this area. The role of Chat Agent has two parts: making decisions about which data to use from one side to answer questions, which includes the Chat Engine, Sub Question Engine, and RAG Engine. | Thai-to-English
Original : ในปัจจุบันนี้มีการนำ AI มาใช้ในหลายๆอย่าง ซึ่ง Q&A Document ถ้าเราจินตนาการว่าโปรเจ็คเป็นยังไง สิ่งแรกที่เรานึกก็คงนึก OpenAI กัน หรือ บางคนอาจจะนึง Chat Bot เจ้าต่างๆ ที่เราถามคำถามไปเเล้วเจ้า Chat bot ก็จะตอบคำถามกลับมา ซึ่งตัวQ&A Document นี้ เราจะโยนตัว Document ไป ให้ Chat bot ของเราเเล้วหลังจากนั้นเราก็ถาม เจ้า Chat bot ก็จะตอบกลับ | Translated : In today's world, AI is being used in many ways. If we imagine a project, the first thing we might think of is OpenAI or some Chat Bots that we ask questions to and they answer back. The Q&A Document is like throwing the Document to the Chat Bot and then asking the Chat Bot questions. | Thai-to-English

## Bonus
We have include asynchronus translation code example to demonstrate how to use the model in a batching application. The code is available in the `SeaLLM-7b.py`.

It could help speed up the translation process by `2-3 times.` However, the code is not optimized for speed. It is only a proof of concept.

