import { useEffect, useState , useContext} from "react"
import React from 'react'
import AuthContext from "../Auth/AuthContext";
import { Redirect, Link } from "react-router-dom";

import './FashionWomen.css'
import Pagination from "../Pagination";
const FashionWomen = () => {
  
    const [products, setProducts] = useState([]);
   
    const { isLoggedIn } = useContext(AuthContext);
    const [currentPage, setCurrentPage] = useState(1);
    const [postsPerPage, setPostsPerPage] = useState(50)


    useEffect(() =>{
        fetch("http://127.0.0.1:8000/women/fashion")
            .then(response => response.json())
            .then(data => {
        
                setProducts(data);
            })
            .catch(error => console.log(error))
    },[])

    // const filteredProducts = products.filter(product => 
    //     product.name.toLowerCase().includes(searchQuery.toLowerCase())
    // );

    
    const lastPostIndex = currentPage * postsPerPage;
    const firstPostIndex = lastPostIndex - postsPerPage;
    const currentItems = products.slice(firstPostIndex, lastPostIndex);
   
    

    if(!isLoggedIn){
        return <Redirect to={'/login'} />
    } else {
        return (
            <div className="fashion-women-div">FashionWomen

                <ul className="product-card" >
                    {currentItems.map(product =>
                        
                        <Link className="link" to={`/product/`+ product.id} key={product.id} >
                            <li   >
                                <img src={product.image} alt="fashion-women"></img>
                                <p>{product.name}</p>
                                <p>{product.actual_price}</p>
                            </li>
                            
                        
                        </Link>
                        
                    )}
                </ul>
                <Pagination totalPosts = {products.length} postsPerPage={postsPerPage} setCurrentPage={setCurrentPage}></Pagination>
            </div>
        )
    }    
}

export default FashionWomen
