#! python 2.7
# encoding: utf-8
import numpy as np
np.random.seed(4294967295)

# generate two 3*20 datasets
mean_vec1 = np.array([0,0,0])
cov_mat1 = np.array([[1,0,0],[0,1,0],[0,0,1]])
class1_sample = np.random.multivariate_normal(mean_vec1, cov_mat1, 20).T
assert class1_sample.shape == (3,20), "The matrix has not the dimensions 3x20"

mean_vec2 = np.array([1,1,1])
cov_mat2 = np.array([[1,0,0],[0,1,0],[0,0,1]])
class2_sample = np.random.multivariate_normal(mean_vec2, cov_mat2, 20).T
assert class1_sample.shape == (3,20), "The matrix has not the dimensions 3x20"

all_samples = np.concatenate((class1_sample, class2_sample), axis=1)
assert all_samples.shape == (3,40), "The matrix has not the dimensions 3x40"

import dim_reduce
label = ["class 1"]*20 + ["class 2"]*20

dim_reduce.plot3D(all_samples.T, label)

new_samples, eigs = dim_reduce.PCA(all_samples.T)
dim_reduce.plot3D(new_samples, label)
