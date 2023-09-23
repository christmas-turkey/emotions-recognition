import React, { useEffect } from 'react'
import cls from './Camera.module.scss'


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
    <video ref={cameraRef} className={cls.camera} autoPlay muted></video>
  )
}

export default Camera