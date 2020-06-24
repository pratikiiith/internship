import struct
from struct import unpack
import os

def unpack_drawing(file_handle):
    key_id, = unpack('Q', file_handle.read(8))
    country_code, = unpack('2s', file_handle.read(2))
    recognized, = unpack('b', file_handle.read(1))
    timestamp, = unpack('I', file_handle.read(4))
    n_strokes, = unpack('H', file_handle.read(2))
    image = []
    for i in range(n_strokes):
        n_points, = unpack('H', file_handle.read(2))
        fmt = str(n_points) + 'B'
        x = unpack(fmt, file_handle.read(n_points))
        y = unpack(fmt, file_handle.read(n_points))
        image.append((x, y))

    return {
        'key_id': key_id,
        'country_code': country_code,
        'recognized': recognized,
        'timestamp': timestamp,
        'image': image
    }


def unpack_drawings(filename):
    with open(filename, 'rb') as f:
        while True:
            try:
                yield unpack_drawing(f)
            except struct.error:
                break

# f = open('myfile.txt','w')
print("Input directory path of 2d data")
rootdir = input()
print("Input directory path to store txt files")
final = input()

l=[]
count=0
for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		filepath = subdir + "/" + file
		count=count+1
		if filepath.endswith(".bin"):
			print(filepath)
			print("Creating txt")
			f=open(final + "/" + str(count)+".txt","a")
			stroke=1
			for drawing in unpack_drawings(filepath):
			# do something with the drawing
				for x in drawing['image']:
					print(x)
					break
					stroke=stroke+1
					for i in range(len(x[0])):
						f.write(str(x[0][i]))
						f.write(" ")
						f.write(str(x[1][i]))
						if(i!=len(x[0])-1):
							f.write(" ")
					if(stroke>10000):
						break
					f.write("\n")
				if(stroke>10000):
					break
			f.close()
