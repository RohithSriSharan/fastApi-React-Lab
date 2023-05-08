import React from 'react'
import { useState } from 'react'
import './davinci.css'
import { VscHubot } from 'react-icons/vsc';

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
   
        setDavinciResponse(responseJson)
       
        
    }
   

  return (
    <div className='davinci-div'>


        <div className='davinci-response'>
            <p><VscHubot className='davinci-icon'/>{davinciResponse}</p>
        </div>
        <div className='davinci-form'>
            <form className='davinci-form-form' onSubmit={handleSubmit}>
                <input className='form-input' name='prompt' type='text' placeholder='Ask Davinci' value={Prompt} onChange={handlePrompt} required></input> 
                <button className='form-button' type='submit'>Submit</button>
            </form>
        </div>
        
        
    </div>
  )
}

export default Davinci