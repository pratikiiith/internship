import os
import time
k=0
f = open("cate","r")
path = "https://storage.googleapis.com/quickdraw_dataset/full/binary/"
c= ' '
for i in f:
	if(c in i):
		i=i.replace(" ","%20")
	i=i[:-1]+".bin"
	path1 = path + str(i)
	print(path1)
	os.system(f"wget {path1}")
	if(k==20):
		break
	k=k+1
	# https://storage.googleapis.com/quickdraw_dataset/full/binary/airplane.bin