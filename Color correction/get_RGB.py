#   bjut
#   编： 小鳄鱼
#   开发时间  2024/5/2 10:55

from PIL import Image, ImageTk
import tkinter as tk
import numpy as np

def on_click(event):
    global count, x1, y1, x2, y2
    if count == 0:
        x1, y1 = event.x, event.y
        label.config(text="点击右下角")
    elif count == 1:
        x2, y2 = event.x, event.y
        # img.crop((x1, y1, x2, y2)).save("cropped_image.png")
        temp=calculate_average_rgb(x1, y1, x2, y2)
        lst_rgb.append(temp)

        label.config(text="平均RGB值已计算")
    count += 1
    if count > 1:
        count = 0

def calculate_average_rgb(x1, y1, x2, y2):
    global img
    pixels = img.load()
    total_red, total_green, total_blue = 0, 0, 0
    num_pixels = 0
    for y in range(y1, y2):
        for x in range(x1, x2):
            total_red += pixels[x, y][0]
            total_green += pixels[x, y][1]
            total_blue += pixels[x, y][2]
            num_pixels += 1
    average_red = total_red // num_pixels
    average_green = total_green // num_pixels
    average_blue = total_blue // num_pixels
    print(f"平均RGB值: ({average_red}, {average_green}, {average_blue})")
    return [average_red,average_green,average_blue]  #返回一次的平均值

# 初始化Tkinter窗口
root = tk.Tk()
root.title("获取图片区域RGB平均值")

# 加载图片
image_path = 'data/4.jpg'  # 请替换为您的图片路径
img = Image.open(image_path)
img.resize((50,6))
img_tk = ImageTk.PhotoImage(img)
lst_rgb=[]


# 创建一个画布并绑定鼠标点击事件
canvas = tk.Canvas(root, width=img.width, height=img.height)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
canvas.bind("<Button-1>", on_click)

# 创建一个标签来显示提示信息
label = tk.Label(root, text="点击左上角")
label.pack()

count, x1, y1, x2, y2 = 0, 0, 0, 0, 0

root.mainloop()


# 将采集的数据存储
my_array = np.array(lst_rgb)

# 将数组保存为CSV格式的文本文件
# delimiter参数定义了字段分隔符，默认是逗号
np.savetxt('data/rgb.csv', my_array, delimiter=',', fmt='%s')