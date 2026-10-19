# 🎯 Universal Artillery Calculator — Pro Edition

**เวอร์ชันปัจจุบัน: v3.2.4 · รองรับ Arma Reforger 1.8** · [ดู Changelog](CHANGELOG.md)

เครื่องคำนวณการยิงปืนใหญ่และปืนครกสำหรับ **Arma Reforger** ทำงานบนเว็บเบราว์เซอร์ล้วน ไม่ต้องติดตั้งอะไร
คำนวณ Elevation / Azimuth / Time of Flight พร้อมชดเชยลม ความสูง และแสดงผลบนแผนที่จริง

🌐 **ใช้งานออนไลน์:** https://xsign1995.github.io/Universal-Artillery-Calculator-Pro-Edition/

---

## ✨ ความสามารถหลัก

### 🔫 อาวุธและกระสุนที่รองรับ

| อาวุธ | ขนาด | ระบบ MIL | กระสุน |
|---|---|---|---|
| M777 Howitzer — US (PandaMods) | 155mm | 6400 | M107 HE |
| M777A1 Howitzer — US (CIE Artillery) | 155mm | 6400 | M107 HE, M795 HE |
| 2A36 Giatsint-B — Soviet (CIE Artillery) | 152mm | 6400 | 30F59 "Khrebet", 30F29 "Bekas" |
| M252 Mortar — US | 81mm | 6400 | M821 HE, M853A1 Illumination, M819 Smoke |
| 2B14 Podnos — Soviet | 82mm | 6000 | O-832DU HE, S-832S Illumination, D-832DU Smoke |
| 2B9 Vasilek Automatic Mortar — Soviet | 82mm | 6000 | O-832DU HE, D-832DU Smoke |

- ปืนครก M252 / 2B14 มี 2 โปรไฟล์ตาราง: **Original (Vanilla)** และ **Adult Mortars (Mod)**
- เลือก Charge / Ring เองได้ หรือใช้ **⚡ Auto Select** ให้โปรแกรมเลือกให้อัตโนมัติ

### 📐 การคำนวณ
- คำนวณทั้ง **Low Angle** และ **High Angle** พร้อมกัน
- ชดเชย **ลม** (ความเร็ว + ทิศทาง) พร้อมเวลาอัปเดตค่าลมล่าสุด (เขียว < 10 นาที / แดง ≥ 10 นาที)
- **Air Fuze** — คำนวณเวลาตั้งชนวนระเบิดกลางอากาศตามความสูงที่ต้องการ
- **Min Peak Height** — กำหนดความสูงต่ำสุดของวิถีเพื่อให้พ้นสิ่งกีดขวาง
- รองรับพิกัด **Arma Reforger Grid** แบบ 3 / 4 / 5 หลัก (Auto Grid) และแสดงผลเป็น MILs หรือ Degree

### 🗺️ แผนที่และการแสดงผล
- **Tactical Top-Down Map** ใช้ภาพแผนที่จริงจาก ArmaMapTiles รองรับ **36 แผนที่** (Everon, Arland, Kolguyev, Chernarus, Takistan ฯลฯ)
- ดับเบิลคลิกบนแผนที่เพื่อ **Set Target / Set Gun Position**
- **จุดมาร์คแผนที่** (คลิกขวา 2 ครั้ง) ตั้งชื่อ แก้ไข ลบได้ บันทึกแยกตามแผนที่
- รองรับมือถือ / iPad: **แตะค้าง (Long-press)** แทนดับเบิลคลิก/คลิกขวา
- กราฟวิถีกระสุน 2D และ **มุมมอง 3D** (จำลองแรงต้านอากาศให้ตรงกับตารางยิงในเกม)

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

**ออฟไลน์:** ดาวน์โหลด `index.html` และ `ballistic_data.js` ไว้ในโฟลเดอร์เดียวกัน แล้วดับเบิลคลิกเปิด `index.html`
(การคำนวณใช้งานได้แบบออฟไลน์ ส่วนภาพแผนที่และ 3D ต้องต่ออินเทอร์เน็ต)

1. เลือกอาวุธ กระสุน และ Charge (หรือ Auto Select)
2. ใส่พิกัดปืนและเป้าหมาย (X / Y / Z) หรือดับเบิลคลิกบนแผนที่
3. ใส่ความเร็วและทิศทางลม
4. กด **Calculate** แล้วตั้งค่าในเกมตาม Elevation / Azimuth ที่ได้

---

## 📝 Changelog

ดูประวัติการเปลี่ยนแปลงทุกเวอร์ชันได้ที่ **[CHANGELOG.md](CHANGELOG.md)**

---

## 🙏 Credits

- ภาพแผนที่: [ArmaMapTiles](https://armamaptiles.github.io/)
- ตารางยิง: ถอดจากตำรา (Firing Table) ในเกม Arma Reforger และม็อด PandaMods, CIE Artillery, Adult Mortars

> โปรเจกต์นี้เป็นเครื่องมือที่แฟนเกมทำขึ้นเอง ไม่มีส่วนเกี่ยวข้องกับ Bohemia Interactive
