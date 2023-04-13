import React, { useContext } from 'react';

import { Redirect } from 'react-router-dom';
import AuthContext from "./AuthContext";
const Home = () => {
  const { isLoggedIn } = useContext(AuthContext);

  if (!isLoggedIn) {
    return <Redirect to="/login" />;
  }

  return (
    <div>
      <h1>Welcome to the Home Page</h1>
      <p>You are logged in!</p>
    </div>
  );
};

export default Home;
