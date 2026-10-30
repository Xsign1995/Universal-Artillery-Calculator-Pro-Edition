# CLAUDE.md — บันทึกโปรเจกต์ (อ่านก่อนเริ่มงานทุกครั้ง)

เว็บเครื่องคำนวณปืนใหญ่ / ปืนครกสำหรับ **Arma Reforger** — Universal Artillery Calculator Pro Edition
- เว็บ: https://xsign1995.github.io/Universal-Artillery-Calculator-Pro-Edition/ (GitHub Pages, deploy ด้วย `.github/workflows/static.yml`)
- Repo: `Xsign1995/Universal-Artillery-Calculator-Pro-Edition` (public) · branch `main`
- เวอร์ชันล่าสุด: **v3.6.5** (ดู `CHANGELOG.md`)
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
| `ballistic_data.js` | ไฟล์เดียว format 2 จาก Enfusion Ballistics Extractor: `WEAPONS` (รายการปืน / profile / กระสุน → key ตาราง, ผู้ใช้แก้เองได้) + `BALLISTIC_TABLES` (ระหว่าง `EBX-TABLES-BEGIN/END`; ต่อกระสุน: `gun` (milSystem, limits), `ammo` (v0, airDrag, mass), `charges` (v0 ต่อ charge), `wind` (ค่าสำรอง), `highAngle` / `lowAngle` → แถว `[RANGE, ELEV, TOF, dELEV, dTOF, PEAK, FALL, XWIND, LWIND]`) — **ห้ามแก้ตารางตรง** (Extractor เขียนทับ) · `index.html` สร้าง `weaponLibrary` จาก WEAPONS ตอนโหลด และเติม `<select id="weaponSelect">` เอง |
| `maps/<Map>/` | tiles Zoomify ของแผนที่ที่เก็บใน repo เอง (Yunakivka, Novobakhmutivka, Arland, Everon, Kolguyev) · ชุดใหม่มี `<Map>_height.png` (16 บิต) + `.json` อยู่ในโฟลเดอร์เดียวกัน |
| `maps/<map>_labels.js` | ป้ายชื่อ / จุด / สัญลักษณ์จาก labels.json ของ Map Maker → `window.LOCAL_MAP_LABELS` |

ส่วนสำคัญใน `index.html`:
- `DOM` (Proxy cache ของ element), `ArtilleryPhysics` (IIFE ฟิสิกส์ล้วน ใช้ทั้ง `calculate()` และ `calculateFOCorrection()`)
- `calculate()` → `collectGunPositions()` → `computeSheafTargets()` → `computeSolutionForGun()` ต่อกระบอก
- `MapBackground` (tiles): `ALLOWED_MAPS` ต้องตรงกับ `<option>` ใน `#mapBgSelect` เสมอ · `LOCAL_TILE_MAPS` = แผนที่ใน `maps/` (มี `v` = เวอร์ชัน tile)
- `MapLabels`, `HeightMap` (Auto Z), `buildTerrain3D()` (พื้น 3D นูน), `loadScriptOnce()`
- `parseArmaGridValue()`: 3 หลัก = ช่อง 100 m (+50), 4 หลัก = 10 m (+5), 5 หลัก = 1 m, มีทศนิยม = ไม่บวกกลางช่อง · `snapTo10mGrid()`
- localStorage: `m777_selected_map`, `m777_selected_weapon` (อาวุธ / profile / กระสุนล่าสุด — `restoreWeaponSelection()` ตอนโหลด; อาวุธเริ่มต้น = `m777_howitzer` ของ PandaMods), `m777_map_markers` (แยกตามแผนที่), `m777_memory`, `m777_auto_z`, `m777_map_labels` ฯลฯ — ห่อ try/catch

## แผนที่
- แผนที่ส่วนใหญ่ (37 แผนที่รวมทั้งหมด) ดึง tiles จาก `https://armamaptiles.github.io/ArmaMapsTiles/<Map>/` (repo คนอื่น — เขียนไม่ได้)
- Yunakivka, Novobakhmutivka, Arland, Everon, Kolguyev เก็บใน `maps/` (ทำจาก Enfusion Map Maker ของผู้ใช้; 3 แผนที่หลังเป็นแผนที่เริ่มต้นของเกม — เพิ่ม v3.6.1, heightmap แบบ `FILES`)
  - เปิดผ่าน `file://`: โหลด tile จาก GitHub Pages ของ repo นี้ก่อน (`ONLINE_BASE`, มี CORS → 3D ใช้เป็น texture ได้) ไม่มีเน็ตค่อยใช้ไฟล์ในเครื่อง (2D ได้, 3D เป็นสีตามความสูง)
  - **อัปเดต tiles / height / labels ของแผนที่ใน `maps/` ต้องเปลี่ยนเลข `v` ใน `LOCAL_TILE_MAPS` และ `?v=` ใน SCRIPTS ของ `MapLabels` / `HeightMap`** ไม่งั้นเบราว์เซอร์ใช้ไฟล์เก่าใน cache ปนกับของใหม่ (เคยเกิดกับ Yunakivka)
- เพิ่มแผนที่ใหม่ใน `maps/`: copy โฟลเดอร์ tiles (ลบ labels.json ออก) → เพิ่มใน `LOCAL_TILE_MAPS` (+ width/height จาก ImageProperties.xml) → `ALLOWED_MAPS` + `<option>`
- heightmap (ทุกแผนที่ใน `maps/`, v3.6.1): copy `<Map>_height.png` (16 บิต) + `.json` (cell_m, scale, offset, origin_m) ไว้ใน `maps/<Map>/` แล้วเพิ่มใน `FILES` ของ `HeightMap` (path + `v`) — `index.html` อ่านด้วย `fetch` + ถอด PNG 16 บิตเอง (`decodePng16`, `DecompressionStream`) · เปิดผ่าน `file://` ใช้สำเนาบน GitHub Pages (`SITE_BASE`) จึงต้องต่อเน็ต ไม่มีเน็ต = ไม่มี Auto Z / พื้น 3D · อัปเดตไฟล์ความสูงต้องเปลี่ยน `v` ใน `FILES` · ตรวจ origin ให้ตรงภาพแผนที่ (บาง mod ไม่ใช่ 0 เช่น Yunakivka x −28.7 m)
- labels.json → `maps/<map>_labels.js` (เก็บ style, names, points, symbols — ไม่เอา px/py) · ตัวอักษรไอคอนแบบ letter อยู่ในตาราง `LETTERS` (ตรงกับ `SYMBOL_ICONS` ใน Map Maker) · ป้าย "made by xJESUSx" ของ Novobakhmutivka ผู้ใช้ให้ลบออก (บังมุม)
- เครดิต: Novobakhmutivka — xJESUSx · Yunakivka — Rumor / SPEARHEAD
- Map Maker v1.46 ลดระดับแม่น้ำ / คลองใน heightmap ได้ (ผู้ใช้พบว่าผิวน้ำในเกมต่ำกว่าตลิ่ง) — heightmap ใน repo ตอนนี้ยังเป็นชุดก่อนลดระดับ รอผู้ใช้ export ใหม่

## สูตรคำนวณที่ยืนยันแล้ว (ห้ามคิดใหม่จากศูนย์ — ผ่านการยิงทดสอบในเกมหลายรอบ)
- Low Angle มุมเงย: ชดเชยความสูงด้วยแบบจำลองแรงต้านอากาศ (v3.2.5) — **ไม่ใช้** dElevPer100m (ยิงจริงตกสั้น ~100 / ~300 m) · เคยลองย้อนเป็นสูตร trig atan(dz/range) แล้วกลับมาใช้แบบจำลองแรงต้าน หลังยิงเป็นกลุ่มแล้วกลุ่มกระสุนอยู่รอบเป้า (ยิงนัดเดียวหลอกได้เพราะ range dispersion)
- High Angle มุมเงย: (v3.6.0) ชดเชยความสูงด้วยแบบจำลองแรงต้านเหมือน Low (`heightCorrection(..., high=true)` — กิ่งมุมสูง Y ลดลงเมื่อมุมเพิ่ม) แทน D ELEV เดิม · เทียบกับแบบเดิม: Low ตรง ±1 mil, High คลาดไม่เกิน ~5 mil (2B14 −9 vs −13 ต่อ 50 m) · ToF High ยังใช้ `(baseTof + sqrt(baseTof² − 8·dz/g)) / 2` (ตรงกับ armacalc.pages.dev; ฟิสิกส์ต่างราว 0.3 s ที่ ToF 35 s) — ToF แสดงทศนิยม 1 ตำแหน่ง คลาด 0.1 s กระสุนอาจถึงพื้นก่อนชนวนทำงาน · เป้าสูงเกินระยะที่ charge ยิงถึง → `heightCorrection` คืน null → ใช้ atan(dz/ระยะ)
- คอลัมน์ dELEV / dTOF ในตารางชุดใหม่ = ต่างเมื่อระยะ +50 m (ไม่ใช่ต่อความสูงเป้า 100 m แบบตารางเดิม) — โค้ดไม่ใช้ · ฟิสิกส์: `a = −g·ŷ − (AirDrag/Mass)·|v|·v`, v0 ต่อ charge จาก `charges[c].v0` (ลงทะเบียนผ่าน `registerCharge`, ตรงกับแถวตารางทุกแถว คลาดแค่การปัดมุม) · 2A36 = 6000 mil ตามข้อมูลใหม่
- กราฟวิถี 2D / 3D, Alt @100m, จุด Air Fuze บนแผนที่ ใช้แบบจำลองแรงต้านอากาศ (v3.2.4 — แทน Bézier เดิม) · Air Fuze Timer ใช้สูตรเดิมที่ยืนยันในเกมแล้ว
- Air Fuze: `effectiveDz` (dz + airburstH) ใช้ **เฉพาะ** หาจุดตัดชนวนใน `getDragSimulatedPoints` ห้ามใช้กับ Elevation / ToF / PeakAlt (ใช้ dz จริง) · ผู้ใช้เลื่อนจุดเล็งให้ Air Fuze Point บนแผนที่ทับเป้าจริง (ไม่งั้นระเบิดก่อนถึงเป้า)
- ยังไม่ได้ยืนยันซ้ำ: เคส High Angle ~8000 m, dz < 0 (เคยแค่ "ตกใกล้" กับสูตรเก่า)

## ข้อมูลอาวุธ / ตาราง
- อาวุธ (ตามไฟล์ข้อมูลใหม่): 2B14 / M252 (profile Original + Adult Mortars), 2A36 Giatsint-B (CIE; 3OF29, 3OF59), M777A1 (CIE; M107, M795, M982A1), M777 Howitzer Artillery (PandaMods — label ต่อท้ายด้วยผู้สร้างเพราะชื่อเท่าชื่อ mod; M107, M982 Excalibur — ยิงผ่าน FDC Tablet) · **2B9 Vasilek ถูกนำออก** (ไม่มีในตารางชุดใหม่ — ตารางเดิมอยู่ใน git history ก่อน v3.6.0; ถ้าจะเอากลับต้องทำเป็นตาราง `manual` ใน ballistic_data.js)
- โค้ดข้าม Low Angle ถ้าเป็น mortar (`!isMortar && lowAngle`) · ปืนครกมีแต่ highAngle (c0–c4 = Ring)
- ตารางชุด v3.6.0 ครบทุก charge (ตรวจแล้ว: ไม่มี charge ไหนเหลือ ≤2 แถว) — High Angle ของ charge ต่ำมีแถวน้อยตามธรรมชาติ (ช่วงระยะแคบ) ไม่ใช่ข้อมูลขาด
- Fire History เก็บ weaponId / ammoId — รายการเก่า (id รุ่นก่อน v3.6.0) โหลดพิกัดได้แต่ไม่สลับอาวุธ (มี guard ใน `loadHistory`)

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
