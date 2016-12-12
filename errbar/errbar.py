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

def errbar(data, Group, yl = 10, ym = 1000, savefile = r'errbar.png'):
	x = np.unique(data[:, 1])
	x = x.astype(np.float64)
	x.sort()

	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1 , xlim=[x.min() - 0.5, x.max() + 0.5], ylim=[yl, ym] )

	ax.set_yscale('log')
	
	Legend = []
	for g, col in zip(Group, _get_colors(len(Group)) ):
		gData = data[data[:, 0] == g][:, [1, 2]]
		gData = gData.astype(np.float64)
		Points = np.unique(gData[:, 0])
		Points.sort()
		p_l = []; p_m = []; p_u =[]
		for p in Points:
			tmp = gData[gData[:, 0] == p][:, 1]
			#tmp = tmp.astype(np.float64)
			p_l.append(tmp.min() )
			p_m.append(tmp.mean() )
			p_u.append(tmp.max() )
			
		p_l = np.array(p_l); p_m = np.array(p_m); p_u = np.array(p_u)
		errbarPlt = plt.errorbar(Points, p_m, yerr=[p_m - p_l, p_u - p_m], color=col, fmt='-o')
		Legend.append(errbarPlt)
		
	ax.legend(Legend, Group)
	ax.axhline(y=yl, linewidth=2, color="black")
	ax.axvline(x=x.min() - 0.5, linewidth=2, color="black")
	ax.tick_params(length=4, width=2)
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')
	
	plt.savefig(savefile)
	plt.show()
	
	
if __name__ == '__main__':
	if len(sys.argv) != 3:
		usage()
	
	with open(sys.argv[1], 'rU') as csvfile:
		spamreader = csv.reader(csvfile)
		Data = np.array(list(spamreader) )[1:, :]
		
	Group = np.unique(Data[:, 0])
	errbar(Data[:, :], Group, savefile = sys.argv[2] + r'.png')
