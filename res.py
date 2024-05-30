import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# 加载预训练的ResNet模型
model = ResNet50(weights='imagenet')

# 定义要进行识别的图像路径
image_path = 'flowers/8.jpg'

# 加载图像并进行预处理
img = image.load_img(image_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# 进行植物识别预测
preds = model.predict(x)
predicted_labels = decode_predictions(preds, top=3)[0]

# 打印识别结果
for _, label, probability in predicted_labels:
    print(label, ':', probability)
