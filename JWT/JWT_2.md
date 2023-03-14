# JWT를 사용한 로그인 구현
> JWT란?
<br>

### JWT 토큰
> JSON Web Token

```
# 토큰 값 예시
# HS256 암호화 방식 사용

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

# XXXXX.YYYYY.ZZZZZ
# 세 부분으로 나뉘어져 있음
# 각각 header(헤더), payload(내용), verify signature(서명)
```

<br>

```json
// header 
// eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9에 해당하는 부분
{
  "alg": "HS256",
  "typ": "JWT"
}
```
- `header` 부분
	- `typ` - 토큰 유형
	- `alg` - 사용할 해시 알고리즘 HS256등 여러 암호화 방식 중 하나를 지정 가능, 한쪽 방향으로는 계산이 되더라도 양방향으로는 계산되지 아니함

<br>

```json
// payload
// eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
```
- `payload` 
	- 토큰에서 사용할 정보의 조각들인 `Claim`이 담겨있음
		- key-value 형식으로 이루어진 한 쌍의 정보를 Claim이라고 함
	- Base64로 디코딩해보면 JSON형식으로 실제로 사용될 정보가 들어있음
	- 정해진 데이터 타입은 없으나
		- `Registed claims` : 미리 정의된 클레임
			- iss(issuer; 발행자)
			- exp(expireation time; 만료 시간)
			- sub(subject; 제목)
			- iat(issued At; 발행 시간) 
			- jti(JWI ID)
		- `Public claims` : 사용자가 정의할 수 있는 클레임 공개용 정보 전달을 위해 사용
		- `Private claims` : 해당하는 당사자들 간에 정보를 공유하기 위해 만들어진 사용자 지정 클레임. 외부에 공개되도 상관없지만 해당 유저를 특정할 수 있는 정보들을 담는다

<br>

```json
// verify signature
// SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
)
```

- header와 payload Base64 URL-safe Encode를 한 이후 그리고 서버에 감춰놓은 비밀 값 세개를  header에서 정의한 alg(암호화 알고리즘)에 넣고 돌리게 되면 `verify signature`값이 나오게 됨
- 서버 측에서 관리하는 비밀번호가 유출되지 않는 이상 복호화 불가능
	- 토큰의 위변조 여부 확인하는데 사용

<br>

### 로그아웃 구현

- 따라한 영상 내부에서는 res.cookie('accessToken', '') 이런식으로 토큰을 없애주는 방식을 사용
- `res.clearCookie('쿠키의 key', cookieOptions)` 의 방식 존재