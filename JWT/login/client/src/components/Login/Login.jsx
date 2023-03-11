import React, { useState } from 'react';
import axios from 'axios';
import styles from './Login.module.css';
// onChange 사용해서 구현 후,
// FormData 사용해서 리팩토링할 것
export default function Login() {
  const [login, setLogin] = useState({
    email : '',
    password : '',
  });

  const handleSubmit = (e) => {
    e.preventDefault();

    axios({
      url: "http://localhost:8123/login",
      method: "post",
      withCredentials: true,
      data: {
        email: login.email,
        password: login.password
      },
    }).then((result) => {
      console.log(result);
    }).catch((error) => {
      console.log('실패');
      console.log(error.response.data);
    })
  };

  // onChange 사용해서 입력되는 값 받아오는 것 완료
  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <input
      className={styles.email} 
      type='email' 
      placeholder='Email' 
      onChange={(e) => setLogin({
        ...login, email : e.target.value
      })}
      value={login.email}/>
      <input 
      className={styles.pwd}
      type='password' 
      placeholder='Password' 
      onChange={(e) => setLogin({
        ...login, password : e.target.value
      })}
      value={login.password}/> 
      <input type="submit" value="login" className={styles.submit}/>
    </form>
  );
}

