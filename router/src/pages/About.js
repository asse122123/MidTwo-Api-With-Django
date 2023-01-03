// export default function About() {
//   return <h1 className="a"> <a href="https//www.w3schools.com">Well Come to our About Page</a></h1>
// }
import axios from 'axios'
import React, { useState, useEffect } from 'react';

function About() {
  const[data, setData] = useState([])

  const fetch =() => {
    axios.get('http://127.0.0.1:8000/TeacherList/')
    .then((res) => setData(res.data))
    .then(err => console.log(err))
  }
  useEffect(()=>{
    fetch();
  },[])

  const deletes = (id)=>{
    axios.delete(`http://127.0.0.1:8000/TeacherDelete/${id}`).then((Response)=>
    alert(" are you sure ?"),fetch()).catch((err)=>console.log(err))
  }
  return (
  <div>
     <h1>STUDENT VIEW</h1>
    {data.map((res) => {
      return (
       
      <div className='ab'>
     
       <p className='fname'>FirstName:  {res.firstName}</p>
       <p className='lname'>LastName:  {res.lastName}</p>
       <button className='btn' onClick={()=>deletes(res.id)}>Delete</button>
      </div> 
      
      )
    })}
         
  </div>
  );
}

export default About;