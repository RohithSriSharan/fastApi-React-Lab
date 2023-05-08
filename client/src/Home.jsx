import React, { useContext, useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { Redirect } from 'react-router-dom';
import AuthContext from "./Auth/AuthContext";
import Pagination from './Pagination';
import './Home.css'


import { BsBasket3Fill } from 'react-icons/bs';
import {VscHubot } from 'react-icons/vsc';

import { MdOutlineAddShoppingCart } from 'react-icons/md';

const Home = () => {
  const { isLoggedIn } = useContext(AuthContext);
  const { logout } = useContext (AuthContext);
  const [products, setProducts] = useState([]);
  const [query, setQuery] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const [itemsPerPage, setItemsPerPage] = useState(10);

  const handleQuery = (e) => {
    setQuery(e.target.value);
  };

  const handleLogout = ()  => {
    logout();
  };

  const handleSearch = async(e) => {
    e.preventDefault();
    const response = await fetch("http://127.0.0.1:8000/query", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({"search": query})
    })
    const data = await response.json();
    
      setProducts(data)
    
     
  }
  const handleAddToBasket = async (product) =>{
    console.log("Adding to basket")
    fetch("http://localhost:8000/addtobasket",{
      method:'POST',
      headers:{
        'Content-Type':'application/json'
      },
      body:JSON.stringify(product)
    })
  }
  
  
  const lastItemIndex = currentPage * itemsPerPage;
  const firstItemIndex = lastItemIndex - itemsPerPage;
  const currentItems = products.slice(firstItemIndex, lastItemIndex);

  console.log(products)

  
  
  if (!isLoggedIn) {
    return <Redirect to="/login" />;
  } else {
    return (
      <div>
        <div><button onClick={handleLogout}>Log Out</button></div>
            <div className='home-header'>
              <form className='search-form' onSubmit={handleSearch}>
                <input type='text' value={query} onChange={handleQuery} required/>
                <button type='submit'>Search</button>
              </form>
              <div>
                <a href='/basket'><button className='basket'><BsBasket3Fill/></button></a>
                <a href='/davinci'><button className='basket'><VscHubot/></button></a>
              </div>
              
              
            </div>
            <div className='search-products'>
              <ul >
              {currentItems.map((product) => (
                <div id="product" key={product.id}>
                  <Link className='search-link' to={`/search/${product.tag}/${product.id}`} target="_blank">
                    <li>
                      
                      <img src={product.image}></img>
                      <h3>{product.name}</h3>
                      <p className='search-price'>{product.actual_price}</p>
                      
                      
                      
                      
                    </li>
                  </Link>
                  <button onClick={() => handleAddToBasket(product)}><MdOutlineAddShoppingCart/></button>
                </div>
            ))}
            
            </ul>
            </div>
          
        <div>
        
          <Pagination className="pagination" totalPosts={products.length} postsPerPage={itemsPerPage} setCurrentPage={setCurrentPage} />
        </div>
        
      </div>
    );
  }
};

export default Home;
