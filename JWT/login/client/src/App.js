import './App.css';
import axios from 'axios';
import Login from './components/Login/Login'
import { useEffect, useState } from 'react';

function App() {
  const [login, setIsLogin] = useState(false);
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

  useEffect(() => {
    try {
      axios({
        url: "http://localhost:8123/login/success",
        method: "GET",
        withCredentials: true,        
      }).then((res) => {
        if (res.data) {
          setIsLogin(true);
          setUser({
            email : res.data.email,
            iss : res.data.iss,
            username : res.data.username,
          });
        };
      });
    } catch (error) {
      console.log(error);
    }
  }, []);

  const handleLogout = (e) => {
    e.preventDefault();

    axios({
      url: "http://localhost:8123/logout",
      method: "POST",
      withCredentials: true,
    }).then(() => {
      setIsLogin(!login);
      setUser({
        email : '',
        iss : '',
        username : '',
      });
    })
  };

  return (
    <>
      <GetToken name='getAccessToken' getToken={handleAccess} user={user} />
      <GetToken name='getRefreshToken' getToken={handleRefresh} />
      <div className='box'>
        { login ? 
        (<form className='logoutBox'>
          <p className='title'><span className='name'>{user.username}</span> 님</p>
          <p className='title'>{user.email}</p>
          <button
          type='button'
          className='logout'
          onClick={handleLogout}>Logout</button>
        </form>) : <Login login={login} setIsLogin={setIsLogin}/>
        }
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
