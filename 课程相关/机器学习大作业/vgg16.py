import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
import os, shutil

from keras_preprocessing.image import ImageDataGenerator

base_d = "D:/cat_vs_dog"
# os.mkdiniddr(base_d)
train_d = os.path.join(base_d, "train")
val_d = os.path.join(base_d, "val")
test_d = os.path.join(base_d, "test")
# os.mkdir(train_d)
# os.mkdir(test_d)
# os.mkdir(val_d)

train_cat_d = os.path.join(train_d, "cat")
val_cat_d = os.path.join(val_d, "cat")
test_cat_d = os.path.join(test_d, "cat")

train_dog_d = os.path.join(train_d, "dog")
val_dog_d = os.path.join(val_d, "dog")
test_dog_d = os.path.join(test_d, "dog")

# os.mkdir(train_dog_d)
# os.mkdir(test_dog_d)
# os.mkdir(val_dog_d)
#
# os.mkdir(train_cat_d)
# os.mkdir(test_cat_d)
# os.mkdir(val_cat_d)

# for i in range(2000):
# 	f=r"D:\浏览器下载\dogs-vs-cats\train"
# 	s=os.path.join(f,"cat."+str(i)+".jpg")
# 	if (i<1000):
# 		dst=os.path.join(train_cat_d,"cat."+str(i)+".jpg")
# 		shutil.copyfile(s,dst)
# 	elif (i<1500):
# 		dst=os.path.join(val_cat_d,"cat."+str(i)+".jpg")
# 		shutil.copyfile(s,dst)
# 	else:
# 		dst = os.path.join(test_cat_d, "cat." + str(i) + ".jpg")
# 		shutil.copyfile(s, dst)
#
# for i in range(2000):
# 	f=r"D:\浏览器下载\dogs-vs-cats\train"
# 	s=os.path.join(f,"dog."+str(i)+".jpg")
# 	if (i<1000):
# 		dst=os.path.join(train_dog_d,"dog."+str(i)+".jpg")
# 		shutil.copyfile(s,dst)
# 	elif (i<1500):
# 		dst=os.path.join(val_dog_d,"dog."+str(i)+".jpg")
# 		shutil.copyfile(s,dst)
# 	else:
# 		dst = os.path.join(test_dog_d, "dog." + str(i) + ".jpg")
# 		shutil.copyfile(s, dst)

net = keras.applications.VGG16(include_top=False, weights="imagenet", input_shape=(150, 150, 3))
model = keras.models.Sequential()
model.add(net)
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(256, activation="relu"))
model.add(keras.layers.Dense(3, activation="softmax"))
net.trainable = False
model.summary()

train_datagen = ImageDataGenerator(
	rescale=1. / 255,
	rotation_range=40,
	width_shift_range=0.2,
	height_shift_range=0.2,
	shear_range=0.2,
	zoom_range=0.2,
	horizontal_flip=True,
	fill_mode='nearest')
train_generator = train_datagen.flow_from_directory(
	"train",
	target_size=(150, 150),
	batch_size=64,
	class_mode="categorical"
)
test_datagen = ImageDataGenerator(rescale=1. / 255)
validation_generator = test_datagen.flow_from_directory(
	"validation",
	target_size=(150, 150),
	batch_size=64,
	class_mode='categorical')
model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.RMSprop(lr=2e-5),
              metrics=['acc'])
history = model.fit(
	train_generator,
	epochs=100,
	validation_data=validation_generator)

model.save("kkk.h5")

import matplotlib.pyplot as plt
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()
