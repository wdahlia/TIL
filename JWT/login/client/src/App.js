import './App.css';
// import axios from 'axios';
import Login from './components/Login/Login'

function App() {
  return (
    <>
      <GetToken name='getAccessToken' />
      <GetToken name='getRefreshToken'/>
      <div className='box'>
        <Login />
      </div>
    </>
  );
}



export function GetToken({ name }) {
  return (
    <div className='btn-box'>
      <button className='btn'>{name}</button>
    </div>
  );
}





// get access token click이벤트시 받아와야함
// get refresh token click이벤트시 받아와야함
// email, password 사용해서 login 하는 login 표시하는 곳

export default App;
