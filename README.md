# 🎯 Universal Artillery Calculator — Pro Edition

**เวอร์ชันปัจจุบัน: v3.7.13 · รองรับ Arma Reforger 1.8** · [ดู Changelog](CHANGELOG.md)

เครื่องคำนวณการยิงปืนใหญ่และปืนครกสำหรับ **Arma Reforger** ทำงานบนเว็บเบราว์เซอร์ล้วน ไม่ต้องติดตั้งอะไร
คำนวณ Elevation / Azimuth / Time of Flight พร้อมชดเชยลม ความสูง และแสดงผลบนแผนที่จริง

🌐 **ใช้งานออนไลน์:** https://xsign1995.github.io/Universal-Artillery-Calculator-Pro-Edition/

---

## ✨ ความสามารถหลัก

### 🔫 อาวุธและกระสุนที่รองรับ

| อาวุธ | ขนาด | ระบบ MIL | กระสุน |
|---|---|---|---|
| M777A1 Howitzer — US (CIE Artillery) | 155mm | 6400 | M107 HE, M795 HE, M982A1 Excalibur |
| M777 Howitzer — M777 Howitzer Artillery (PandaMods) | 155mm | 6400 | M107 HE, M982 Excalibur (นำวิถี) |
| 2A36 Giatsint-B — Soviet (CIE Artillery) | 152mm | 6000 | 3OF29 "Bekas", 3OF59 "Khrebet" |
| M252 Mortar — US | 81mm | 6400 | M821 HE, M853A1 Illumination, M819 Smoke, M879 Training |
| 2B14 Podnos — Soviet | 82mm | 6000 | O-832DU HE, S-832S Illumination, D-832DU Smoke |

- ปืนครก M252 / 2B14 มี 2 โปรไฟล์ตาราง: **Original (Vanilla)** และ **Adult Mortars (Mod)**
- เลือก Charge / Ring เองได้ หรือใช้ **⚡ Auto Select** ให้โปรแกรมเลือกให้อัตโนมัติ
- จำอาวุธ โปรไฟล์ และกระสุนที่เลือกล่าสุด (ค่าเริ่มต้น: M777 Howitzer Artillery — PandaMods)

### 📐 การคำนวณ
- คำนวณทั้ง **Low Angle** และ **High Angle** พร้อมกัน
- ชดเชย **ความสูงเป้าต่างจากปืน** ทั้ง High และ Low Angle ด้วยแบบจำลองแรงต้านอากาศ (ใช้ความเร็วต้นและค่าแรงต้านของกระสุนที่อ่านจากไฟล์เกม)
- ชดเชย **ลม** (ความเร็ว + ทิศทาง) พร้อมเวลาอัปเดตค่าลมล่าสุด (เขียว < 10 นาที / แดง ≥ 10 นาที)
- **Air Fuze** — คำนวณเวลาตั้งชนวนระเบิดกลางอากาศตามความสูงที่ต้องการ
- **Min Peak Height** — กำหนดความสูงต่ำสุดของวิถีเพื่อให้พ้นสิ่งกีดขวาง
- รองรับพิกัด **Arma Reforger Grid** แบบ 3 / 4 / 5 หลัก (Auto Grid) และแสดงผลเป็น MILs หรือ Degree

### 🗺️ แผนที่และการแสดงผล
- **Tactical Top-Down Map** รองรับ **40 แผนที่** (Everon, Arland, Kolguyev, Chernarus, Takistan ฯลฯ) — 5 แผนที่ (Everon, Arland, Kolguyev, Yunakivka, Novobakhmutivka) เก็บใน repo นี้เองพร้อมป้ายชื่อและข้อมูลความสูง ส่วนที่เหลือใช้ภาพจาก ArmaMapTiles
- ดับเบิลคลิกบนแผนที่เพื่อ **Set Target / Set Gun Position**
- **🏷️ ป้ายชื่อสถานที่และสัญลักษณ์** บนแผนที่ 5 แผนที่ข้างต้น ซ่อน/แสดงได้ด้วยช่องติ๊ก Labels
- **⛰️ Auto Z** — ดึงค่าความสูงจากตำแหน่งบนแผนที่ให้อัตโนมัติ (5 แผนที่ข้างต้น)
- **จุดมาร์คแผนที่** (คลิกขวา 2 ครั้ง) ตั้งชื่อ แก้ไข ลบได้ บันทึกแยกตามแผนที่
- รองรับมือถือ / iPad: **แตะค้าง (Long-press)** แทนดับเบิลคลิก/คลิกขวา
- **Trajectory Profile 2D** — แสดงพื้นดินจริงตามแนวปืนไปเป้า เตือนเมื่อวิถีชนเนิน, ป้าย Low / High พร้อม ToF ความสูงสูงสุด มุมตก, จุด Air Fuze, ซูมด้วยล้อเมาส์ / ลากเลื่อน / ดับเบิลคลิกรีเซ็ต และเลื่อนเมาส์ดูค่าที่จุดใดก็ได้
- **มุมมอง 3D** — จำลองแรงต้านอากาศให้ตรงกับตารางยิงในเกม มีอนิเมชันกระสุนบิน และเส้นวิถีโค้งตามแรงลม
- **3D พื้นนูนตามความสูงจริง** บนแผนที่ที่มีข้อมูลความสูง (5 แผนที่ข้างต้น)

### 🧰 เครื่องมือภาคสนาม
- **🔭 FO Spotter** — รับระยะ/ทิศจากผู้ตรวจการณ์ หาจุดตกจริง แล้ว **ปรับชดเชย** อัตโนมัติ
- **ปรับเป้า (D-Pad)** ขยับจุดเล็งทีละ 5m / 10m ทั้ง 8 ทิศ
- **ปืนหลายกระบอก (สูงสุด 5)** — ยิงจุดเดียวกัน หรือ **ยิงแบบหน้ากระดาน (Sheaf)** ตามแกน X/Y และระยะห่างที่กำหนด
- **📡 Counter-Battery** — ใส่จุดที่เรดาร์ตรวจจับได้สูงสุด 6 จุด เพื่อประเมินพื้นที่ตั้งปืนข้าศึก
- **📢 Copy to Chat** — คัดลอกคำสั่งยิงแบบบรรทัดเดียว (Chat Team / Chat Gunner แยกต่อกระบอก) ไปวางในแชทเกม
- **💾 Target Memory** — บันทึกและตั้งชื่อเป้าหมาย
- **📜 Fire History** — บันทึกทุกการยิงอัตโนมัติ (สูงสุด 50 รายการ) โหลดกลับมาใช้ได้ และกู้พิกัดล่าสุดเมื่อเปิดหน้าเว็บใหม่

---

## 🚀 วิธีใช้งาน

**ออนไลน์:** เปิดลิงก์ GitHub Pages ด้านบน

**ออฟไลน์:** ดาวน์โหลด `index.html`, `ballistic_data.js` และโฟลเดอร์ `maps/` ไว้ในโฟลเดอร์เดียวกัน แล้วดับเบิลคลิกเปิด `index.html`
(การคำนวณใช้งานได้แบบออฟไลน์ ส่วนภาพแผนที่ (ยกเว้นแผนที่ใน `maps/`) และ 3D ต้องต่ออินเทอร์เน็ต · Auto Z และพื้น 3D ของแผนที่ใน `maps/` เมื่อเปิดจากไฟล์ในเครื่องจะดึงข้อมูลความสูงจากเว็บ จึงต้องต่อเน็ตด้วย)

1. เลือกอาวุธ กระสุน และ Charge (หรือ Auto Select)
2. ใส่พิกัดปืนและเป้าหมาย (X / Y / Z) หรือดับเบิลคลิกบนแผนที่
3. ใส่ความเร็วและทิศทางลม
4. กด **Calculate** แล้วตั้งค่าในเกมตาม Elevation / Azimuth ที่ได้

---

## 📝 Changelog

ดูประวัติการเปลี่ยนแปลงทุกเวอร์ชันได้ที่ **[CHANGELOG.md](CHANGELOG.md)**

---

## 🙏 Credits

- ภาพแผนที่: [ArmaMapTiles](https://armamaptiles.github.io/) · แผนที่ Everon, Arland, Kolguyev (แผนที่เริ่มต้นของเกม) ทำด้วย Enfusion Map Maker
- แผนที่ Novobakhmutivka: ผู้สร้าง xJESUSx
- แผนที่ Yunakivka: ผู้สร้าง Rumor / SPEARHEAD
- ข้อมูลอาวุธและกระสุนทั้งหมดมาจากเกมและม็อดต่อไปนี้ — ขอบคุณผู้สร้างทุกท่าน (ตารางยิงดึงจากไฟล์ด้วยโปรแกรม [Enfusion Ballistics Extractor](https://github.com/Xsign1995/Enfusion-Ballistics-Extractor)):
  - **Arma Reforger** (Bohemia Interactive) — 2B14, M252 (โปรไฟล์ Original)
  - **M777 Howitzer Artillery** โดย **PandaMods** (APL-SA) — M777 Howitzer: M107 HE และ M982 Excalibur
  - **CIE Artillery** โดย **Ligthman** — M777A1, 2A36 Giatsint-B
  - **Adult Mortars** โดย **odkupiciel375** — โปรไฟล์ Adult Mortars ของ M252 / 2B14
  - **Tactical Flava** โดย **KERNOV** — 2B9 Vasilek
  - **OSP-BM21** โดย **Dazoc** — BM-21 Grad

> โปรเจกต์นี้เป็นเครื่องมือที่แฟนเกมทำขึ้นเอง ไม่มีส่วนเกี่ยวข้องกับ Bohemia Interactive
