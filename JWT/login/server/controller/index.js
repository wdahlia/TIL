const userDatabase = require("../Database");
const jwt = require("jsonwebtoken");

// https://github.com/auth0/node-jsonwebtoken
// JsonWebToken

const login = (req, res, next) => {
  // node.js express 사용시, req = request
  // res = response
  // next는 middleware 함수
  // next(); 사용하는 이유는 매번 req 받을때마다 콘솔창에 어떤 값을 출력하게끔 하고 싶을때 사용
  // req에 대한 판단 유보라고 생각하면됨!

  const { email, password } = req.body;

  const userInfo = userDatabase.filter((item) => {
    return item.email === email;
  })[0];

  // console.log(userInfo); 
  // next();
  // 유효하지 않다면 [] 로 출력
  // 사용해서 userInfo 찍어보면 DB와 저장된 값이라면 [{}] 리스트 안에 객체 형태로 반환
  // 이때 첫번째 값을 얻고 싶기 때문에 [0]을 붙여주어야함

  if (!userInfo) {
    // userInfo가 아니면 403 error 발생, JSON으로 Not Authorized
    res.status(403).json('Not Authorized');
  } else {
    try {
      
      // Access Token 발급
      // jwt.sign(payload, secretOrPrivateKey, [options, callback])
      // payload 어떤 내용을 담을 것인지
      // secretOrPrivateKey 시크릿과 Private 키
      // options 세번째 인자는 algorithm 정보라던지, 유효시간, 발행자 등을 명시 가능

      const accessToken = jwt.sign({
        id : userInfo.id,
        username : userInfo.username,
        email : userInfo.email,
      }, process.env.ACCESS_SECRET, {
        expiresIn : '1m',
        issuer : 'Jinsook Ryu',
      });

      // Refresh Token 발급
      // 1회용으로 사용하는 것이 안전
      // 재발급해달라고 하고 그러면 인가 안해줘야함

      const refreshToken = jwt.sign({
        id : userInfo.id,
        username : userInfo.username,
        email : userInfo.email,
      }, process.env.REFRESH_SECRET, {
        expiresIn : '24h',
        issuer : 'Jinsook Ryu',
      });

      // Token 전송
      // res.cookie(name, value [, options])
      // httpOnly와 secure을 사용하여 쿠키에 저장하였기 때문에 CSRF 공격에 어느정도 보안할 수 있는 상태
      // local Storage와 db서버에 refreshToken 저장하는 방법도 있음
      res.cookie('accessToken', accessToken, {
        secure : false,
        // https인지 http인지 명시
        httpOnly : true,
        // javascript에서 쿠키 접근 불가능하게 하려면 true 값 설정하면 됨
      });

      res.cookie('refreshToken', refreshToken, {
        secure : false,
        // https인지 http인지 명시
        httpOnly : true,
        // javascript에서 쿠키 접근 불가능하게 하려면 true 값 설정하면 됨
      });

      res.status(200).json('로그인 성공');
      
    } catch (error) {
      // 예외의 경우 지정
      res.status(500).json(error);
    }
  }
};

const getAccessToken = (req, res) => {
  try {
    const token = req.cookies.accessToken;
    const data = jwt.verify(token, process.env.ACCESS_SECRET);

    const userData = userDatabase.filter(item => {
      return item.email === data.email;
    })[0];

    const { password, ...others } = userData;

    res.status(200).json(others);

  } catch (error) {
    res.status(500).json(error);
  }
};

const getRefreshToken = (req, res) => {
  try {
    const token = req.cookies.refreshToken;
    const data = jwt.verify(token, process.env.REFRESH_SECRET);

    const userData = userDatabase.filter(item => {
      return item.email === data.email;
    })[0];

    
    // accessToken 재발급
    const accessToken = jwt.sign({
      id : userData.id,
      username : userData.username,
      email : userData.email,
    }, process.env.ACCESS_SECRET, {
      expiresIn : '1m',
      issuer : 'Jinsook Ryu',
    });

    // accessToken 전송
    res.cookie('accessToken', accessToken, {
      secure : false,
      // https인지 http인지 명시
      httpOnly : true,
      // javascript에서 쿠키 접근 불가능하게 하려면 true 값 설정하면 됨
    });

    res.status(200).json(data);

    // token 받고 이제 
  } catch (error) {
    res.status(500).json(error);
  }
};

const loginSuccess = (req, res) => {
  try {
    // login이 되었는지 안되었는지를 확인해주어야함
    const token = req.cookies.accessToken;
    const data = jwt.verify(token, process.env.ACCESS_SECRET);

    const userData = userDatabase.filter(item => {
      return item.email === data.email;
    })[0];

    res.status(200).json(userData);

  } catch (error) {
    res.status(500).json(error);
  }
};

const logout = (req, res) => {
  try {
    // cookie 지우는 방식
    res.cookie('accessToken', '');
    res.status(200).json('logout success');
  } catch (error) {
    res.status(500).json(error);
  }
}

module.exports = {
  login,
  getAccessToken,
  getRefreshToken,
  loginSuccess,
  logout,
}