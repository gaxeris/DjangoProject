import React from "react";


function TodoItem({ todo }) {

    return (
        <div className="todo-container">
            <p className="todo-title">{todo.title}</p>
            <p className="todo-description">{todo.description}</p>


            <button className="delete-button" onClick={() => onDelete(todo.id)}>
                Delete
            </button>
        </div>
    );
}

export default TodoItem