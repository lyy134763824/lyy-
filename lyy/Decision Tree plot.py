# -*-coding:utf-8-*-
# 利用安装的库graphviz进行决策树的绘制
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import graphviz
import warnings
warnings.filterwarnings('ignore')

# 数据集
def createDataSet():
    row_data = {'no surfacing': [1, 1, 1, 0, 0],
                'flippers':[1,1,0,1,1],
                'fish':['yes','yes','no','no','no']}
    dataSet = pd.DataFrame(row_data, columns=['no surfacing', 'flippers', 'fish']) # 习惯将标签放在最后一列
    return dataSet
dataSet = createDataSet()

# 特征
Xtrain = dataSet.iloc[:,:-1]
# 标签
Ytrain = dataSet.iloc[:,-1]

# 将本文转换为数字(这里可以用sklearn中.processing库中LabelEncoder直接进行修改）
labels = Ytrain.unique().tolist()
Ytrain = Ytrain.apply(lambda x: labels.index(x))

# 绘制树模型
clf = DecisionTreeClassifier()
clf = clf.fit(Xtrain, Ytrain)
tree.export_graphviz(clf)

# 给图形增加标签和颜色
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=['no surfacing', 'flippers'],
                                class_names=['fish', 'not fish'],
                                filled=True, rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)

# 利用render方法生成图形,保存为pdf格式
graph.render("fish")
