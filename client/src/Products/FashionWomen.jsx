import { useEffect, useState , useContext} from "react"
import React from 'react'
import AuthContext from "../Auth/AuthContext";
import { Redirect, Link } from "react-router-dom";

import './FashionWomen.css'
import Pagination from "../Pagination";

import ProductCard from "../Components/ProductCard";

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

    console.log(products)
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
                <div className="fashion-women-products">
                    <ul>
                        {currentItems.map(product =>
                                <li>
                                    <ProductCard className="product"  id={product.id}
                                        name = {product.name}
                                        image = {product.image}
                                    />
                                </li>
                               
                        
                        )}
                        </ul>
                       
                </div>
                    
                <div className="fashion-women-pagination">
                    <Pagination totalPosts = {products.length} postsPerPage={postsPerPage} setCurrentPage={setCurrentPage}></Pagination>
                </div>
                
            </div>
        )
    }    
}

export default FashionWomen
