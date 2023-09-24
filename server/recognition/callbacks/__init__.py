from .stop_on_accuracy import stop_accuracy_callback
from .save_weights import save_callback

class Callbacks():
    def __init__(self):
        self.callbacks = []
        self.callbacks.append(stop_accuracy_callback)
        self.callbacks.append(save_callback)

    def get_callbacks(self):
        return self.callbacks

callbacks = Callbacks().get_callbacks()