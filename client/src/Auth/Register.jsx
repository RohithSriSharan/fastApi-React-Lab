import React from 'react'
import './Register.css'
import {useState } from 'react'

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
  const isFormValid = registerform.email !== '' && registerform.password !== ''

  return (
    <div>
    <h1>Register</h1>
    <form>
        <label>Email</label>
        <input type='email' value={registerform.email} name='email' onChange={handleChange} autoComplete='current_email' required></input>
        <br></br>
        <label>Password</label>
        <input type='password' value={registerform.password} name='password' onChange={handleChange} autoComplete='current_password' required></input>
        <br></br>
        <button type='submit' onClick={handleSubmit} disabled={!isFormValid} >Submit</button>
    </form>
    <a href="/login"><button>Login</button></a>
    </div>
  )
}

export default Register


