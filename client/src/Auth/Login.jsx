import React from 'react'
import './Login.css'
import { useState, useEffect } from 'react'
import Home from './Home'
const Login = () => {
   
  
    const [form, setForm] = useState({
      username:'',
      password: '',
    })
  
    const handleChange = (e) =>{
      const {name, value} = e.target;
      setForm({ ...form , [name]:value});
  
    }
  
   
  
  
    const handleSubmit =async (e) =>{
      e.preventDefault();
      const response =  await fetch("http://localhost:8000/login",{
        method:'POST',
        headers:{
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(form),
      });
      const data = await response.json();
      console.log(data)
    }
   
  return (
    <div>
    <h1>Login</h1>
          <from  >
            <label>Username</label>
            <input type='text' name='username' value={form.username} onChange={handleChange}></input>
            <br></br>
            <label>Password</label>
            <input type='password' name='password' value={form.password} onChange={handleChange} ></input>
            <br></br>
            <input type='submit' onClick={handleSubmit}></input>
          </from>
        <Home/>
      </div>
  )
}

export default Login