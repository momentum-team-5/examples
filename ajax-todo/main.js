/* globals fetch, moment */
const url = 'http://localhost:3000/todos'

document.addEventListener('submit', function (event) {
  event.preventDefault()
  createTodo()
})

function renderTodoList () {
  fetch(url)
    .then(res => res.json())
    .then(todoData => {
      const todoList = document.querySelector('#todo-list')
      for (const item of todoData) {
        const todoItemEl = document.createElement('li')
        todoItemEl.dataset.id = item.id
        todoItemEl.innerText = item.todoItem
        const deleteIcon = document.createElement('span')
        deleteIcon.classList.add('fas', 'fa-times', 'mar-l-xs', 'delete')
        todoItemEl.appendChild(deleteIcon)
        todoList.appendChild(todoItemEl)
      }
    })
}

function createTodo () {
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
}

renderTodoList()

function deleteTodo (todoId) {
  fetch(url + '/' + todoId, {
    method: 'DELETE'
  })
    .then(res => res.json())
    .then(data => {
      const itemToRemove = document.querySelector(`li[data-id='${todoId}']`)
      itemToRemove.remove()
    })
}

const todoList = document.querySelector('#todo-list')

todoList.addEventListener('click', function (e) {
  if (e.target.matches('.delete')) {
    console.log(e.target.parentElement.dataset.id)
    deleteTodo(e.target.parentElement.dataset.id)
  }
})
