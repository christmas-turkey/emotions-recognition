from flask import request, jsonify
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from datetime import datetime
# IMAGE SETTINGS
height = 480
width = 640
channels = 3

def routes(app):
    @app.route('/api/image', methods=['POST'])
    def process_image():
        if 'image' not in request.files:
            return jsonify({'error': 'No image part'})

        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file:
            # Display the image on the server
            current_time = datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
            image_data = file.read()
            image_buffer = BytesIO(image_data)
            image = plt.imread(image_buffer, format='jpg')
            plt.figure(num=f'Image {current_time}')
            plt.imshow(image)
            plt.axis('off')
            plt.show()

        # Return a response
        return jsonify({'message': 'Image uploaded and processed successfully'})