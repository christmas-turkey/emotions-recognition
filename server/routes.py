from flask import request, jsonify
from recognition.predict import crop_and_predict

def routes(app):
    @app.route('/api/image', methods=['POST'])
    def process_image():
        if 'image' not in request.files:
            return jsonify({'error': 'No image part'})

        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file:
            image_data = file.read()
            return {"emotion" : crop_and_predict(image_data)}

        # Return a response
        return jsonify({'message': 'Error'})