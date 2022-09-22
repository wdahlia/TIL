
// next 버튼
const nextBtn = document.querySelector('#nextBtn')

nextBtn.addEventListener('click', function() {
  const currentElement = document.querySelector('.active')
  const items = document.querySelectorAll('.carousel-item')
  const idx = [...items].indexOf(currentElement)
  console.log(currentElement, items, idx)
  currentElement.classList.toggle('active')
  items[(idx+1)%items.length].classList.toggle('active')
})

// prev 버튼
const prevBtn = document.querySelector('#prevBtn')

prevBtn.addEventListener('click', function() {
  const currentElement = document.querySelector('.active')
  const items = document.querySelectorAll('.carousel-item')
  const idx = [...items].indexOf(currentElement)
  console.log(currentElement, items, idx)
  currentElement.classList.toggle('active')
  if (idx === 0){
    items[items.length-1].classList.toggle('active')
  }
  else {
  items[(idx-1)%items.length].classList.toggle('active')
  }
  // items[((idx-1)+items.length)%items.length].classList.toggle('active')
}) 