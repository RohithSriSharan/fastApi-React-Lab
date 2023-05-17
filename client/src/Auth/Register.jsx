import React from 'react'
import './Register.css'
import {useState } from 'react'


import { FaUserAlt } from 'react-icons/fa';
import { HiLockClosed } from 'react-icons/hi';

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
    <div className='register'> 
    
      <form>
        <div className='register-email'>
        <label><FaUserAlt/></label>   
          <input type='email' placeholder='Email' value={registerform.email} name='email' onChange={handleChange} autoComplete='current_email' required></input>
        </div>
        
        
        <div className='register-password'>   
        <label><HiLockClosed/></label> 
          <input type='password' value={registerform.password} name='password' placeholder='Password' onChange={handleChange} autoComplete='current_password' required></input>
        </div>
        
    
        <button className='register-button' type='submit' onClick={handleSubmit} >Create Account</button>
    </form>
   
    </div>
  )
}

export default Register


