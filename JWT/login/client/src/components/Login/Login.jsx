import React, { useState } from 'react';
import axios from 'axios';
import styles from './Login.module.css';
// onChange 사용해서 구현 후,
// FormData 사용해서 리팩토링할 것
export default function Login() {
  const [info, setInfo] = useState({
    email : '',
    password : '',
  });

  const handleSubmit = (e) => {
    e.preventDefault();

    axios({
      url: "http://localhost:8123/login",
      method: "POST",
      withCredentials: true,
      data: {
        email: info.email,
        password: info.password
      },
    }).then((result) => {
      if (result.status === 200) {
        window.open('/', '_self');
      }
    }).catch((error) => {
      console.log('실패');
      console.log(error.response);
    })
  };


  // onChange 사용해서 입력되는 값 받아오는 것 완료
  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <input
      className={styles.email} 
      type='email' 
      placeholder='Email' 
      onChange={(e) => setInfo({
        ...info, email : e.target.value
      })}
      value={info.email}/>
      <input 
      className={styles.pwd}
      type='password' 
      placeholder='Password' 
      onChange={(e) => setInfo({
        ...info, password : e.target.value
      })}
      value={info.password}/> 
      <input type="submit" value="login" className={styles.submit}/>
    </form>
  );
}

