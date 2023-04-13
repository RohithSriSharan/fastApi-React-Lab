import React, { useContext } from 'react';

import { Redirect } from 'react-router-dom';
import AuthContext from "./AuthContext";
const Home = () => {
  const { isLoggedIn } = useContext(AuthContext);
  const { logout } = useContext (AuthContext);

  const handleLogout = ()  =>{
    logout()
  }

  if (!isLoggedIn) {
    return <Redirect to="/login" />;
  }else{

    return (
        <div>
          <h1>Welcome to the Home Page</h1>
          <p>You are logged in!</p>
          <button onClick={handleLogout}>Log Out</button>
        </div>
      );

  }
 

 
};

export default Home;
