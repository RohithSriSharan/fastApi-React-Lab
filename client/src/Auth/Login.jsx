import React, { useState, useContext } from "react";
import { Redirect } from "react-router-dom";
import AuthContext from "./AuthContext";

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
    console.log(data);
    auth.login(data.access_token);
    setRedirectToHome(true);
  };

  if (redirectToHome) {
    return <Redirect to="/home" />;
  }

  return (
    <div>
      <h1>Login</h1>
      <form>
        <label>Username</label>
        <input
          type="text"
          name="username"
          value={form.username}
          onChange={handleChange}
        />
        <br />
        <label>Password</label>
        <input
          type="password"
          name="password"
          value={form.password}
          onChange={handleChange}
        />
        <br />
        <input type="submit" onClick={handleSubmit} />
      </form>
    </div>
  );
};

export default Login;
