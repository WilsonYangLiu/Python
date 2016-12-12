import csv, os
import numpy as np
import dim_reduce

with open("./CancerMatrix.csv", "rb") as csvfile:
    spamreader = csv.reader(csvfile)
    data = list(spamreader)

header = data.pop(0)
header.pop(0)
sample_name = []
for i in range(len(data)):
    sample_name.append(data[i].pop(0))
    
Cancer = np.array(data, dtype = np.float)
class_label1 = ['paracancer','paracancer','paracancer','paracancer','paracancer','paracancer','paracancer','paracancer','paracancer','lung cancer','lung cancer','lung cancer','lung cancer','lung cancer','paracancer','paracancer','paracancer','paracancer','paracancer','paracancer','paracancer','paracancer','paracancer','paracancer','paracancer','lung cancer','lung cancer','lung cancer','lung cancer','lung cancer','lung cancer','lung cancer','lung cancer','lung cancer','lung cancer','lung cancer','lung cancer','lung cancer','lung cancer','lung cancer']
class_label2 = ['poor','poor','poor','good','poor','poor','good','good','poor','poor','good','good','good','poor','poor','poor','poor','good','good','good','good','good','poor','good','good','poor','good','poor','poor','poor','good','good','good','good','poor','good','good','poor','poor','poor']

from sklearn.decomposition import PCA as sklearnPCA
sklearn_pca = sklearnPCA(n_components=3)
X_pca = sklearn_pca.fit_transform(Cancer)

dim_reduce.plot3D(X_pca, class_label1)
dim_reduce.plot3D(X_pca, class_label2)
