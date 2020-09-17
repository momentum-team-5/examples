for (let img of document.querySelectorAll('img')) {
  img.addEventListener('click', function (event) {
    console.log(event)
    event.target.classList.add('border-purple')
  })
}

let buttonDiv = document.querySelector('.number-buttons')

buttonDiv.addEventListener('click', function (event) {
  console.log('CLICKED!!!')
  console.log('the box you clicked was ', event.target.id)
  // create a new element
  // create a p
  // that p element will have text inside it.
  // if the p is already there, remove it
  let existingP = document.querySelector('.msg-p')
  if (existingP) {
    existingP.remove()
  }
  // select the element that will be the parent of the new element we're creating
  let messageDiv = document.querySelector('.message')
  // create a new paragraph element
  let messagePara = document.createElement('p')
  // add a class to it so it's easier to select
  messagePara.classList.add('msg-p')
  // set the innerText to display the id of the box that was clicked.
  messagePara.innerText = `The box you clicked on was ${event.target.id}`
  // add this whole new paragraph element to the page
  messageDiv.appendChild(messagePara)
})
