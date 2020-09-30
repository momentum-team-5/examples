/* globals fetch, moment */
const url = 'http://localhost:3000/todos'
const todoList = document.querySelector('#todo-list')

document.addEventListener('submit', function (event) {
  event.preventDefault()
  createTodo()
})

todoList.addEventListener('click', function (e) {
  if (e.target.matches('.delete')) {
    deleteTodo(e.target.parentElement.dataset.id)
  }
})

function renderTodoList () {
  fetch(url)
    .then(res => res.json())
    .then(todoData => {
      for (const todo of todoData) {
        renderTodoItem(todo)
      }
    })
}

function renderTodoItem (todo) {
  const todoList = document.querySelector('#todo-list')
  const todoItemEl = document.createElement('li')
  todoItemEl.dataset.id = todo.id
  todoItemEl.id = `item-${todo.id}`
  todoItemEl.innerText = todo.todoItem
  const deleteIcon = document.createElement('span')
  deleteIcon.classList.add('fas', 'fa-times', 'mar-l-xs', 'delete')
  todoItemEl.appendChild(deleteIcon)
  todoList.appendChild(todoItemEl)
}

function createTodo () {
  const todoInputField = document.querySelector('#todo-input')

  const requestData = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      todoItem: todoInputField.value,
      created_at: moment().format()
    })
  }

  fetch(url, requestData)
    .then(res => res.json())
    .then(data => {
      todoInputField.value = ''
      renderTodoItem(data)
    })
}

function deleteTodo (todoId) {
  fetch(url + '/' + todoId, {
    method: 'DELETE'
  })
    .then(res => res.json())
    .then(data => {
      const itemToRemove = document.querySelector(`#item-${todoId}`)
      itemToRemove.remove()
    })
}

renderTodoList()
