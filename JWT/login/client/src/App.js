import './App.css';

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


export function Login() {
  return (
    <form className='form'>
      <input id='email' className='email' type='email' placeholder='Email' />
      <input id='pwd' className='pwd' type='password' placeholder='Password' /> 
      <input type="submit" value="login" className='submit'/>
    </form>
  );
}






// get access token click이벤트시 받아와야함
// get refresh token click이벤트시 받아와야함
// email, password 사용해서 login 하는 login 표시하는 곳

export default App;
