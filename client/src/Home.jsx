import React, { useContext, useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Redirect } from 'react-router-dom';
import AuthContext from "./Auth/AuthContext";
const Home = () => {
  const { isLoggedIn } = useContext(AuthContext);
  const { logout } = useContext (AuthContext);
  const[ products, setProducts] = useState([])
  const [query, setQuery] = useState("")

  const handleQuery = (e) =>{
    setQuery(e.target.value)
  }

  const handleLogout = ()  =>{
    logout()
  }

  const handleSearch = async(e) => {
    e.preventDefault();
    fetch("http://127.0.0.1:8000/query", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({"search": query})
 
    })
    
    .then(response => response.json())
    .then(data => {
      console.log(data)
      setProducts(data)
    })
    .catch(error => console.log(error))
  }






  if (!isLoggedIn) {
    return <Redirect to="/login" />;
  }else{

    return (
        <div>
              <div><button onClick={handleLogout}>Log Out</button></div>
                <div>
                  <form onSubmit={handleSearch} >
                    <input type='text'  value={query} onChange={handleQuery}></input>
                    <button type='submit'>Search</button>
                  </form>
                  
                </div>
                    {Object.keys(products).map((category, index) => (
                      <div key={index}>
                        
                     
                        {JSON.parse(products[category]).map((product, index) => (
                          <Link to={`/search/`+ product.id}>
                              <div key={index}>
                              <h3>{product.name}</h3>
                              <p>{product.description}</p>
                              <img src={product.image}></img>
                              <p>Price: {product.actual_price}</p>
                            </div>
                          </Link>
                          
                        ))}
                  </div>
                ))}
                <div>

                </div>
          <div>
          
        </div>
          
          
          
        </div>
      );

  }
 

 
};

export default Home;
