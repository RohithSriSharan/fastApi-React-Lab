import React from 'react'
import { useState } from 'react'

const Davinci = () => {
    const [Prompt, setPrompt] = useState("")
    const [davinciResponse, setDavinciResponse] = useState("")

    const handlePrompt = (e) =>{
            setPrompt(e.target.value)
    }

    const handleSubmit= async(e) => {
        e.preventDefault()
        const response = await fetch("http://127.0.0.1:8000/davinciprompt", {
            method:"POST",
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({"prompt": Prompt})

        })
        const responseJson = await response.json()
        console.log(responseJson)
        setDavinciResponse(responseJson)

        
    }
   

  return (
    <div className='davinci-div'>
        <div>
            <form onSubmit={handleSubmit}>
                <input name='prompt' type='text' placeholder='Ask Davinci for recommendations' value={Prompt} onChange={handlePrompt}></input> 
                <button type='submit'> Submit</button>
            </form>
        </div>
        <div>
            <p>{davinciResponse}</p>
        </div>
        
    </div>
  )
}

export default Davinci