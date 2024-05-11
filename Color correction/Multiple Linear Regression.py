#   bjut
#   编： 小鳄鱼
#   开发时间  2024/5/2 11:48

import cv2
import numpy as np
from sklearn.linear_model import LinearRegression
import warnings
from PIL import Image


# 假设我们已经有了采样值和标准色标值
# X为采样值矩阵，Y为标准色标值矩阵
label=[[116,81,67],[199,147,129],[91,122,156],[90,108,64],[130,128,176],[92,190,172],[224,124,47],[68,91,170],
   [198,82,97],[94,58,106],[159,189,63],[230,162,39],[35,63,147],[67,149,74],[180,49,57],[238,198,20],
   [193,84,151],[0,136,170],[245,245,243],[200,202,202],[161,163,163],[121,121,122],[82,84,86],[49,49,51]]

#导入采样数据
data = np.loadtxt('data/rgb.csv', delimiter=',',dtype=int)
data_list = data.tolist()
X = np.array(data_list)  # 采样值，其中R1, G1, B1是第一个色块的采样值
Y = np.array(label)  # 标准色标值

# 添加常数项以适应多元线性回归模型
X_b = np.c_[np.ones(X.shape[0]), X]

# 构建并拟合多元线性回归模型
model = LinearRegression()
model.fit(X_b, Y)

# 得到回归系数矩阵 W
W = model.coef_
W = W[:, 1:]  # 选择从第二个元素开始的所有元素
matr=np.mat([[191,124,100]])
pre=W.T*matr.T


# 读取要校正的图像
image_path = 'data/4.jpg'
image = Image.open(image_path)

# 校正图像中的每个像素点
# 获取图像的宽度和高度
width, height = image.size

# 遍历图像的每个像素点
for x in range(width):
    for y in range(height):
        # 获取当前像素的RGB值
        r, g, b = image.getpixel((x, y))

        # 应用多元线性回归模型来计算校正后的RGB值
        # 假设 W 是已经计算好的回归系数矩阵
        # 由于 W 是 3xN 矩阵，这里假设 N=3
        new_r, new_g, new_b = W.dot([r, g, b])

        # 应用公式（12）进行数值范围的调整
        new_r = min(max(int(new_r + 0.5), 0), 255)
        new_g = min(max(int(new_g + 0.5), 0), 255)
        new_b = min(max(int(new_b + 0.5), 0), 255)

        # 将新的RGB值赋给图像的对应像素点
        image.putpixel((x, y), (new_r, new_g, new_b))

# 显示修改后的图像
image.show()

# 如果需要，也可以将修改后的图像保存到文件
image.save('corrected_image.jpg')