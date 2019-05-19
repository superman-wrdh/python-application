# encoding utf8
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import datetime

# 设置所使用的字体
# font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 200)
font_size = 220
font = ImageFont.truetype("simsun.ttc", font_size, encoding="unic")
font2 = ImageFont.truetype("simsun.ttc", font_size - 50, encoding="unic")
# 打开图片
imageFile = "m1.jpg"
im1 = Image.open(imageFile)

wight, height = im1.size

# 画图
draw = ImageDraw.Draw(im1)
text = "今日鸡汤:感谢那些伤害你的人,他们让你变得更强大"
date = "----- 尼古拉斯.超人" + str(datetime.now().date())
# text = text.encode("utf8").decode("utf8")
# draw.text((160, 0), "2019-5-19", (255, 0, 0), font=font)  # 设置文字位置/内容/颜色/字体
draw.text((100, height * 0.9), text, (255, 0, 0), font=font)  # 设置文字位置/内容/颜色/字体
draw.text((wight * 0.4, height * 0.9 + font_size * 2), date, (148, 0, 211), font=font)  # 设置文字位置/内容/颜色/字体
draw = ImageDraw.Draw(im1)  # Just draw it!

# 另存图片
im1.save("m2.jpg")
