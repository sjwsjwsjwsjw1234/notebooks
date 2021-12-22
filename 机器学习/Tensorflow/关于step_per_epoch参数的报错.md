## 使用tensorflow的ImageGenerator迭代器加载图片时遇到如下错误


> WARNING:tensorflow:Your input ran out of data; interrupting training. Make sure that your dataset or generator can generate at least `steps_per_epoch * epochs` batches (in this case, 50 batches). You may need to use the repeat() function when building your dataset.

代码如下
```python
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
	batch_size=32,
	class_mode="categorical"
)
history = model.fit(
	train_generator,
	steps_per_epoch=100,
	epochs=100,
	validation_data=validation_generator,
	validation_steps=50)
```

问题出在了`steps_per_epoch=100`这个参数上，这个参数指定的是每一个epoch包含的step数，因为在generator中已经指定了`batch_size=32`因此step_per_epoch应该等于len(train)/batch_size,在这里应该是 1530/32=48。或者不指定s_p_e这个参数，这样的话，tensorflow会自动计算。