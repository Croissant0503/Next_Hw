const todoForm = document.getElementById('todo-form');
const todoList = document.getElementById('todo-list');
const submitBtn = document.querySelector('.submitBtn');

let todos = JSON.parse(localStorage.getItem('todos')) || [];

function submitAddTodo(event) {
    event.preventDefault();
    const todoInput = document.getElementById('content');
    const newTodo = todoInput.value;
    if (newTodo.trim() !== '') {
        const newTodoObj = {
            id: Date.now(),
            text: newTodo,
        };
        todos.push(newTodoObj);
        todoInput.value = '';
        saveTodos();
        paintTodo();
    }
}

function paintTodo() {
    todoList.innerHTML = '';
    todos.forEach((todo) => {
        const li = document.createElement('li');
        li.id = todo.id;
        li.innerText = todo.text;
        const deleteBtn = document.createElement('button');
        deleteBtn.innerText = '삭제';
        deleteBtn.addEventListener('click', () => deleteTodo(todo.id));
        li.appendChild(deleteBtn);
        todoList.appendChild(li);
    });
}

function saveTodos() {
    localStorage.setItem('todos', JSON.stringify(todos));
}

function deleteTodo(id) {
    todos = todos.filter((todo) => todo.id !== id);
    saveTodos();
    paintTodo();
}

todoForm.addEventListener('submit', submitAddTodo);
document.addEventListener('DOMContentLoaded', paintTodo);
