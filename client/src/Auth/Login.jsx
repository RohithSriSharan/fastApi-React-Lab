import React from 'react'
import './Login.css'
const Login = () => {
    const [username, setUsername] = useState('')
    const[password, setPassword] = useState('')
  
    const [form, setForm] = useState({
      username:'',
      password
    })
  
    const handleChange = (e) =>{
      const {name, value} = e.target;
      setForm({ ...form , [name]:value});
  
    }
  
    useEffect(() => {
      fetch('http://localhost:8000')
      .then(resoponse => resoponse.json())
      .then(res => setData(res))
      .catch(error => console.log(error))
    },[])
  
  
  
    const handleSubmit =async (e) =>{
      e.preventDefault();
      const response =  await fetch("http://localhost:8000",{
        method:'POST',
        headers:{
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(form),
      });
      const data = await response.json();
      
    }
   
  return (
    <div>
          <from  >
            <label>Username</label>
            <input type='text' name='username' value={form.username} onChange={handleChange}></input>
            <br></br>
            <label>Password</label>
            <input type='password' name='password' value={form.password} onChange={handleChange} ></input>
            <br></br>
            <input type='submit' onClick={handleSubmit}></input>
          </from>
       
      </div>
  )
}

export default Login