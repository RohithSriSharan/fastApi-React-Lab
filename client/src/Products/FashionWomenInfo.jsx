import { useEffect, useState } from "react"
import React from 'react'
import { useParams } from "react-router-dom";

const FashionWomenInfo = () => {
    const { id } = useParams();
    const [product, setProduct] = useState(null);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/product/${id}`)
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
            <img src={product.image}></img>
            <p>{product.description}</p>
            <p>Price: {product.actual_price}</p>
            <p>Category: {product.category}</p>
        </div>
    )
}

export default FashionWomenInfo
