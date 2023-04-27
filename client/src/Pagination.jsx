import React from 'react'

const Pagination = (props) => {
  let pages = []

  for (let i = 1; i<= Math.ceil( props.totalPosts / props.postsPerPage); i++){
    pages.push(i)
  } 

  const handleClick = (page) => {
    props.setCurrentPage(page);
    window.scrollTo(0, 0);
  };

  return (
    <div>
      {pages.map((page, index) =>{
        return <button onClick={() => handleClick(page)} key={index}>{page}</button>
      })}
    </div>
  )
}

export default Pagination
