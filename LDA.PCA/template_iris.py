import pandas as pd
df = pd.io.parsers.read_csv(
    filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
    header=None,
    sep=',',
    )
feature_dict = {i:lable for i, lable in zip(
                range(4),
                ('sepal length in cm', 'sepal width in cm', 'petal length in cm', 'petal width in cm'))}
df.columns = [l for i, l in sorted(feature_dict.items())] + ['class_label']
# to drop the empty line at file-end
df.dropna(how = 'all', inplace = True)
#df.tail()

X = df[[0, 1, 2, 3]].values
y = df['class_label'].values

import dim_reduce

from sklearn.decomposition import PCA as sklearnPCA
sklearn_pca = sklearnPCA(n_components=3)
X_pca = sklearn_pca.fit_transform(X)

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as sklearnLDA
sklearn_lda = sklearnLDA(n_components=2)
X_lda_sklearn = sklearn_lda.fit_transform(X, y)





