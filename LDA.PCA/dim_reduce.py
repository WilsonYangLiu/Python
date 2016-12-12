#! python 2.7
# encoding: utf-8
# see: http://sebastianraschka.com/Articles/2014_python_lda.html
from sklearn.preprocessing import LabelEncoder, StandardScaler
from matplotlib import pyplot as plt
import numpy as np
import math
import colorsys
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

def _get_colors(num_colors):
    '''
    Automatically generate N "distinct" colors
    num_colors: number of colors
    Return: color sets
    More info: http://stackoverflow.com/questions/470690/how-to-automatically-generate-n-distinct-colors
    '''
    colors = []
    for i in np.arange(0., 360., 360. / num_colors):
        hue = i/360.
        lightness = (50 + np.random.rand() * 10)/100.
        saturation = (90 + np.random.rand() * 10)/100.
        colors.append(colorsys.hls_to_rgb(hue, lightness, saturation))
    return colors

def PCA(X, n_comp = 5, covmat = True):
    '''
    X: Data without categorial labels [n_samples, n_features]
    n_comp: number of components, list
    covmat: bool. if true, calculate covariance matrix. Otherwise, the correlation matrix (Especially, in the field of "Finance")
    Return: [new_X, eig_pairs]
    '''
    n_features = X.shape[1]
    
    # Standardizing
    X_std = StandardScaler().fit_transform(X)
    # calculate covariance Matrix or correlation matrix. Perform an eigendecomposition on the covariance (correlation) matrix
    if covmat:
        mat = np.cov(X_std, rowvar = False)
        eig_vals, eig_vecs = np.linalg.eig(mat)
    else:
        mat = np.corrcoef(X_std, rowvar = False)
        eig_vals, eig_vecs = np.linalg.eig(mat)
    
    # Selecting Principal Components
    eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
    eig_pairs = sorted(eig_pairs, key=lambda k: k[0], reverse=True)
    W = np.hstack([eig_pairs[i][1].reshape(n_features, 1) for i in range(0, min(n_comp, len(eig_vals)))])
    new_X = X_std.dot(W)
    return [new_X, eig_pairs]

def LDA(X, label, n_comp = 5):
    '''
    X: Data without categorial labels
    label: coresponding categorial labels
    n_comp: number of components
    Return: [new_X, eig_pairs]
    '''
    enc = LabelEncoder()
    label_enc = enc.fit(label)
    y = label_enc.transform(label) + 1
    
    class_labels = np.unique(y)
    n_classes = class_labels.shape[0]
    n_features = X.shape[1]

    # Computing the d-dimensional mean vectors
    mean_vectors = []
    for cl in class_labels:
        mean_vectors.append(np.mean(X[y == cl], axis = 0))

    # Computing the Scatter Matrices (within class)
    S_W = np.zeros((n_features, n_features))
    for cl, mv in zip(class_labels, mean_vectors):
        class_sc_mat = np.zeros((n_features, n_features))
        mv = mv.reshape(n_features, 1)
        for row in X[y == cl]:
            row = row.reshape(n_features, 1)
            class_sc_mat += (row-mv).dot((row-mv).T)
        S_W += class_sc_mat

    # Computing the Scatter Matrices (between class)
    overall_mean = np.mean(X, axis=0)
    S_B = np.zeros((n_features, n_features))
    for i, mean_vec in enumerate(mean_vectors):
        n = X[y==i+1,:].shape[0]
        mean_vec = mean_vec.reshape(n_features, 1)
        overall_mean = overall_mean.reshape(n_features, 1)
        S_B += n * (mean_vec - overall_mean).dot((mean_vec - overall_mean).T)

    # Calculate the generalized eigenvalue of inverse(S_W) .dot S_B
    eig_vals, eig_vecs = np.linalg.eig(np.linalg.inv(S_W).dot(S_B))
    # Selecting linear discriminants for the new feature subspace
    eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
    eig_pairs = sorted(eig_pairs, key=lambda k: k[0], reverse=True)
    W = np.hstack([eig_pairs[i][1].reshape(n_features, 1) for i in range(0, min(n_comp, len(eig_vals)))])
    new_X = X.dot(W)
    return [new_X, eig_pairs]
    
def plot3D(X, class_label):
    '''
    X: sew subspace
    class_label: class labels
    '''
    enc = LabelEncoder()
    label_enc = enc.fit(class_label)
    y = label_enc.transform(class_label) + 1
    
    dicts = {i:lb for i, lb in zip(y, class_label)}
    
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    # global parameters
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['lines.linestyle'] = ''
    marker = '.'
    for label,color in zip(
        range(1, len(np.unique(y))+1), _get_colors(len(np.unique(y)))):
        ax.plot(X[:,0].real[y == label],
                X[:,1].real[y == label],
                X[:,2].real[y == label],
                marker=marker,
                markersize=8,
                color=color,
                alpha=0.5,
                label=dicts[label]
                )
   
    ax.set_xlabel('x_values')
    ax.set_ylabel('y_values')
    ax.set_zlabel('z_values')
    
    leg = plt.legend(loc='upper right', fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.title('The first 3 linear dimension')
    
    plt.grid()
    plt.tight_layout
    plt.show()
    
    
def plot_lda(X_lda, class_label):
    '''
    X_lda: sew subspace
    class_label: class labels
    '''
    enc = LabelEncoder()
    label_enc = enc.fit(class_label)
    y = label_enc.transform(class_label) + 1
    
    dicts = {i:lb for i, lb in zip(y, class_label)}

    ax = plt.subplot(111)
    marker = '.'
    for label,color in zip(
        range(1, len(np.unique(y))+1), _get_colors(len(np.unique(y)))):
        plt.scatter(x=X_lda[:,0].real[y == label],
                y=X_lda[:,1].real[y == label],
                marker=marker,
                color=color,
                alpha=0.5,
                label=dicts[label]
                )

    plt.xlabel('LD1')
    plt.ylabel('LD2')

    leg = plt.legend(loc='upper right', fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.title('LDA: The first 2 linear discriminants')

    # hide axis ticks
    plt.tick_params(axis="both", which="both", bottom="off", top="off",  
            labelbottom="on", left="off", right="off", labelleft="on")

    # remove axis spines
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)    

    plt.grid()
    plt.tight_layout
    plt.show()

def plot_hist(X, label, nrow = 1, ncol = 1, feature = 0):
    '''
    X: Data without categorial labels
    label: coresponding categorial labels
    nrows, ncols: number of row, col in the figure
    '''
    enc = LabelEncoder()
    label_enc = enc.fit(label)
    y = label_enc.transform(label) + 1

    class_labels = np.unique(y)
    n_classes = class_labels.shape[0]
    n_features = X.shape[1]

    dicts = {i:lb for i, lb in zip(y, label)}

    fig, axes = plt.subplots(nrows = nrow, ncols = ncol, figsize = (12, 6))
    for ax, cnt in zip(axes.ravel(), range(n_features)):
        # set bin sizes
        min_b = math.floor(np.min(X[:, cnt]))
        max_b = math.ceil(np.max(X[:, cnt]))
        bins = np.linspace(min_b, max_b, 25)
    
        # plotting the histograms
        ## label: Bar charts yield multiple patches per dataset, but only the first gets the label, so that the legend command will work as expected.
        ## ax.get_ylim(): Get the y-axis range
        ## alpha: Set the alpha tranparency
        for lab, col in zip(range(1, n_classes+1), _get_colors(n_classes)):
            ax.hist(X[y == lab, cnt],
                    color = col,
                    label = 'class %s' % dicts[lab],
                    bins = bins,
                    alpha = 0.5,)
            ylims = ax.get_ylim()

        # plot annotation
        leg = ax.legend(loc = 'upper right', fancybox = True, fontsize = 8)
        leg.get_frame().set_alpha(0.5)
        
        ax.set_ylim([0, max(ylims)+2])
        if feature == 0:
            ax.set_xlabel(cnt)
        else:
            ax.set_xlabel(feature[cnt])
        ax.set_title('histogram #%s' %str(cnt+1))

        # hide axis ticks
        ax.tick_params(axis="both", which="both", bottom="off", top="off",  
                labelbottom="on", left="off", right="off", labelleft="on")

        # remove axis spines
        ax.spines["top"].set_visible(False)  
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["left"].set_visible(False)

    axes[0][0].set_ylabel('count')
    axes[1][0].set_ylabel('count')
    #Adjust subplot parameters to give specified padding
    fig.tight_layout()

    plt.show()

def plot_pca(X_pca, class_label):
    '''
    X_pca: sew subspace
    class_label: class labels. 
    '''
    enc = LabelEncoder()
    label_enc = enc.fit(class_label)
    y = label_enc.transform(class_label) + 1
    
    dicts = {i:lb for i, lb in zip(y, class_label)}

    ax = plt.subplot(111)
    marker = '.'
    for label,color in zip(
        range(1, len(np.unique(y))+1), _get_colors(len(np.unique(y)))):
        plt.scatter(x=X_pca[:,0].real[y == label],
                y=X_pca[:,1].real[y == label],
                marker=marker,
                color=color,
                alpha=0.5,
                label=dicts[label]
                )

    plt.xlabel('PC1')
    plt.ylabel('PC2')

    leg = plt.legend(loc='upper right', fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.title('PCA: The first 2 principal components')

    # hide axis ticks
    plt.tick_params(axis="both", which="both", bottom="off", top="off",  
            labelbottom="on", left="off", right="off", labelleft="on")

    # remove axis spines
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)    

    plt.grid()
    plt.tight_layout
    plt.show()
    
