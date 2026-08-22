import pathlib
import subprocess

from PIL import Image

cmd = pathlib.Path.cwd()

TEST_IMAGES_DIR = cmd / "test-images"
STAGE_DIR = cmd / "staged_images"  # demo.py only accepts .jpg/.png, so .jpeg files get restaged here
OUT = cmd / "output"
STAGE_DIR.mkdir(exist_ok=True)
OUT.mkdir(exist_ok=True)

order = ["1", "2", "3", "4", "5", "7", "8", "10", "12", "13",
"21", "22"]

paths = []
for n in order:
    src = sorted(TEST_IMAGES_DIR.glob(f"{n}.*"))[0]
    if src.suffix.lower() == ".jpeg":
        input_path = STAGE_DIR / f"{n}.jpg"
        Image.open(src).convert("RGB").save(input_path)
    else:
        input_path = src

    subprocess.run(
        [
            "python", "demo.py",
            "--input-filename", str(input_path),
            "--output-dir", "output/",
            "--modality", "image",
        ],
        check=True,
    )
    paths.append(OUT / f"{n}_image_output.png")

cols = 4
rows = 3
thumb_w, thumb_h = 480, 360
pad = 8
label_h = 30

cell_w = thumb_w + 2 * pad
cell_h = thumb_h + 2 * pad + label_h

canvas = Image.new("RGB", (cols * cell_w, rows * cell_h), (255,
255, 255))

from PIL import ImageDraw, ImageFont
draw = ImageDraw.Draw(canvas)
try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
except Exception:
    font = ImageFont.load_default()

for idx, (name, p) in enumerate(zip(order, paths)):
    img = Image.open(p).convert("RGB")
    # resize to fit within thumb box, preserving aspect ratio
    img.thumbnail((thumb_w, thumb_h), Image.LANCZOS)
    r, c = divmod(idx, cols)
    x0 = c * cell_w
    y0 = r * cell_h
    # center thumbnail
    off_x = x0 + pad + (thumb_w - img.width) // 2
    off_y = y0 + pad + (thumb_h - img.height) // 2
    canvas.paste(img, (off_x, off_y))
    label = f"test-images/{name}"
    bbox = draw.textbbox((0, 0), label, font=font)
    tw = bbox[2] - bbox[0]
    draw.text((x0 + (cell_w - tw) // 2, y0 + thumb_h + 2 * pad),
label, fill=(0, 0, 0), font=font)

out_path = cmd / "gaze3d_matrix.png"
canvas.save(out_path)
print("saved", out_path, canvas.size)