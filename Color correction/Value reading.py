#   bjut
#   编： 小鳄鱼
#   开发时间  2024/4/18 16:26
from PIL import Image
import numpy as np
import pandas as pd


def got_RGB(img_path):
    img = Image.open(img_path)
    width, height = img.size
    img = img.convert('RGB')
    array = []
    sum_r,sum_g,sum_b=0,0,0
    for i in range(width):
        for j in range(height):
            r, g, b = img.getpixel((i, j))
            sum_r+=r
            sum_g+=g
            sum_b+=b
            if r != 0:
                pass
                # print(r, b, g)
            rgb = (r, g, b)
            array.append(rgb)
    return (sum_r//(width*height),sum_g//(width*height),sum_b//(width*height))


if __name__ == "__main__":
    lst=['data/f.jpg','data/brown.jpg']
    rgb=[]
    for path in lst:
        img_path = fr'{path}'  # 图像路径
        temp=got_RGB(img_path)
        rgb.append(temp)
    np.savez('data/get_rgb', rgb)




