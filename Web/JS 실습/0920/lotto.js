
const btn = document.querySelector('#btn')
btn.addEventListener('click', function() {
  const ballContainer = document.createElement('div')
  // div를 만들어주고 그걸 ballContainer라는 변수에 저장 그리고 그 div에 ball-container라는 class를 준다
  ballContainer.classList.add('ball-container')
  const numbers = _.sampleSize(_.range(1, 46), 7)
  const colors = ["#fcbf49", "#4361ee", "#f25c54", "#e0e1dd", "#80ed99"]
  for (let idx in numbers) {
    // 1~10, 11~20, 21~30, 31~40, 41~45 노 파 빨 회 녹
    let bgColor = Math.floor(numbers[idx]/10)
    // let ballBox = document.createElement('div')
    // ballBox.classList.add('ball-box')
    const ball = document.createElement('div')
    ball.classList.add('ball')
    if (idx !== (numbers.length - 1)) {

    }
    ball.innerText = numbers[idx]
    ball.style.backgroundColor = colors[bgColor]
    ballContainer.appendChild(ball)
    const result = document.querySelector('#result')
  }
  result.appendChild(ballContainer)
})