import React from 'react';
import Camera from './components/Camera/Camera';


function App() {
  return (
    <div className='content'>
      <h1 className='title'>Emotions recognition 😀😐😡</h1>
      <Camera />
      <h2 className='output'>Agressive 😡</h2>
    </div>
  );
}

export default App;
