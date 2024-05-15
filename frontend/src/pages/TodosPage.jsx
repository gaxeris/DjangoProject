import react, { useState, useEffect } from "react"
import TodoItem from '../components/todo/TodoItem'

function TodosPage() {

  const [todoItems, setTodoItems] = useState([])

  useEffect(() => {
    fetchTodoItems()
  }, []);

  const fetchTodoItems = async () => {
    const response = await fetch("http://127.0.0.1:8000/api/todos/");
    const data = await response.json();
    setTodoItems(data);
    console.log(data)
  };

  return (
    <>
      <div>
        <h2>Todo Items</h2>
        {todoItems.map((todo) => (
          <TodoItem todo={todo} />
        ))}
      </div>
    </>
  )
}

export default TodosPage
