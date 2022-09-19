
// modal toggle
const modalToggle = function() {
  document.querySelector('#modal-content').classList.toggle('active')
}

// modal active
const modalBtn = document.querySelector('#modal-btn')
modalBtn.addEventListener('click', modalToggle)

// modal reset
const modalResetBtn = document.querySelector('#modal-back-btn')
modalResetBtn.addEventListener('click', modalToggle)