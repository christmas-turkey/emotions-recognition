import React, { useEffect, useState } from 'react'
import cls from './Camera.module.scss'
import send_image from './send_img'

const Camera = ({handler} : any) => {
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
    const interval = setInterval(() => {
        send_image(cameraRef, handler)
    }, 500)
      return () => clearInterval(interval)
  }, [])

  return (
    <div>
    <video ref={cameraRef} className={cls.camera} autoPlay muted></video>
    {/* <button onClick={(e) => {setEmo(e)}} className={cls.btn_send}>Send Image</button> */}
    </div>
  )
}

export default Camera