import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
from readdata import parsefile
from readdata import generateFeatureDic
def cluster(featureDic):
    data = generateFeatureDic(parsefile('swdata.txt'))
   # print(data)
    data = DataFrame(data)
    data.columns = ['c1','c2','c3','c4','c5','c6']
    print(data)
    data_zs = 1.0 * (data - data.mean())/data.std()
   # print(data_zs)
    k = 1
    threshold = 2 
    iteration = 500
    model = KMeans(n_clusters=k, n_jobs = 4, max_iter = iteration)
    model.fit(data_zs) 

    r = data_zs
   # r = pd.concat([data_zs,pd.Series(model.labels_, index = data.index)], axis = 1)
   # r.colunms = ['c1','c2','c3','c4','c5','c6','type']
  #  print(r)
    norm = []
    norm_tmp = r-model.cluster_centers_[0]
    norm_tmp = norm_tmp.apply(np.linalg.norm,axis = 1)
    norm.append(norm_tmp/norm_tmp.median())
    print(norm)
    norm = pd.concat(norm)    

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    norm[norm <= threshold].plot(style = 'go')
    
    discrete_points = norm[norm > threshold]
    discrete_points.plot(style = 'ro')
    
    for i in range(len(discrete_points)):
        id = discrete_points.index[i]
        n = discrete_points.iloc[i]
        plt.annotate('(%s,%0.2f)'%(id,n),xy= (id,n),xytext = (id,n))
    plt.xlabel(u'编号')
    plt.ylabel(u'相对距离')
    plt.show()


	
if __name__ == '__main__':
    data = generateFeatureDic(parsefile('swdata.txt'))
    cluster(data)
'''
__K-means算法的中心思想其实就是迭代，通过不断的迭代，使聚类效果达到局部最优__，为什么我们说局部最优呢？因为K-means算法的效果的优劣性和最初选取的中心点是有莫大关系的，我们只能在初始中心点的基础上达到局部最优解。K-means算法是基于距离的聚类算法，采用距离作为相似性的评价指标，即认为两个对象的距离越近，其相似度越大。该算法认为簇是由距离靠近的对象组成的，因此把得到紧凑且独立的簇作为最终目标。我感觉总的来说就是物以类聚。

对于聚类问题，我们事先并不知道给定的一个训练数集到底有哪些类别（即没有指定类标签），而是根据需要设置指定个数类标签的数量（但不知道具体的类标签是什么），然后通过K-means算法将具有相同特征，或者基于一定规则认为某一些对象相似，与其它一些组明显的不同的数据聚集到一起，自然形成分组。之后，我们可以根据每一组的数据的特点，给定一个合适的类标签（当然，可能给出类标签对实际应用没有实际意思，例如可能我们就想看一下聚类得到的各个数据集的相似性）。

在这里我们首先说明一个概念：质心（Centroid）。质心可以认为就是一个样本点，或者可以认为是数据集中的一个数据点P，它是具有相似性的一组数据的中心，即该组中每个数据点到P的距离都比到其它质心的距离近（与其它质心相似性比较低）。

__K个初始类聚类质心的选取对聚类结果具有较大的影响__，因为在该算法第一步中是随机的选取任意k个对象作为初始聚类的质心，初始地代表一个聚类结果，当然这个结果一般情况不是合理的，只是随便地将数据集进行了一次随机的划分，具体进行修正这个质心还需要进行多轮的计算，来进一步步逼近我们期望的聚类结果：具有相似性的对象聚集到一个组中，它们都具有共同的一个质心。另外，因为初始质心选择的随机性，可能未必使最终的结果达到我们的期望，所以我们可以多次迭代，每次迭代都重新随机得到初始质心，直到最终的聚类结果能够满足我们的期望为止。
### 1. 首先输入k的值，即我们希望将数据集D = {P1, P2, …, Pn}经过聚类得到k个分类（分组）。

### 2. 从数据集D中随机选择k个数据点作为质心，质心集合定义为：Centroid = {Cp1, Cp2, …, Cpk}，排除质心以后数据集O={O1, O2, …, Om}。

### 3. 对集合O中每一个数据点Oi，计算Oi与Cpj(j=1, 2, …,k)的距离，得到一组距离Si={si1, si2, …, sik}，计算Si中距离最小值，则该该数据点Oi就属于该最小距离值对应的质心。
### 4.每个数据点Oi都已经属于其中一个质心，然后根据每个质心所包含的数据点的集合，重新计算得到一个新的质心。
###5. 如果新计算的质心和原来的质心之间的距离达到某一个设置的阈值（表示重新计算的质心的位置变化不大，趋于稳定，或者说收敛），可以认为我们进行的聚类已经达到期望的结果，算法终止。

### 6. 如果新质心和原来之心距离变化很大，需要迭代2~5步骤。

'''
