const form = document.querySelector('#registration-form')
let formIsValid // this is set as a global variable so it can be used in different functions

form.addEventListener('submit', validateForm)

function validateForm (event) {
  event.preventDefault()
  removeErrorMessage() // if an error message is showing from a previous validation attempt
  formIsValid = true // reset this each time you try to validate the form

  validateAge()
  confirmPasswordMatch()
  // create some more functions to validate more form fields

  if (formIsValid) {
    fetch('https://momentum-server.glitch.me/parking', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ formData: { name: 'Amy' } }) // get this value from the form input!
    })
      .then(res => res.json())
      .then(data => {
        console.log(data)
        // you can add a message to the DOM that says that the form was successfully submitted!
      })
  }
}

function validateAge () {
  const ageInput = document.querySelector('#age-input')

  if (ageInput.value > 18) {
    console.log('age is valid')
  } else {
    formIsValid = false
    console.log('age is invalid')
  }
}

function confirmPasswordMatch () {
  // grab the password input
  const password = document.querySelector('#password-input')
  // grab the confirm password input
  const confirmPwd = document.querySelector('#confirm-password')
  confirmPwd.parentElement.classList.remove('input-invalid') // if it's there from before

  // compare their values to see if they match
  if (password.value !== confirmPwd.value) {
    // show an error message on the page
    const errorDiv = document.querySelector('#error-msg')
    errorDiv.innerHTML = 'Your passwords must match'
    confirmPwd.parentElement.classList.add('input-invalid')
    formIsValid = false
  }
}

function removeErrorMessage () {
  const errorDiv = document.querySelector('#error-msg')
  if (errorDiv) {
    errorDiv.innerHTML = ''
  }
}
