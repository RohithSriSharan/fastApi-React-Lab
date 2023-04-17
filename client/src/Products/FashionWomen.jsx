import { useEffect, useState , useContext} from "react"
import React from 'react'
import AuthContext from "../Auth/AuthContext";
import { Redirect, Link } from "react-router-dom";
import { useHistory } from 'react-router-dom';
import './FashionWomen.css'

const FashionWomen = () => {
    const history = useHistory();
    const [products, setProducts] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');
    const { isLoggedIn } = useContext(AuthContext);

    useEffect(() =>{
        fetch("http://127.0.0.1:8000/women/fashion")
            .then(response => response.json())
            .then(data => {
                setProducts(data);
            })
            .catch(error => console.log(error))
    },[])

    const filteredProducts = products.filter(product => 
        product.name.toLowerCase().includes(searchQuery.toLowerCase())
    );


   
    

    if(!isLoggedIn){
        return <Redirect to={'/login'} />
    } else {
        return (
            <div className="fashion-women-div">FashionWomen
                <input type="text" value={searchQuery} onChange={event => setSearchQuery(event.target.value)}></input>
                <ul className="product-card" >
                    {filteredProducts.map(product =>
                        
                        <Link className="link" to={`/product/`+ product.id}>
                            <li  key={product.id} >
                            
                                <img src={product.image}></img>
                                <p>{product.name}</p>
                                <p>{product.actual_price}</p>
                            </li>
                            
                        
                        </Link>
                        
                    )}
                </ul>
            </div>
        )
    }    
}

export default FashionWomen
