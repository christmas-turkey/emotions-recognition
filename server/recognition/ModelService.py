import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from .model import model
from .extern_model import extern_model
from .callbacks import callbacks
from .config import save_path, extern_model_name
import matplotlib.pyplot as plt
import sys
import os

class ModelService:
    def __init__(self, metrics=['accuracy']):
        self.model = model
        self.model.compile(optimizer=RMSprop(learning_rate=1e-4),
              loss='categorical_crossentropy',
              metrics=metrics)

    def get_model(self):
        return self.model
    
    def predict(self, image):
        return self.model.predict(image)
    
    def fit(self, epochs=5, train_generator=None, validation_generator=None, verbose=1):
        return self.model.fit(train_generator,
                              epochs=epochs,
                              validation_data=validation_generator,
                              verbose=verbose,
                              callbacks=callbacks)
    
    def save(self):
        print("Saving weights to " + save_path)
        self.model.save(save_path)

    def load(self):
        print("Which model to use?")
        print(f"Extern model({extern_model_name}) 0")
        print(f"Own model({save_path}) 1")
        choice = int(input("Your choice: "))
        if choice == 0:
            print(f"Loading weights from {extern_model_name}")
            self.model = extern_model
            self.model.load_weights(os.path.join(os.path.dirname(__file__), extern_model_name))
        elif(choice == 1):
            print("Loading weights from " + save_path)
            self.model = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__), save_path))
        else:
            sys.exit(0)

    def analytics(self, history, string):
        plt.plot(history.history[string])
        plt.plot(history.history['val_'+string])
        plt.xlabel("Epochs")
        plt.ylabel(string)
        plt.legend([string, 'val_'+string])
        plt.show()

        
