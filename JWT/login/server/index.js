// express 서버 구현
const express = require("express");
const dotenv = require("dotenv");
const cookieParser = require("cookie-parser");
const cors = require("cors");
const {
  login,
  getAccessToken,
  getRefreshToken,
  loginSuccess,
  logout,
 } = require("./controller");

const app = express();
dotenv.config();

// 기본설정을 해줍니다.
// 기본 설정
// client 와 server 간의 통신을 위해 JSON 형식의 파일을 다뤄야함
app.use(express.json());
// express 내부에 있는 미들웨어인 express.json()을 설치

// 쿠키를 사용해서 JSON 웹 토큰을 사용할 것이기 때문에
app.use(cookieParser());
// 클라이언트에서 서버간 오리진이 다른상황에서 통신을 하기 위해서
app.use(
  cors({
    origin: "http://localhost:3000",
    methods: ["GET", "POST"],
    credentials: true,
  })
);
// origin : 클라이언트 단
// 사용자와 서버간의 통신에서 cookie를 이용하여 통신할 것이기 때문에
// Credentials 쿠키, Authorization 인증 헤더, TLS client certificates를 내포하는 자격인증 정보
// 요청과 응답에 쿠키를 허용하고 싶을 경우
// 다른 도메인(Cross Origin)에 요청 보낼 때 요청에 인증 정보를 담아서 보낼지를 결정하는 항목

app.post("/login", login);
app.get("/accesstoken", getAccessToken);
app.get("/refreshtoken", getRefreshToken);
app.get("/login/success", loginSuccess);
app.post("/logout", logout);
// access token 제거

// app에 port 연결
// 이 API 서버 PORT는 8123
app.listen(process.env.PORT, () => {
  console.log(`server is on ${process.env.PORT}`);
});
