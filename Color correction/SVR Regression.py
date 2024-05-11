#   bjut
#   编： 小鳄鱼
#   开发时间  2024/5/9 16:10
from PIL import Image
from sklearn.svm import SVR
import numpy as np
import warnings
#忽略报错
warnings.filterwarnings('ignore')

label=[[116,81,67],[199,147,129],[91,122,156],[90,108,64],[130,128,176],[92,190,172],[224,124,47],[68,91,170],
   [198,82,97],[94,58,106],[159,189,63],[230,162,39],[35,63,147],[67,149,74],[180,49,57],[238,198,20],
   [193,84,151],[0,136,170],[245,245,243],[200,202,202],[161,163,163],[121,121,122],[82,84,86],[49,49,51]]
R_standard=[]
G_standard=[]
B_standard=[]
for item in label:
   R_standard.append(item[0])
   G_standard.append(item[1])
   B_standard.append(item[2])


#导入采样数据
data = np.loadtxt('data/rgb.csv', delimiter=',',dtype=int)
data_list = data.tolist()
X = np.array(data_list)  # 训练矩阵，采样值
Y = np.array([R_standard, G_standard, B_standard])  # 标准色标值组成的矩阵

#训练支持向量回归模型    为R、G、B各训练一个SVR模型

svr_r = SVR(kernel='linear', C=1.0, epsilon=0.1)
svr_r.fit(X, Y[0])

svr_g = SVR(kernel='linear', C=1.0, epsilon=0.1)
svr_g.fit(X, Y[1])

svr_b = SVR(kernel='linear', C=1.0, epsilon=0.1)
svr_b.fit(X, Y[2])


# 遍历图像中的每个像素点   对图像中的每个像素点，使用训练好的模型计算预测值。

image_path = 'data/4.jpg'
image = Image.open(image_path)

# 获取图像的宽度和高度
width, height = image.size
cnt=0
# 校正图像中的每个像素点
for x in range(width):
   for y in range(height):
      # 获取当前像素的RGB值
      pixel = np.array(image.getpixel((x, y))).reshape(1, -1)

      # 使用训练好的模型预测R、G、B值
      predicted_r = svr_r.predict(pixel)
      predicted_g = svr_g.predict(pixel)
      predicted_b = svr_b.predict(pixel)

      # 应用文献中的公式（12）进行数值范围的调整
      predicted_r = max(0, min(predicted_r, 255))
      predicted_g = max(0, min(predicted_g, 255))
      predicted_b = max(0, min(predicted_b, 255))

      # 更新像素值
      image.putpixel((x, y), (int(predicted_r), int(predicted_g), int(predicted_b)))
      if x>cnt:
         print(cnt)
         cnt=x


# 显示修改后的图像
image.show()
# 保存校正后的图像
corrected_image_path = 'corrected_svr_image.jpg'
image.save(corrected_image_path)
