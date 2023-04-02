
import './App.css';
import {useState, useEffect} from 'react'

function App() {
  const [data, setData] = useState('')

 
  
  return (
    <div className="App app">
      {data&&(
        <h1>{data.name}</h1>

      )}
      <button >Register</button>
      <button>Login</button>

      
    </div>
  );
}

export default App;
