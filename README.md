# กรรมตรังไทย (Kramtrangthai)

ระบบแจกเหรียญ Kramcion ตามสมาธิและคำภาวนา  
บนเครือข่าย Bitcoin โดยมีการฝัง metadata และเรียกใช้ RPC เพื่อสร้างธุรกรรมแบบใหม่

## แนวคิด
- สมาธิ = Proof of Stillness
- คำภาวนา = Proof of Purity
- ทุกการกระทำเป็นกรรม → ทุกกรรมแปรเป็นพลังงาน

## โมดูลหลัก
- claim_reward.py → เรียก RPC เพื่อแจกเหรียญ
- meditations/ → เก็บผลสมาธิที่ผ่านการประเมิน
- metadata/ → แม่แบบคำอธิบายกรรมใน metadata

## เริ่มต้น
```bash
git clone https://github.com/[yourname]/kramtrangthai.git
cd kramtrangthai
python scripts/claim_reward.py