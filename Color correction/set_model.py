#   bjut
#   编： 小鳄鱼
#   开发时间  2024/4/22 10:22

import numpy as np


def models(label,taget):
    # 定义矩阵
    y = np.mat(label)
    X = np.mat(taget)
    # y = np.array(label)
    # X = np.array(taget)
    # y = y.tolist()
    # X = X.tolist()
    X11=X.T  # 转置  3*24
    X1 = X.T*X  #3*3

    # 计算矩阵的逆矩阵
    X1=X1.I

    X2 = X1*X11  *3*24
    X3 = X2*y  #系数矩阵
    return X3
