import { useEffect, useState } from "react"
import React from 'react'
import { useParams } from "react-router-dom";

const SearchProductInfo = () => {
    const { id } = useParams();
    const { tag } = useParams();
    const [product, setProduct] = useState(null);
    console.log(id)
    useEffect(() => {
        fetch(`http://127.0.0.1:8000/search/${tag}/${id}`)
            .then(response => response.json())
            .then(data => {
                setProduct(data);
            })
            .catch(error => console.log(error))
    }, [id])
    

    if (!product) {
        return <div>Loading...</div>
    }
    
    return (
        <div>
            <h1>{product.name}</h1>
            <img src={product.image} alt="product"></img>
            <p>{product.description}</p>
            <p>Price: {product.actual_price}</p>
            <p>Category: {product.sub_category}</p>
        </div>
    )
}

export default SearchProductInfo
