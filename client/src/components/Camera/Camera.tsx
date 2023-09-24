import React, { useEffect } from 'react'
import cls from './Camera.module.scss'
import send_image from './send_img'

const Camera: React.FC = () => {
  const cameraRef = React.useRef<HTMLVideoElement>(null)

  useEffect(() => {
    if (cameraRef.current) {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
          if (cameraRef.current) {
            cameraRef.current.srcObject = stream
          }
        })
        .catch(err => {
          console.error(err)
        })
    }
  }, [])

  return (
    <div>
    <video ref={cameraRef} className={cls.camera} autoPlay muted></video>
    <button onClick={(e) => {send_image(e, cameraRef)}} className={cls.btn_send}>Send Image</button>
    </div>
  )
}

export default Camera