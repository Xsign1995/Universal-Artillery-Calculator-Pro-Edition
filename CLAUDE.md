# CLAUDE.md — บันทึกโปรเจกต์ (อ่านก่อนเริ่มงานทุกครั้ง)

เว็บเครื่องคำนวณปืนใหญ่ / ปืนครกสำหรับ **Arma Reforger** — Universal Artillery Calculator Pro Edition
- เว็บ: https://xsign1995.github.io/Universal-Artillery-Calculator-Pro-Edition/ (GitHub Pages, deploy ด้วย `.github/workflows/static.yml`)
- Repo: `Xsign1995/Universal-Artillery-Calculator-Pro-Edition` (public) · branch `main`
- เวอร์ชันล่าสุด: **v3.5.1** (ดู `CHANGELOG.md`)
- โปรเจกต์เกี่ยวข้อง: `Xsign1995/Enfusion-2D-Map-Maker` (ทำแผนที่ / tiles / heightmap / labels.json ให้เว็บนี้), `Xsign1995/Enfusion-Ballistics-Extractor` (ดึงตารางยิงจากไฟล์เกม / mod)

## กติกาการทำงานกับผู้ใช้ (Xsign1995)
- ตอบเป็น **ภาษาไทย** (ศัพท์เทคนิคใช้อังกฤษได้)
- ผู้ใช้ชอบให้ทำงานจนจบ ส่งไฟล์ที่ใช้ได้ทั้งไฟล์ ไม่ใช่ snippet · ผู้ใช้แก้ CSS / โค้ดเล็กน้อยเองแล้วส่งไฟล์กลับมา — ทำงานต่อจากไฟล์ที่ผู้ใช้ส่ง
- ไฟล์ที่ผู้ใช้อัปโหลด: `cp` มาใช้ ไม่เขียนไฟล์ใหญ่ใหม่ทั้งไฟล์
- **ถามก่อน commit / push ทุกครั้ง** · ส่งไฟล์ให้ผู้ใช้ลองก่อน แล้วค่อย push เมื่อผู้ใช้สั่ง
- **ผู้ใช้เปิดเว็บผ่าน `file://`** (ไม่ใช่ web server) — ห้ามใส่ `defer` ที่ `<script>` (โดยเฉพาะ `ballistic_data.js`), `fetch()` ไฟล์ในเครื่องไม่ได้, canvas ที่วาดภาพจากไฟล์ในเครื่องจะติด taint
- เลขเวอร์ชัน Claude เป็นคนตั้ง + อัปเดต README / CHANGELOG เอง (ผู้ใช้ไม่ทำเอง)
  - `vX.Y.Z`: X = เขียน UI ใหม่ทั้งหมด · Y = ฟีเจอร์ / อาวุธใหม่ / รองรับเกมเวอร์ชันใหม่ · Z = แก้บั๊ก / ปรับตาราง / เพิ่มแผนที่
  - Changelog อยู่ใน `CHANGELOG.md` (README แค่ลิงก์ไป + บรรทัดเวอร์ชันปัจจุบัน) — ห้ามใส่รายละเอียดโค้ด / สูตรภายในใน changelog
  - ถ้าย้อนโค้ดกลับจนเหมือนเวอร์ชันเดิม ไม่ต้องเพิ่มเวอร์ชันใหม่
- Commit message: เวอร์ชัน + เรื่องหลักสั้นๆ เช่น `v3.2.5 — Low Angle height correction`
- คอมเมนต์ในโค้ด: สั้น เฉพาะสาระ ไม่เล่าประวัติการแก้ ไม่ใส่ผลทดสอบ (เก็บคอมเมนต์ที่เตือนจุดสำคัญไว้)
- โปรแกรม Python ที่ทำให้ผู้ใช้ ต้องรันบน Python ปัจจุบัน (3.15) · ไฟล์ .exe ต้องมีเลขเวอร์ชันในชื่อ เช่น `AppName_v0.2.1.exe`

## โครงสร้าง
| ไฟล์ | หน้าที่ |
|---|---|
| `index.html` | ทั้งแอป (HTML + CSS + JS) — คำนวณ, แผนที่ 2D, กราฟวิถี 2D / 3D (Three.js 0.165 จาก jsDelivr ผ่าน importmap) |
| `ballistic_data.js` | ตารางยิงทุกอาวุธ / กระสุน / charge — แถว `[RANG, ELEV, ToF, D ELEV/100m DR, D ToF/100m DR, Peak Alt, Angle of Impact, Cross Wind 10m/s, Long Wind 10m/s]` |
| `maps/<Map>/` | tiles Zoomify ของแผนที่ที่เก็บใน repo เอง (Yunakivka, Novobakhmutivka) |
| `maps/<map>_height.js` | heightmap ฝังเป็น PNG data URL (R = ไบต์สูง, G = ไบต์ต่ำ, เมตร = ค่า × scale + offset) → `window.LOCAL_HEIGHTMAPS` |
| `maps/<map>_labels.js` | ป้ายชื่อ / จุด / สัญลักษณ์จาก labels.json ของ Map Maker → `window.LOCAL_MAP_LABELS` |

ส่วนสำคัญใน `index.html`:
- `DOM` (Proxy cache ของ element), `ArtilleryPhysics` (IIFE ฟิสิกส์ล้วน ใช้ทั้ง `calculate()` และ `calculateFOCorrection()`)
- `calculate()` → `collectGunPositions()` → `computeSheafTargets()` → `computeSolutionForGun()` ต่อกระบอก
- `MapBackground` (tiles): `ALLOWED_MAPS` ต้องตรงกับ `<option>` ใน `#mapBgSelect` เสมอ · `LOCAL_TILE_MAPS` = แผนที่ใน `maps/` (มี `v` = เวอร์ชัน tile)
- `MapLabels`, `HeightMap` (Auto Z), `buildTerrain3D()` (พื้น 3D นูน), `loadScriptOnce()`
- `parseArmaGridValue()`: 3 หลัก = ช่อง 100 m (+50), 4 หลัก = 10 m (+5), 5 หลัก = 1 m, มีทศนิยม = ไม่บวกกลางช่อง · `snapTo10mGrid()`
- localStorage: `m777_selected_map`, `m777_map_markers` (แยกตามแผนที่), `m777_memory`, `m777_auto_z`, `m777_map_labels` ฯลฯ — ห่อ try/catch

## แผนที่
- แผนที่ส่วนใหญ่ (37 แผนที่รวมทั้งหมด) ดึง tiles จาก `https://armamaptiles.github.io/ArmaMapsTiles/<Map>/` (repo คนอื่น — เขียนไม่ได้)
- Yunakivka, Novobakhmutivka เก็บใน `maps/` (ทำจาก Enfusion Map Maker ของผู้ใช้)
  - เปิดผ่าน `file://`: โหลด tile จาก GitHub Pages ของ repo นี้ก่อน (`ONLINE_BASE`, มี CORS → 3D ใช้เป็น texture ได้) ไม่มีเน็ตค่อยใช้ไฟล์ในเครื่อง (2D ได้, 3D เป็นสีตามความสูง)
  - **อัปเดต tiles / height / labels ของแผนที่ใน `maps/` ต้องเปลี่ยนเลข `v` ใน `LOCAL_TILE_MAPS` และ `?v=` ใน SCRIPTS ของ `MapLabels` / `HeightMap`** ไม่งั้นเบราว์เซอร์ใช้ไฟล์เก่าใน cache ปนกับของใหม่ (เคยเกิดกับ Yunakivka)
- เพิ่มแผนที่ใหม่ใน `maps/`: copy โฟลเดอร์ tiles (ลบ labels.json ออก) → เพิ่มใน `LOCAL_TILE_MAPS` (+ width/height จาก ImageProperties.xml) → `ALLOWED_MAPS` + `<option>`
- heightmap จาก Map Maker (`<Map>_height.png` 16 บิต + `.json`: cell_m, scale, offset, origin_m) → แปลงเป็น `maps/<map>_height.js` (PNG RGB: R = value>>8, G = value&255, ฝัง base64) แล้วเพิ่มใน `HeightMap` SCRIPTS · ตรวจตำแหน่งให้ตรงภาพแผนที่ก่อน (origin บาง mod ไม่ใช่ 0 เช่น Yunakivka x −28.7 m)
- labels.json → `maps/<map>_labels.js` (เก็บ style, names, points, symbols — ไม่เอา px/py) · ตัวอักษรไอคอนแบบ letter อยู่ในตาราง `LETTERS` (ตรงกับ `SYMBOL_ICONS` ใน Map Maker) · ป้าย "made by xJESUSx" ของ Novobakhmutivka ผู้ใช้ให้ลบออก (บังมุม)
- เครดิต: Novobakhmutivka — xJESUSx · Yunakivka — Rumor / SPEARHEAD
- Map Maker v1.46 ลดระดับแม่น้ำ / คลองใน heightmap ได้ (ผู้ใช้พบว่าผิวน้ำในเกมต่ำกว่าตลิ่ง) — heightmap ใน repo ตอนนี้ยังเป็นชุดก่อนลดระดับ รอผู้ใช้ export ใหม่

## สูตรคำนวณที่ยืนยันแล้ว (ห้ามคิดใหม่จากศูนย์ — ผ่านการยิงทดสอบในเกมหลายรอบ)
- Low Angle มุมเงย: ชดเชยความสูงด้วยแบบจำลองแรงต้านอากาศ (v3.2.5) — **ไม่ใช้** dElevPer100m (ยิงจริงตกสั้น ~100 / ~300 m) · เคยลองย้อนเป็นสูตร trig atan(dz/range) แล้วกลับมาใช้แบบจำลองแรงต้าน หลังยิงเป็นกลุ่มแล้วกลุ่มกระสุนอยู่รอบเป้า (ยิงนัดเดียวหลอกได้เพราะ range dispersion)
- High Angle มุมเงย: ใช้ D ELEV จากตาราง (ทิศ SUBTRACT, กลับกับแบบเดิมของ Low) — เทียบโปรแกรมของเพื่อนได้ 1185.1 vs 1185 · ToF = `(baseTof + sqrt(baseTof² − 8·dz/g)) / 2` (ตรงกับ armacalc.pages.dev) — ToF แสดงทศนิยม 1 ตำแหน่ง คลาด 0.1 s กระสุนอาจถึงพื้นก่อนชนวนทำงาน
- คอลัมน์ "D ELEV / D ToF PER 100M DR" = ต่อความต่างความสูงเป้า 100 m (DR = difference) ไม่ใช่ระยะ
- กราฟวิถี 2D / 3D, Alt @100m, จุด Air Fuze บนแผนที่ ใช้แบบจำลองแรงต้านอากาศ (v3.2.4 — แทน Bézier เดิม) · Air Fuze Timer ใช้สูตรเดิมที่ยืนยันในเกมแล้ว
- Air Fuze: `effectiveDz` (dz + airburstH) ใช้ **เฉพาะ** หาจุดตัดชนวนใน `getDragSimulatedPoints` ห้ามใช้กับ Elevation / ToF / PeakAlt (ใช้ dz จริง) · ผู้ใช้เลื่อนจุดเล็งให้ Air Fuze Point บนแผนที่ทับเป้าจริง (ไม่งั้นระเบิดก่อนถึงเป้า)
- ยังไม่ได้ยืนยันซ้ำ: เคส High Angle ~8000 m, dz < 0 (เคยแค่ "ตกใกล้" กับสูตรเก่า)

## ข้อมูลอาวุธ / ตาราง
- อาวุธ: M777 (PandaMods: M107, M982 Excalibur — ยิงผ่าน FDC Tablet), M777A1 (M107, M795), 2A36 Giatsint-B (30F59, 30F29), M252 81mm (Vanilla / Adult Mortars), 2B14 Podnos 82mm (Vanilla / Adult Mortars), 2B9 Vasilek 82mm
- 2B9 Vasilek ลงทะเบียนเป็น `type: "howitzer"` (ไม่ใช่ "mortar") เพื่อให้มี Low Angle — โค้ดข้าม Low Angle ถ้าเป็น mortar (`!isMortar && lowAngle`) · ระบบ 6000 mil, ค่าลมเท่า 2B14 · O-832DU HE (High 2500–3900 m, Low 100–3900 m), D-832DU Smoke (Low อย่างเดียว 100–2800 m)
- ตาราง CIE บาง charge mod ทำไม่เสร็จ มีแถวเดียว (เช่น M777A1 M107 High c5) — ปกติ ไม่ใช่บั๊ก
- แผน: เปลี่ยนให้อ่าน `ballistic_data.js` แบบไฟล์เดียวรูปแบบใหม่ (`WEAPONS` + `BALLISTIC_TABLES`) ที่ Enfusion Ballistics Extractor สร้าง โดยตรง — ไม่ทำชั้นแปลงให้เข้ากับ `weaponLibrary` เดิม · เทียบตารางให้ใช้ `ballistic_data.js` จาก GitHub ของ repo นี้ก่อน (ตัวที่ใช้งานจริง)

## ฟีเจอร์หลัก (ย่อ)
- ปืนหลายกระบอก (สูงสุด 5), รูปแบบยิงจุดเดียว / หน้ากระดาน (sheaf), ปุ่ม Copy to Chat แยกต่อกระบอก (แชทในเกมไม่รับข้อความยาว / ขึ้นบรรทัด)
- แผนที่ 2D: ทุกกระบอกบนแผนที่, จุดมาร์ค (คลิกขวา 2 ครั้ง / กดค้างบนมือถือ), ป้ายชื่อ (ช่องติ๊ก Labels), ⛰️ Auto Z (เติม Z เมื่อใส่ X/Y, เลือกจุดบนแผนที่, ดึงเป้าจาก FO — ไม่เขียนทับค่า Z จาก Fire History / Target Memory)
- 3D: พื้นนูนตามความสูงจริงสเกล 1:1 กับวิถี (เฉพาะแผนที่ที่มี heightmap) — เส้นกริดพาดตามพื้น
- Fire History (บันทึกทุกครั้งที่คำนวณ), Target Memory, FO Spotter, 📡 Counter-Battery, Range Offset, Air Fuze, Min Peak Height, ลม (เวลาอัปเดตรีเซ็ตเฉพาะตอนกด Calculate)
- มือถือ / iPad: กดค้าง 500 ms = เมนู, layout แก้ด้วย `min-width: 0` ที่ grid children (หน้ากว้างเกินจอประมาณ 15 px ที่ 390 px มีอยู่เดิม)
- สีหลัก: navy `#0f172a`, เขียว `#22c55e`, ฟ้า `#38bdf8`, เหลือง `#eab308`

## เรื่องที่คุยไว้ (ยังไม่ทำ)
- ซ่อนสูตร: ต้องย้าย `calculate()` + `calculateFOCorrection()` + `ballistic_data.js` ไปด้วยกัน · ตัดสินใจทาง **Firebase (Cloud Functions + Hosting)** (wasm ไม่คุ้ม, minify กันได้แค่คนทั่วไป) — ต้องใช้ Blaze plan (ยังอยู่ในโควตาฟรีที่ขนาดงานนี้, ควรตั้ง budget alert) · ข้อเสีย: คำนวณต้องต่อเน็ตตลอด, latency + cold start
- โปรแกรม OCR อ่านภาพตารางยิงในเกม → ข้อความรูปแบบแถวของ `ballistic_data.js` ให้ผู้ใช้ตรวจ (ห้ามแก้ไฟล์ตรง) เป็นโปรแกรม Windows มี GUI
