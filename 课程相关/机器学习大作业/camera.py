import tensorflow as tf
import tensorflow.keras as keras
import time

#conv_base = keras.applications.VGG16(weights="imagenet", include_top="True", input_shape=(224, 224, 3))
# net=keras.Sequential()
# net.add(conv_base)
# net.add(keras.layers.Softmax)
net=keras.models.load_model("kkk.h5")
import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # 我的摄像头位置是700
cv2.waitKey(5)  # 等待5ms

while cap.isOpened():  # 也可以是 while True
	ok, img = cap.read()
	if ok:  # 若读取到图像再进行显示
		cv2.imshow('winName', img)
		temp=cv2.resize(img,dsize=(150,150))
		temp = np.array(temp)
		temp=np.reshape(temp,[1,150,150,3])
		temp=tf.cast(temp,dtype="float32")
		k=net.predict(temp)
		k=tf.argmax(k,axis=1)
		k=tf.squeeze(k)
		if (int(k)==0):
			print("剪刀")
		elif(int(k)==1):
			print("手机")
		else:
			print("水杯")

	if cv2.waitKey(5) == ord('q'):  # 等到5ms检测是否退出，同时防止读取太快
		cv2.destroyWindow('winName')
		break

cap.release()
