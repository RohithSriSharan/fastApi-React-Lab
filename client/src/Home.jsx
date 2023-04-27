import React, { useContext, useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { Redirect } from 'react-router-dom';
import AuthContext from "./Auth/AuthContext";
import Pagination from './Pagination';


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
            <div>
              <form onSubmit={handleSearch}>
                <input type='text' value={query} onChange={handleQuery} />
                <button type='submit'>Search</button>
              </form>
            </div>
            <ul>
                {currentItems.map((product) => (
                  <Link to={`/search/${product.tag}/${product.id}`} target="_blank" key={product.id}>
                      <li >
                        <h3>{product.name}</h3>
                        <p>{product.description}</p>
                        <img src={product.image}></img>
                        <p>Price: {product.actual_price}</p>
                        <p>category: {product.sub_category}</p>
                        <p>category_id: {product.id}</p>
                        <p>tag: {product.tag}</p>
                      </li>
                  </Link>
                ))
                }
          
            
            </ul>
          
        <div>
        
          <Pagination totalPosts={products.length} postsPerPage={itemsPerPage} setCurrentPage={setCurrentPage} />
        </div>
      </div>
    );
  }
};

export default Home;
