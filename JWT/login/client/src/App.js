import './App.css';
import axios from 'axios';
import Login from './components/Login/Login'
import { useState } from 'react';

function App() {
  const [user, setUser] = useState({
    email : '',
    iss : '',
    username : '',
  });

  const handleAccess = () => {

    axios({
      url : 'http://localhost:8123/accesstoken',
      method : 'GET',
      withCredentials : true,
    }).then((response) => {
      const { email, iss, username } = response.data;
      console.log(email, iss, username);
      setUser({ email, iss, username });
    });
  };

  const handleRefresh = () => {
    axios({
      url : 'http://localhost:8123/refreshtoken',
      method : 'GET',
      withCredentials : true,
    }).then((response) => {
      const { email, iss, username } = response.data;
      console.log(email, iss, username);
      setUser({ email, iss, username });
    });
  };

  return (
    <>
      <GetToken name='getAccessToken' getToken={handleAccess} user={user} />
      <GetToken name='getRefreshToken' getToken={handleRefresh} />
      <div className='box'>
        <Login />
      </div>
    </>
  );
}



export function GetToken({ name, getToken }) {
  return (
    <div className='btn-box'>
      <button className='btn' onClick={getToken}>{name}</button>
    </div>
  );
}





// get access token click이벤트시 받아와야함
// get refresh token click이벤트시 받아와야함
// email, password 사용해서 login 하는 login 표시하는 곳

export default App;
