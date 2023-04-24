import React from 'react'

const Pagination = (props) => {
  let pages = []

  for (let i = 1; i<= Math.ceil( props.totalPosts / props.postsPerPage); i++){
    pages.push(i)
  } 

  return (
    <div>
      {pages.map((page, index) =>{
        return <button onClick={() => props.setCurrentPage(page)} key={index}>{page}</button>
      })}
    </div>
  )
}

export default Pagination