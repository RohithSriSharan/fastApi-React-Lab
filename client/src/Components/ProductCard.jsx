import React from 'react'
import { Link } from 'react-router-dom'
import "./ProductCard.css"
const ProductCard = (props) => {
  return (
    <div className='product-card'>
    <Link className="link" to={`/product/`+ props.id} key={props.id} target="_blank" >
        <img src={props.image}></img>
        <p>Name: {props.name}</p>
    </Link>
        
    </div>
  )
}

export default ProductCard