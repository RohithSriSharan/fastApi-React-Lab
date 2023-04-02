import './App.css';
import {useState, useEffect} from 'react'
import Login from '../src/Auth/Login.jsx'
import Register from './Auth/Register';

function App() {
    const [login, setlogin] = useState(true)
    const [register, setRegister] = useState(false)

  const handleLogin = () =>{
    setlogin(true)
    setRegister(false)
   
  }
  const handleRegister = () =>{
    setRegister(true)
    setlogin(false)
  }

  return (
    <div className="App app">
      <button onClick={handleLogin}>Login</button>
      <button onClick={handleRegister} >Register</button>
      { login?(<div><Login/></div>): (<div><Register/></div>)}
    </div>
  );
}

export default App;
