
const btn = document.querySelector('#btn-click')
btn.addEventListener('click', function(event) {
  const password = document.querySelector('#password')
  const passwordRecheck = document.querySelector('#password_confirmation')
  console.log(event.target.value.length)
  if (password.value.length < 8) {
    alert('비밀번호 8자리 이상이라고 했다.');
  } 
  if (password.value !== passwordRecheck.value) {
    alert('똑바로 입력하라고 했다.');
  }
})