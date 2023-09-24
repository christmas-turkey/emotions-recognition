import os
from tensorflow.keras.callbacks import ModelCheckpoint
from ..config import save_path, checkpoint_filename

# Create a directory to save the model's weights
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Path to save the model's weights
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "checkpoint", checkpoint_filename)

# callback that saves the model's weights on each epoch
save_callback = ModelCheckpoint(filepath=path, save_weights_only=True, verbose=1)