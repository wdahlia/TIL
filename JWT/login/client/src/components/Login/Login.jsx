import React, { useState } from 'react';
// import axios from 'axios';

// onChange 사용해서 구현 후,
// FormData 사용해서 리팩토링할 것
export default function Login() {
  const [login, setLogin] = useState({
    email : '',
    password : '',
  });

  // onChange 사용해서 입력되는 값 받아오는 것 완료

  return (
    <form className='form'>
      <input
      className='email' 
      type='email' 
      placeholder='Email' 
      onChange={(e) => setLogin({
        ...login, email : e.target.value
      })}/>
      <input 
      className='pwd' 
      type='password' 
      placeholder='Password' 
      onChange={(e) => setLogin({
        ...login, password : e.target.value
      })}/> 
      <input type="submit" value="login" className='submit'/>
    </form>
  );
}

