import React, { useState } from 'react';

const AuthContext = React.createContext({
  token: null,
  isLoggedIn: false,
  login: (token) => {},
  logout: () => {},
});

export const AuthProvider = (props) => {
  const [token, setToken] = useState(localStorage.getItem('token'));
  const isLoggedIn = !!token;

  const loginHandler = (token) => {
    localStorage.setItem('token', token);
    setToken(token);
  };

  const logoutHandler = () => {
    localStorage.removeItem('token');
    setToken(null);
  };

  return (
    <AuthContext.Provider
      value={{
        token: token,
        isLoggedIn: isLoggedIn,
        login: loginHandler,
        logout: logoutHandler,
      }}
    >
      {props.children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
