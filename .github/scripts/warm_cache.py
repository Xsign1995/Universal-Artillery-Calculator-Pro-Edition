"""อุ่น cache ของ CDN หลัง deploy: ยิงไฟล์หนักของแผนที่ใน maps/ ให้ตรงกับ URL (รวม ?v=) ที่ index.html ใช้จริง"""
import re, sys, os
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen

BASE = sys.argv[1].rstrip("/") + "/"
DRY = "--dry" in sys.argv
MAX_ZOOM = 4  # ชั้น tile ที่แอปโหลดตอนเปิดแผนที่ (ชั้นฐาน + ชั้นละเอียดแรก ๆ)

html = open("index.html", encoding="utf-8").read()
urls = []

# tiles: LOCAL_TILE_MAPS → ไฟล์จริงใน maps/<Map>/TileGroup*/<z>-<col>-<row>.jpg
block = re.search(r"const LOCAL_TILE_MAPS = \{(.*?)\n\s*\};", html, re.S).group(1)
for m in re.finditer(r'"(\w+)":\s*\{\s*base:\s*"([^"]+)".*?v:\s*"([^"]+)"', block):
    name, base, v = m.groups()
    for root, _, files in os.walk(base):
        for f in files:
            t = re.fullmatch(r"(\d+)-\d+-\d+\.jpg", f)
            if t and int(t.group(1)) <= MAX_ZOOM:
                urls.append(f"{BASE}{root.replace(os.sep, '/')}/{f}?v={v}")

# heightmap: FILES ใน HeightMap
block = re.search(r"const FILES = \{(.*?)\n\s*\};", html, re.S).group(1)
for m in re.finditer(r'path:\s*"([^"]+)",\s*v:\s*"([^"]+)"', block):
    path, v = m.groups()
    urls += [f"{BASE}{path}.png?v={v}", f"{BASE}{path}.json?v={v}"]

print(f"warm-up {len(urls)} URLs")
if DRY:
    print("\n".join(urls[:5]), "...", urls[-2:], sep="\n")
    sys.exit(0)

def hit(u):
    try:
        with urlopen(Request(u, headers={"User-Agent": "cache-warmup"}), timeout=60) as r:
            while r.read(1 << 20):
                pass
            return r.status
    except Exception as e:
        return str(e)

with ThreadPoolExecutor(16) as ex:
    res = list(ex.map(hit, urls))
bad = [(u, s) for u, s in zip(urls, res) if s != 200]
print(f"ok {len(urls) - len(bad)} / failed {len(bad)}")
for u, s in bad[:10]:
    print("  ", s, u)
