import React from 'react';
import Register from './Auth/Register';
import Login from './Auth/Login';
import { useState } from 'react';
import './HomeAuth.css'

const HomeAuth = () => {
    const [login, setLogin] = useState(true);
    const [regis, setRegister] = useState(false);

    const handleLogs = () => {
        setLogin(true);
        setRegister(false);
    };

    const handleRegis = () => {
        setRegister(true);
        setLogin(false);
    };

    return (
        <div className='home-auth'>
            <div className='home-content'>
                <div className='buttons-auth'>
                            
                    <button onClick={handleRegis}>Register</button>
                    <button onClick={handleLogs}>Login</button>
                    
                </div>
                <div className='form'>

                    {regis && <Register/>}
                    {login && <Login/>}
                    
                </div>
            </div>
            
        
        </div>
        

        
    );
};

export default HomeAuth;
