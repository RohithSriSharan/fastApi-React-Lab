import './App.css';

import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Login from '../src/Auth/Login.jsx'
import Register from './Auth/Register';
import Home from './Home';
import { AuthProvider } from './Auth/AuthContext';
import FashionWomenInfo from './Products/FashionWomenInfo';
import FashionWomen from './Products/FashionWomen';

import SearchProductInfo from './SearchProductInfo';
import davinci from './Davinci/davinci';
import Basket from './Basket/Basket';
import HomeAuth from './HomeAuth';


function App() {

  return (
    <AuthProvider>
      <Router>
        <Switch>
     
          <Route path="/home" component={Home} />
         
          <Route path='/women-fashion' component={FashionWomen}/>
          <Route path="/product/:id" component={FashionWomenInfo} />
          <Route path="/search/:tag/:id" component={SearchProductInfo}/>
          <Route  path="/davinci" component={davinci}></Route>
          <Route  path="/basket" component={Basket}></Route>
          <HomeAuth/>
        </Switch>
      </Router>
    </AuthProvider>
  
  );
}

export default App;
