import './App.css';

import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Login from '../src/Auth/Login.jsx'
import Register from './Auth/Register';
import Home from './Auth/Home';
import { AuthProvider } from './Auth/AuthContext';
import FashionWomenInfo from './Products/FashionWomenInfo';
import FashionWomen from './Products/FashionWomen';

function App() {

  return (
    <AuthProvider>
      <Router>
        <Switch>
          
          <Route path="/home" component={Home} />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path='/women-fashion' component={FashionWomen}/>
          <Route path="/product/:id" component={FashionWomenInfo} />
        </Switch>
      </Router>
    </AuthProvider>
  );
}

export default App;
