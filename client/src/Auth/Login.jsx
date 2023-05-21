import React, { useState, useContext } from "react";
import { Redirect } from "react-router-dom";
import AuthContext from "./AuthContext";
import { FaUserAlt } from 'react-icons/fa';
import { HiLockClosed } from 'react-icons/hi';
import './Login.css'
const Login = () => {
  const auth = useContext(AuthContext);

  const [form, setForm] = useState({
    username: "",
    password: "",
  });

  const [redirectToHome, setRedirectToHome] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://localhost:8000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(form),
    });
    const data = await response.json();
 
    auth.login(data.access_token);
    setRedirectToHome(true);
  };

  if (redirectToHome) {
    return <Redirect to="/home" />;
  }
  

  return (
    <div className="login">
 
      <form>
          <div className="login-email">
          <label><FaUserAlt/></label>
            <input
              type="email"
              name="username"
              value={form.username}
              onChange={handleChange}
              autoComplete="current-user"
              placeholder="Username"
              required
            />
            </div>
        
          <div className="login-password">
          <label><HiLockClosed/></label>
          <input
            type="password"
            name="password"
            value={form.password}
            onChange={handleChange}
            autoComplete="current-password"
            required
            placeholder="Password"
          />    
          </div>
          <div>
          
          <button className="login-button" type="submit" onClick={handleSubmit}>Login</button>
          </div>
      </form>
      
    </div>
  );
};

export default Login;
