const userDatabase = require("../Database");
const jwt = require("jsonwebtoken");

// https://www.npmjs.com/package/jsonwebtoken
// JsonWebToken

const login = (req, res, next) => {
  const { email, password } = req.body;

  const userInfo = userDatabase.filter((item) => {
    return item.email === email;
  })[0];

  if (!userInfo) {
    // userInfo가 아니면 403 error 발생, JSON으로 Not Authorized
    res.status(403).json("Not Authorized");
  }
};


module.exports = login;