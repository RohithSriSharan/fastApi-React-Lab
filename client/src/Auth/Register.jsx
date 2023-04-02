import React from 'react'
import './Register.css'
import {useState, useEffect} from 'react'

const Register = () => {
  const [registerform, setRegisterForm] = useState({
    email:'',
    password:''
  })
  const handleChange = (event) =>{
    const {name, value} = event.target;
    setRegisterForm({ ...registerform, [name]:value})
  }

  const handleSubmit = async(e) =>{
    e.preventDefault();
    const response = await fetch('http://127.0.0.1:8000/register',{
      method:'POST',
      headers:{'Content-Type': 'application/json'},
      body: JSON.stringify(registerform)
    });
    const data = await response.json();
    console.log(data)
  }
    
  return (
    <div>
    <h1>Register</h1>
    <form>
        <label>Email</label>
        <input type='text' value={registerform.email} name='email' onChange={handleChange} required></input>
        <br></br>
        <label>Password</label>
        <input type='text' value={registerform.password} name='password' onChange={handleChange} required></input>
        <br></br>
        <button type='submit' onClick={handleSubmit}>Submit</button>
    </form>
    </div>
  )
}

export default Register