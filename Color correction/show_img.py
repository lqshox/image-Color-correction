#   bjut
#   编： 小鳄鱼
#   开发时间  2024/5/9 22:01


from PIL import Image

# 打开两个图像
img1 = Image.open('corrected_svr_image.jpg')
img2 = Image.open('data/4.jpg')

# 确定新图像的尺寸
total_width = img1.width + img2.width
new_img = Image.new('RGB', (total_width, img1.height))

# 将两个图像粘贴到新图像上
new_img.paste(img1, (0, 0))
new_img.paste(img2, (img1.width, 0))

# 显示和保存新图像
new_img.show()
