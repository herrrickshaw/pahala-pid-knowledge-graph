"""Render every preview sheet html in a folder to a 1600 x 1130 png with headless Chrome, 4 in parallel."""
import sys, os, glob, subprocess
from concurrent.futures import ThreadPoolExecutor
CH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
d = os.path.abspath(sys.argv[1]); out = os.path.join(d, "png"); os.makedirs(out, exist_ok=True)
fs = sorted(f for f in glob.glob(os.path.join(d, "*_s*.html")))
def one(f):
    png = os.path.join(out, os.path.basename(f)[:-5] + ".png")
    if os.path.exists(png): return 1
    r = subprocess.run([CH, "--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1600,1130", f"--screenshot={png}", "file://" + f], capture_output=True, timeout=120)
    return int(os.path.exists(png))
with ThreadPoolExecutor(4) as ex: n = sum(ex.map(one, fs))
print(n, "of", len(fs), "rendered")
