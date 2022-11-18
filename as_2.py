from PIL import ImageFont, Image, ImageDraw

text = "平泉 最高"
image = Image.open("images/konjikido_01 2.jpg")
image = image.resize((1000, 400))

font_path = "/System/Library/Fonts/Arial Unicode.ttf"
font_size = 100
font_color = (255, 200, 169)
font = ImageFont.truetype(font_path, font_size)

(w, h), (x, y) = font.font.getsize(text)
W, H = image.size
pos = ((W - w) / 2, (H - h) / 2)

draw = ImageDraw.Draw(image)

draw.text(pos, text, font=font, fill=font_color)
image.save("images/after.jpg")
image.show()
