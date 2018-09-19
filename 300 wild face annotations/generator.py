import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split

resize=100

direct='./combined'



listn=[]

data=[]
annot=[]
for filename in os.listdir(direct): 
	if(filename.split('.')[1]!='pts'):
   		listn.append(filename)
q=0
for k in listn:
	print(q)
	q+=1

	x=[]
	y=[]
	with open(direct+'/'+k.split('.')[0]+'.pts') as f:
	    annots= f.readlines()[3:-1]
	for i in annots:
		i=i.rstrip("\r\n")
		try:
			x1,y1=i.split(' ')
		except:
			print(k)
		x1=float(x1)
		y1=float(y1)
		x.append(x1)
		y.append(y1)

	image=cv2.imread(direct+'/'+k)
	resized_image = cv2.resize(image, (resize, resize))
	try:
		xs,ys,_=image.shape
	except:
		continue
	xscale=resize/xs
	yscale=resize/ys

	x2= [i * yscale for i in x]
	y2= [i * xscale for i in y]

	x22=np.array([x2,y2])



	data.append(resized_image)
	annot.append(x22)

print('data loaded......')

X=np.array(data)
Y=np.array(annot)

print('converted to array...........')

x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=42)


print('saving train test...............')
np.save('x_keypoints_train',x_train)

np.save('x_keypoints_test',x_test)

np.save('y_keypoints_test',y_test)
np.save('y_keypoints_train',y_train)

	
