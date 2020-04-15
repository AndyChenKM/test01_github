from PIL import Image, ImageDraw

# 1.创建画板
im = Image.new(mode="RGB", size=(300, 300), color="white")
im.save('test.bmp')

# 2.启动画图
draw = ImageDraw.Draw(im)

# 3.描出矩形的四个点
draw.polygon([(200, 200), (220, 200), (220, 240), (200, 240)],
             outline="blue")

# 4.保存图片
im.save('test.bmp')

# 5.展示图片
im.show()