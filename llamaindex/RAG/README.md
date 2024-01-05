# Our Example Based on the Float16.cloud Model 

[Float16.cloud](https://float16.cloud)

## Why? 

Every model has its unique architecture, size, compatibility, and knowledge set, which necessitates prompt adaptation to the model in use.

## How? 

We utilize techniques from prompt engineering to customize the prompts for the model. These include:

- Few-shot learning
- Chain of Thought (CoT)
- Tree of Thought (ToT)
- Reason + Act (ReACT)

## Model

- SeaLLM-7b

For summarizing tasks, we could use zero-shot learning. Despite being able to summarize the entire content, it's often necessary to summarize one paragraph at a time, particularly if the text's length exceeds 1,000 tokens. However, the effectiveness of this model with long-form content has not yet been tested. 

Comparative tests on Thai language content were performed between SeaLLM-7b and GPT-4 (Thai). From the results, it was inferred that SeaLLM-7b could summarize Thai language content as effectively as the GPT-4 (Thai) model.

### Results 
| Content | Summary | Language |
| --- | --- | --- |
รอคอยมานานกว่า 10 ปี ในที่สุดก็ได้ฤกษ์ดีเข้าพิธีวิวาห์ เริ่มต้นชีวิตคู่ในฐานะสามีภรรยา อย่างเป็นทางการ สำหรับ โก๊ะตี๋ อารามบอย และ น้องกวาง สุภัค  โดยล่าสุด! พี่ชายคนสนิท จตุรงค์ โพธาราม หรือ จตุรงค์ มกจ๊ก ได้แชร์คลิปวิดีโอที่เผยให้เห็นภาพพิธีมงคลสมรสในช่วงเช้า พร้อมระบุแคปชั่น "แต่งจารโก๊ะ+กวาง @kootee" ผ่านอินสตาแกรม @jaturong_p ซึ่งเป็นโมเมนต์ขณะคู่บ่าวสาว ญาติผู้ใหญ่ รวมถึงแขกคนสนิท กำลังร่วมกันทำบุญเลี้ยงพระ ท่ามกลางบรรยากาศอันเรียบง่ายและเป็นส่วนตัว  นอกจากนั้นแล้ว ในช่วงเย็นวันนี้ (17 ธันวาคม) โก๊ะตี๋ และ น้องกวาง จะจัดแถลงข่าวเปิดใจถึงเส้นทางความหวาน และแพลนครอบครัวในอนาคตกับสื่อมวลชน ณ ห้อง Basilica โพธาลัย เลเซอร์ ปาร์ค  ซึ่งทีมข่าวบันเทิง Sanook ต้องขอแสดงความยินดีกับทั้งคู่ไว้ด้วยนะคะ | โก๊ะตี๋ และ น้องกวาง จัดพิธีวิวาห์ในฐานะสามีภรรยาอย่างเป็นทางการ หลังรอคอยมานานกว่า 10 ปี จตุรงค์ โพธาราม แชร์คลิปวิดีโอในช่วงเช้า ระหว่างพิธีมงคลสมรส และในช่วงเย็นวันนี้จะแถลงข่าวเปิดใจถึงเส้นทางความหวาน และแพลนครอบครัวในอนาคตกับสื่อมวลชน. | Thai
ส่งคัมแบ็กด้วยมินิอัลบั้มใหม่ในรอบกว่า 1 ปี 9 เดือนกับ แทยอน ศิลปินสาวเสียงทรงพลัง เมนโวคอลจากเกิร์ลกรุ๊ปแห่งชาติ Girls’ Generation ด้วยซิงเกิลไตเติลในชื่อ To. X พร้อมปล่อยมิวสิกวิดีโอออกมาให้รับชมพร้อมกันในวันที่ 27 พฤศจิกายนที่ผ่านมา      To. X เป็นเพลงแนว R&B ผสมผสานการริฟฟ์กีตาร์และทำนองที่เป็นจังหวะ ร่วมด้วยเสียงร้องอันเป็นเอกลักษณ์ของแทยอน ที่ทำให้ผู้ฟังสามารถเข้าถึงห้วงอารมณ์และความหมายของบทเพลงผ่านน้ำเสียงของเธอได้เป็นอย่างดี ซึ่งเพลงนี้เป็นการเล่าเรื่องราวของความรักที่กำลังถูกอีกฝ่ายควบคุมจนเสียความเป็นตัวเองไป นำมาสู่จุดสิ้นสุดของความสัมพันธ์     ด้านมิวสิกวิดีโอของเพลงนี้ นำเสนอการเปลี่ยนแปลงทางอารมณ์ในความรักที่ไร้เหตุผลของคนรักที่พยายามตัดขาดจากตัวเองและโลก โดยแทยอนยังรับบทบาทแสดงนำในมิวสิกวิดีโอนี้ด้วยตัวเอง | แทยอน ศิลปินสาวเสียงทรงพลัง จากเกิร์ลกรุ๊ป Girls' Generation เปิดตัวมินิอัลบั้มใหม่ To. X พร้อมปล่อยมิวสิกวิดีโอออกมาให้รับชมพร้อมกันในวันที่ 27 พฤศจิกายนที่ผ่านมา ภายในอัลบั้มนี้มีเพลงแนว R&B ผสมผสานการริฟฟฟ์กีตาร์และทำนองที่เป็นจังหวะ ร่วมด้วยเสียงร้องอันเป็นเอกลักษณ์ของแทยอน ที่ทำให้ผู้ฟังสามารถเข้าถึงห้วงอารมณ์และความหมายของบทเพลงผ่านน้ำเสียงของเธอได้เป็นอย่างดี. | Thai

