import os
import warnings
warnings.filterwarnings("ignore")
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 数据所在文件夹
base_dir = './data/cats_and_dogs'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

# 训练集
train_cats_dir = os.path.join(train_dir, 'cats')
train_dogs_dir = os.path.join(train_dir, 'dogs')

# 验证集
validation_cats_dir = os.path.join(validation_dir, 'cats')
validation_dogs_dir = os.path.join(validation_dir, 'dogs')

model = tf.keras.models.Sequential([
    #如果训练慢，可以把数据设置的更小一些
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(64, 64, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    
    #为全连接层准备
    tf.keras.layers.Flatten(),
    
    tf.keras.layers.Dense(512, activation='relu'),
    # 二分类sigmoid就够了
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.summary()

model.compile(loss='binary_crossentropy',
              optimizer=Adam(lr=1e-4),
              metrics=['acc'])

train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        train_dir,  # 文件夹路径
        target_size=(64, 64),  # 指定resize成的大小
        batch_size=20,
        # 如果one-hot就是categorical，二分类用binary就可以
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        validation_dir,
        target_size=(64, 64),
        batch_size=20,
        class_mode='binary')

# import os
# from PIL import Image
# folder_path = r''  #写入你图片所在的文件夹，即包含该图片的文件夹
# extensions = []
# for filee in os.listdir(folder_path):
#     file_path = os.path.join(folder_path, filee)
#     print('** Path: {}  **'.format(file_path), end="\r", flush=True)
#     im = Image.open(file_path)
#     rgb_im = im.convert('RGB')
#     if filee.split('.')[1] not in extensions:
#         extensions.append(filee.split('.')[1])



# history = model.fit_generator(
#       train_generator,
#       steps_per_epoch=100,  # 2000 images = batch_size * steps
#       epochs=20,
#       validation_data=validation_generator,
#       validation_steps=50,  # 1000 images = batch_size * steps
#       verbose=2)

history = model.fit(
      train_generator,
      steps_per_epoch=100,  # 2000 images = batch_size * steps
      epochs=20,
      validation_data=validation_generator,
      validation_steps=50,  # 1000 images = batch_size * steps
      verbose=2)

import matplotlib.pyplot as plt
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training Loss')
plt.plot(epochs, val_loss, 'b', label='Validation Loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()



import numpy as np
from tensorflow.keras.preprocessing import image

def predict_image(model, img_path):
    # 加载并预处理图片
    img = image.load_img(img_path, target_size=(64, 64))
    img_tensor = image.img_to_array(img)  # 转换为数组
    img_tensor = np.expand_dims(img_tensor, axis=0)  # 增加批次维度
    img_tensor /= 255.  # 归一化到 [0,1]

    # 预测图片
    prediction = model.predict(img_tensor)
    # 因为使用了sigmoid激活函数，输出在0到1之间，通常0.5是分类阈值
    if prediction < 0.5:
        return "Cat"  # 猫
    else:
        return "Dog"  # 狗

# 调用函数
img_path = 'cat1.jpg'  # 指定要预测的图片路径
result = predict_image(model, img_path)
print(f'The image is a {result}.')


import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image

def predict_and_show_image(model, img_path):
    # 加载并预处理图片
    img = image.load_img(img_path, target_size=(64, 64))
    img_tensor = image.img_to_array(img)  # 转换为数组
    img_tensor = np.expand_dims(img_tensor, axis=0)  # 增加批次维度
    img_tensor /= 255.  # 归一化到 [0,1]

    # 预测图片
    prediction = model.predict(img_tensor)
    predicted_class = "Dog" if prediction >= 0.5 else "Cat"
    
    # 显示图片和预测结果
    plt.imshow(image.load_img(img_path))
    plt.title(f'Prediction: {predicted_class}')
    plt.axis('off')  # 关闭坐标轴
    plt.show()

# 调用函数
img_path = 'cat1.jpg'  # 指定要预测的图片路径
predict_and_show_image(model, img_path)


import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image

def predict_image(model, img_path):
    # 加载并预处理图片
    img = image.load_img(img_path, target_size=(64, 64))
    img_tensor = image.img_to_array(img)  # 转换为数组
    img_tensor = np.expand_dims(img_tensor, axis=0)  # 增加批次维度
    img_tensor /= 255.  # 归一化到 [0,1]

    # 预测图片
    prediction = model.predict(img_tensor)
    return "Dog" if prediction >= 0.5 else "Cat"

def predict_and_show_images(model, folder_path):
    # 遍历文件夹中的所有图片文件
    for img_file in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_file)
        if img_path.lower().endswith((".png", ".jpg", ".jpeg")):  # 确保处理图片文件
            # 预测图片
            predicted_class = predict_image(model, img_path)
            
            # 显示图片和预测结果
            img = image.load_img(img_path)
            plt.imshow(img)
            plt.title(f'Prediction: {predicted_class}')
            plt.axis('off')  # 关闭坐标轴
            plt.show()

# 指定要预测的图片文件夹路径
folder_path = 'D:\\anli\\tensorflow\\cat_dog\\data\\cats_and_dogs\\validation\\cats'
predict_and_show_images(model, folder_path)


import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image

def predict_image(model, img_path):
    # 加载并预处理图片
    img = image.load_img(img_path, target_size=(64, 64))
    img_tensor = image.img_to_array(img)  # 转换为数组
    img_tensor = np.expand_dims(img_tensor, axis=0)  # 增加批次维度
    img_tensor /= 255.  # 归一化到 [0,1]

    # 预测图片
    prediction = model.predict(img_tensor)
    return "Dog" if prediction >= 0.5 else "Cat"

def predict_and_show_images(model, folder_path):
    # 获取文件夹内所有图片文件
    files = [f for f in os.listdir(folder_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    num_files = len(files)
    num_columns = 4
    num_rows = (num_files + num_columns - 1) // num_columns  # 确保有足够的行

    plt.figure(figsize=(num_columns * 4, num_rows * 4))  # 调整整体图形窗口的大小

    # 遍历文件夹中的所有图片文件
    for index, img_file in enumerate(files):
        img_path = os.path.join(folder_path, img_file)
        predicted_class = predict_image(model, img_path)
        img = image.load_img(img_path)
        plt.subplot(num_rows, num_columns, index + 1)
        plt.imshow(img)
        plt.title(f'Prediction: {predicted_class}')
        plt.axis('off')  # 关闭坐标轴

    plt.tight_layout()
    plt.show()

# 指定要预测的图片文件夹路径
folder_path = r'D:\anli\tensorflow\cat_dog\data\cats_and_dogs\validation\cats'
predict_and_show_images(model, folder_path)


from tensorflow.keras.preprocessing import image
import numpy as np

def predict_image(model, img_path):
    # 加载图片并调整大小以匹配模型的输入要求
    img = image.load_img(img_path, target_size=(64, 64))
    img_array = image.img_to_array(img)  # 将图片转换为数组
    #img_array = np.expand_dims(img_array, axis=0)  # 增加一个维度，因为模型预期的是批量数据
    img_array /= 255.0  # 归一化到[0,1]区间

    # 使用模型进行预测
    prediction = model.predict(img_array)

    # 判断预测值，将其转换为具体的类别
    if prediction[0] < 0.5:
        return "Cat"
    else:
        return "Dog"

# 假设模型已经加载，并且您有一个图片路径可以传入
img_path = 'cat1.jpg'
result = predict_image(model, img_path)
print(f"The image is a {result}.")








