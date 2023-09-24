from ModelService import ModelService
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

if __name__ == "__main__":
    print("main.py")
    model_service = ModelService()
    model = model_service.get_model()
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset/')
    train_dir = os.path.join(base_dir, 'train')
    validation_dir = os.path.join(base_dir, 'validation')

    train_datagen = ImageDataGenerator(rescale=1.0/255,
                                    #    rotation_range=30,
                                    #     width_shift_range=0.2,
                                    #     height_shift_range=0.2,
                                    #     shear_range=0.2,
                                    #     zoom_range=0.2,
                                    #     horizontal_flip=True
    )
    validation_datagen = ImageDataGenerator(rescale=1.0/255)

    train_generator = train_datagen.flow_from_directory(train_dir,
                                                        batch_size=128,
                                                        class_mode='categorical',
                                                        target_size=(48, 48),
                                                        color_mode='grayscale')
    validation_generator = validation_datagen.flow_from_directory(validation_dir,
                                                                    batch_size=64,
                                                                    class_mode='categorical',
                                                                    target_size=(48, 48),
                                                                    color_mode='grayscale')
    history = model_service.fit(epochs=100,
                                train_generator=train_generator,
                                validation_generator=validation_generator,
                                verbose=1)
    model_service.save()
    model_service.analytics(history, 'accuracy')
    model_service.analytics(history, 'loss')
    while True:
        img_path = input("Enter path to image: ")
        img = load_img(img_path, target_size=(48, 48), color_mode='grayscale')
        img = img_to_array(img)
        img = img.reshape(1, 28, 28, 1)
        img = img.astype('float32')
        img = img / 255.0
        prediction = model_service.predict(img)
        print("Predicted number is: " + str(np.argmax(prediction)))
    
