/* globals fetch, moment */
const url = 'http://localhost:3000/todos'

document.addEventListener('submit', function (event) {
  event.preventDefault()
  const todoInput = document.querySelector('#todo-input').value
  console.log(todoInput)

  fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      todoItem: todoInput,
      created_at: moment().format()
    })
  })
    .then(res => res.json())
    .then(data => {
      const todoList = document.querySelector('#todo-list')
      const todoItemEl = document.createElement('li')
      todoItemEl.innerText = data.todoItem
      todoList.appendChild(todoItemEl)
    })
})

fetch(url)
  .then(res => res.json())
  .then(todoData => {
    const todoList = document.querySelector('#todo-list')
    for (const item of todoData) {
      console.log(item)
      const todoItemEl = document.createElement('li')
      todoItemEl.innerText = item.todoItem
      todoList.appendChild(todoItemEl)
    }
  })
