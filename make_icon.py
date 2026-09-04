from PIL import Image, ImageDraw

def make_icon(size, path):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = int(size * 0.2)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=(83, 74, 183, 255))
    try:
        from PIL import ImageFont
        font = ImageFont.truetype("seguiemj.ttf", int(size * 0.55))
        text = "\U0001F4B3"
        bbox = d.textbbox((0, 0), text, font=font, embedded_color=True)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        d.text(((size - w) / 2 - bbox[0], (size - h) / 2 - bbox[1]), text, font=font, embedded_color=True)
    except Exception as e:
        print("emoji font failed, drawing plain shape:", e)
        cw = size * 0.6
        ch = size * 0.4
        cx, cy = size / 2, size / 2
        d.rounded_rectangle([cx - cw/2, cy - ch/2, cx + cw/2, cy + ch/2], radius=int(size*0.06), outline=(255,255,255,255), width=max(2,int(size*0.03)))
        d.line([cx - cw/2, cy - ch*0.05, cx + cw/2, cy - ch*0.05], fill=(255,255,255,255), width=max(2,int(size*0.08)))
    img.save(path)

make_icon(192, "icon-192.png")
make_icon(512, "icon-512.png")
print("done")
