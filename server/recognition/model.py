import tensorflow.keras.layers as layers
import tensorflow.keras.models as models

model = models.Sequential([
    layers.Conv2D(64, (3, 3),input_shape=(48,48,1) , activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dropout(0.4),
    layers.Dense(512, activation='relu'), 
    layers.Dense(3, activation='softmax')
])