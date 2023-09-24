from tensorflow import keras
from ..config import stop_on_accuracy

class Stop_accuracy(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy') is not None and logs.get('accuracy') > stop_on_accuracy):
            print(f"\nReached {stop_on_accuracy}% accuracy so cancelling training!")
            self.model.stop_training = True
            
stop_accuracy_callback = Stop_accuracy()
