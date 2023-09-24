const send_image = async (cameraRef : any, handler : any) => {

    if (cameraRef.current) {
      const canvas = document.createElement('canvas');
      const context = canvas.getContext('2d');

      canvas.width = cameraRef.current.videoWidth;
      canvas.height = cameraRef.current.videoHeight;

      if (context) {
        context.drawImage(cameraRef.current, 0, 0, canvas.width, canvas.height);
        canvas.toBlob(async (blob) => {
          if (blob) {
            const formData = new FormData();
            formData.append('image', blob, 'image.jpg'); // 'image.jpg' is the file name

            try {
              const response = await fetch('http://localhost:5000/api/image', {
                method: 'POST',
                body: formData,
              }).then((res) => res.json());
              handler(response["emotion"]);
              if (response) {
                console.log('Image sent successfully');
              } else {
                console.error('Failed to send image');
              }
            } catch (error) {
              console.error('Error sending image:', error);
            }
          }
        }, 'image/jpeg');
      }
    }
  };

  export default send_image;