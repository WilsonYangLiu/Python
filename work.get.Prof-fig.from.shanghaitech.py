#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
	
import os,sys,urllib,urllib2,urlparse	
from sgmllib import SGMLParser
	
img = []
class URLLister(SGMLParser):
	is_a = ""
	is_div = ""
	def reset(self):	
		SGMLParser.reset(self)
		self.urls=[]	
		self.imgs=[]
		self.names=[]
		self.positions=[]
	def start_a(self, attrs):
		for k, v in attrs:
			if (k=="class") & (v == "ju"):
				self.is_a = 1
		href = [ "http://www.shanghaitech.edu.cn" + v for k,v in attrs if k=="href" and v.startswith("/faculty")]
		if href:	
			self.urls.extend(href)
	def end_a(self):
		self.is_a = ""
	def handle_data(self, text):	
		if self.is_a:	
			self.names.append(text)	
	def start_img(self, attrs):	
		src = [ v for k,v in attrs if k=="src" and v.startswith("http://www.shanghaitech.edu.cn/upload/photo") ]	
		if src:	
			self.imgs.extend(src)
	
	def start_div(self, attrs):
		for k, v in attrs:
			if (k=="class") & (v == "line"):
				self.is_div = 1
	def end_div(self):
		self.is_div = 0
	def handle_data(self, text):
		if self.is_div:	
			self.positions.append(text)
	
	
def get_url_of_page(url, if_img = False):	
	urls = []
	try:	
		f = urllib2.urlopen(url, timeout=10).read()	
		url_listen = URLLister()	
		url_listen.feed(f)	
		if if_img:	
			urls.extend(url_listen.imgs)
		else:	
			urls.extend(url_listen.urls)
	except urllib2.URLError, e:	
		print e.reason	
	return urls #zip(names, urls)

#递归处理页面	
def get_page_html(begin_url, depth, ignore_outer = True):	
	#若是设置排除外站 过滤之
	main_site_domain = urlparse.urlsplit(begin_url).netloc
	#print "main site domain: ", main_site_domain
	if ignore_outer:	
		if not main_site_domain in begin_url:	
			return	
	
	if depth == 1:	
		urls = get_url_of_page(begin_url, True)	
		img.extend(urls)	
	else:	
		urls = get_url_of_page(begin_url)	
		if urls:	
			for url in urls:	
				get_page_html(url, depth-1)

#
def position(url):
	urls = get_url_of_page(url)
	names = []
	for link in urls:
		try:	
			f = urllib2.urlopen(link, timeout=10).read()
			urllib.unquote(f)
			url_listen = URLLister()	
			url_listen.feed(f)	 
			names.extend(url_listen.positions)
		except urllib2.URLError, e:	
			print e.reason	
	return names #zip(names, urls)

#取得图片的文件名
def filename(url):
	names = []
	try:	
		f = urllib2.urlopen(url, timeout=10).read()
		urllib.unquote(f)
		url_listen = URLLister()	
		url_listen.feed(f)	 
		names.extend(url_listen.names)
	except urllib2.URLError, e:	
		print e.reason	
	return names #zip(names, urls)

#下载图片	
def download_img(filenames, save_path, min_size):	
	print "download begin..."
	for im, i in zip(img, range(len(filenames))):
		fig = ["jpg", "JPG", "png", "PNG"]
		if im[-3:] not in fig:
			print "wrong url", i, filenames[i]
			continue		
		dist = os.path.join(save_path, filenames[i]+".jpg")	
		#此方式判断图片的大小太浪费了	
		#if len(urllib2.urlopen(im).read()) < min_size:	
		#	continue	
		#这种方式先拉头部，应该好多了，不用再下载一次	
		connection = urllib2.build_opener().open(urllib2.Request(im))	
		if int(connection.headers.dict['content-length']) < min_size:
			print "size are big", i, filenames[i]
			continue	
		urllib.urlretrieve(im, dist,None)	
		print "Done: ", i, filenames[i]	
	print "download end..."	

'''
url = "http://www.shanghaitech.edu.cn/faculty/slst/faculty.html"
positions = [s.decode("utf-8") for s in position(url)]
for i,j in zip(range(1, len(positions), 4), range(2, len(positions), 4)):
	print '_'.join([positions[j], positions[i]])
'''



if __name__ == "__main__":	
	#抓取图片首个页面	
	url = "http://www.shanghaitech.edu.cn/faculty/spst/faculty.html"
	#url = "http://www.shanghaitech.edu.cn/faculty/slst/faculty.html"	
	#图片保存路径	
	save_path = os.path.abspath("./downlaod")	
	if not os.path.exists(save_path):	
		os.mkdir(save_path)	
	#限制图片最小必须大于此域值	单位 B	
	min_size = 92	
	#遍历深度	
	max_depth = 2	
	#是否只遍历目标站内，即存在外站是否忽略	
	ignore_outer = True	
	main_site_domain = urlparse.urlsplit(url).netloc

	#filenames = [s.decode("utf-8") for s in filename(url)]
	#filenames = filename(url)

	filenames = []
	positions = [s.decode("utf-8") for s in position(url)]
	for i,j in zip(range(1, len(positions), 4), range(2, len(positions), 4)):
		filenames.append(('_'.join([positions[j], positions[i]])))
	
	get_page_html(url, max_depth, ignore_outer)	
	
	download_img(filenames, save_path, min_size)

