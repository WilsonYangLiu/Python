#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os, sys
import csv
import colorsys
import numpy as np
import matplotlib.pyplot as plt

def usage():
	print '''
Plot the errorbar figure
		
usage: 
   [python] errbar.py database out_fig
		
argument:
   database:	file contains the data; the first column is the groups, second is the x axis data, third is y axis data
   out_png:	file that want to store the results

Example: 
   errbar.py CPT.csv plot
	'''

	sys.exit(1)

def _get_colors(num_colors):
    '''
    Automatically generate N "distinct" colors
	
	Parameter:
		num_colors: number of colors
		
    Return: 
		color sets
			more info: http://stackoverflow.com/questions/470690/how-to-automatically-generate-n-distinct-colors
    '''
    colors = []
    for i in np.arange(0., 360., 360. / num_colors):
        hue = i/360.
        lightness = (50 + np.random.rand() * 10)/100.
        saturation = (90 + np.random.rand() * 10)/100.
        colors.append(colorsys.hls_to_rgb(hue, lightness, saturation))
    return colors

def errbar(data, Group, ylim=None, savefile = r'errbar.png', yerr=True, LOG=False, set_yscale='linear', show_plot=True, afterLOG=False, LOGbase=2):
	'''
	Parameter:
		data: n * 3 ndarray. Each row for one measure. 
			col 1: name of measure; col 2: measure condition; col 3: value of measure
		Group: a ndarray contains all types of measure, e.g. the gene set
		ylim: either 'None' or a 2 element list. The range of y axis
		savefile: the filename of the saved figure
		yerr: boolen. Draw the error bar or not
		LOG: boolen. transform the [min, mean and max value] to the logarithmic form after calculate these three values or not
		set_yscale: set the scaling of the y-axis: 'linear | 'log' | 'logit' | 'symlog'
			read more: http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.set_yscale
		show_plot: boolen. show the plot or not
		afterLOG: boolen. whether the values of the measure are the form of logarithmic transformation or not
		LOGbase: if afterLOG was True, the base of the logarithmic transformation. Default to 2
	'''
	x = np.unique(data[:, 1])
	x = x.astype(np.float64)
	x.sort()

	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1 , xlim=[x.min() - 0.1, x.max() + 0.1], ylim=ylim )

	ax.set_yscale(set_yscale)
	
	Legend = []
	for g, col in zip(Group, _get_colors(len(Group)) ):
		gData = data[data[:, 0] == g][:, [1, 2]]
		gData = gData.astype(np.float64)
		Points = np.unique(gData[:, 0])
		Points.sort()
		p_l = []; p_m = []; p_u =[]
		for p in Points:
			# whether the values of the measure are the form of logarithmic transformation or not
			if afterLOG:
				tmp = np.power(LOGbase, gData[gData[:, 0] == p][:, 1])
			else:
				tmp = gData[gData[:, 0] == p][:, 1]
			
			p_l.append(tmp.min() )
			p_m.append(tmp.mean() )
			p_u.append(tmp.max() )
		
		if LOG:
			p_l = np.log2(np.array(p_l)); p_m = np.log2(np.array(p_m)); p_u = np.log2(np.array(p_u))
		else:	
			p_l = np.array(p_l); p_m = np.array(p_m); p_u = np.array(p_u)
			
		if yerr:
			errbarPlt = plt.errorbar(Points, p_m, yerr=[p_m - p_l, p_u - p_m], color=col, fmt='-o')
		else:
			errbarPlt = plt.errorbar(Points, p_m, color=col, fmt='-o')
		Legend.append(errbarPlt)
		
	ax.legend(Legend, Group, ncol=3)
	#ax.legend(Legend, Group, bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=4, mode="expand", borderaxespad=0.)
	if ylim:
		ax.axhline(y=ylim[0], linewidth=2, color="black")
	ax.axvline(x=x.min() - 0.1, linewidth=2, color="black")
	ax.tick_params(length=4, width=2)
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')
	
	plt.savefig(savefile)
	if show_plot:
		plt.show()
	
	
if __name__ == '__main__':
	if len(sys.argv) != 3:
		usage()
	
	with open(sys.argv[1], 'rU') as csvfile:
		spamreader = csv.reader(csvfile)
		Data = np.array(list(spamreader) )[1:, :]
		
	Group = np.unique(Data[:, 0])
	errbar(Data[:, :], Group, ylim=[-1., 1.5], savefile = sys.argv[2] + r'.png', yerr=False, LOG=True) 
