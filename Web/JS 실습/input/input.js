 // input 기록 생성
 const inputText = document.querySelector('#input-text')

 inputText.addEventListener('input', function(e) {
   console.log(e)
   console.log(e.target.value)
 })