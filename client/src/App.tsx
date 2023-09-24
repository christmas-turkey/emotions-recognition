import React, { useState } from 'react';
import Camera from './components/Camera/Camera';


function App() {
  const [emotion, setEmotion] = useState('idk')
  return (
    <div className='content'>
      <h1 className='title'>Emotions recognition 😀😐😡</h1>
      <Camera handler={setEmotion} />
      <h2 className='output'>{emotion}</h2>
    </div>
  );
}

export default App;
