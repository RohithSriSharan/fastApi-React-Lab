import './App.css';
import { useState, useEffect, useContext } from 'react'
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom';

import Login from '../src/Auth/Login.jsx'
import Register from './Auth/Register';
import Home from './Auth/Home';
import { AuthProvider, AuthContext } from './Auth/AuthContext';


function App() {

  return (
    <AuthProvider>
      <Router>
        <Switch>
          
          <Route path="/home" component={Home} />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Redirect from="/" to="/login" />
        </Switch>
      </Router>
    </AuthProvider>
  );
}

export default App;
