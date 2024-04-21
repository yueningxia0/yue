import  numpy as np
from sklearn.decomposition import PCA

def dPCA(arry,k):
    # 原始数据均值化
    mean = np.mean(arry,0)   #求每列的均值
    centrArry = arry - mean  #样本值中心化矩阵
    print("中心化矩阵:\n", centrArry)

    # 协方差矩阵
    n = np.shape(arry)[0]    #样本个数
    cov = np.dot(centrArry.T,centrArry) / n
    print("协方差矩阵:\n", cov)

    # 求协方差矩阵的特征向量和特征值
    a,b = np.linalg.eig(cov)  #求cov的特征向量b和特征值a
    sorta = np.argsort(-1*a)  #给特征值排序，降序，输出的是排序后的索引
    print("特征值:\n", a)
    print("特征向量:\n", b)

    # 构建K阶降维的降维转换矩阵
    uT = [b[:,sorta[i]] for i in range(k)]
    u = np.transpose(uT) # uT是list，不能用.T
    print("降维转换矩阵:\n", u)

    # 降维矩阵 = 原始矩阵*降维转换矩阵
    z = np.dot(arry,u)
    print("降维矩阵:\n",z)
    return z

if __name__ == '__main__':
    arry = np.array([[10, 15, 29],
              [15, 46, 13],
              [23, 21, 30],
              [11, 9,  35],
              [42, 45, 11],
              [9,  48, 5],
              [11, 21, 14],
              [8,  5,  15],
              [11, 12, 21],
              [21, 20, 25]])
    k = np.shape(arry)[1]-1
    print("样本：\n",arry)
    z = dPCA(arry,k)

    #直接调用pca算法
    pca = PCA(n_components=k)  # 降到2维
    pca.fit(arry)  # 执行
    newX = pca.fit_transform(arry)  # 降维后的数据
    print("pca算法降维后:\n",newX)  # 输出降维后的数据