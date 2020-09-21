// select the target element on the page
let targetEl = document.querySelector('.menu-items')

// create a ul
let list = document.createElement('ul')

// append the ul to the dom
targetEl.appendChild(list)

for (let menuItem of menuItems) {
  // create an li
  let listItem = document.createElement('li')

  // create p element
  let itemTitleEl = document.createElement('p') // <p></p>
  itemTitleEl.innerText = menuItem.title // <p>noodles</p>
  listItem.appendChild(itemTitleEl) // <li><p>noodles</p></li>
  list.appendChild(listItem) // <ul><li><p>noodles</p></li></ul>

  // create an image element
  let imgEl = document.createElement('img')
  imgEl.src = menuItem.imgUrl
  console.log(imgEl)
  listItem.appendChild(imgEl)
}
