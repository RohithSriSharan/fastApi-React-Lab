import React, { useState } from 'react'

const Home = () => {
    const token = localStorage.getItem('access_token');
    const [home, setHome] = useState('')
    const handleHome = async(e) =>{
        e.preventDefault()
        const response = await fetch("http://localhost:8000/home",{
            method: 'GET',
            headers: {
              'Authorization': `Bearer ${token}`
            }
        })
        .then(response => response.json())
        .then(data => setHome(data))
        .catch(error => console.log(error))
    }
    
  return (
    <div>Home

    <h1>{home}</h1>
    <button onClick={handleHome}>Home</button>
    
    </div>
        
  ) 
}

export default Home