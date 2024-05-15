import React from "react";


function TodoItem({ todo }) {

    return (
        <div className="todo-container">
            <p className="todo-title">{todo.title}</p>
            <p className="todo-description">{todo.content}</p>

        </div>
    );
}

export default TodoItem