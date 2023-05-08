import React from 'react'
import { Link } from 'react-router-dom'
import "./ProductCard.css"

import { MdOutlineAddShoppingCart } from 'react-icons/md';

const ProductCard = (props) => {
  

  return (
    <div className='product-card'>
      <div className='product-card-top'>
          <Link className="link" to={`/product/`+ props.id} key={props.id} target="_blank" >
          <img className='product-card-image' src={props.image}></img>
          <p id='my-paragraph' className='product-card-name'>{props.name}</p>
          
          </Link>
      
      </div>
      
        <div className='cart-price'>
          <p className='cart-price-price'>{props.price}</p>
          <button className='product-card-button'><MdOutlineAddShoppingCart/></button>
          
        </div>
    
        
    </div>
  )
}

export default ProductCard