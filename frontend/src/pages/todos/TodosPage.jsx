import react, { useState, useEffect } from "react";
import axios from "axios";
import TodoItem from '../../components/todos/TodoItem';

function TodosPage() {

  const [todoItems, setTodoItems] = useState([]);

  const [description, setDescription] = useState("");
  const [title, setTitle] = useState("");


  useEffect(() => {
    getTodoItems()
  }, []);


  function getTodoItems() {
    return axios.get('http://127.0.0.1:8000/api/todos/')
    .then((res) => res.data)
    .then((data) => {
        setTodoItems(data);
        console.log(data);
    })
    .catch((err) => alert(err));
  }

  const deleteTodoItems = (id) => {
    return axios.delete(`http://127.0.0.1:8000/api/todos/${id}/`)
      .then((res) => {
          if (res.status === 204) alert("Todo item deleted!");
          else alert("Failed to delete the todo item.");
          getTodoItems();
      })
      .catch((error) => alert(error));
  };

  const createTodoItems = (e) => {
    e.preventDefault();
    return axios.post("http://127.0.0.1:8000/api/todos/", { description, title })
        .then((res) => {
            if (res.status === 201) alert("Todo item created!");
            else alert("Failed to make a todo item.");
            getTodoItems();
        })
        .catch((err) => alert(err));
  };


  return (
    <>
      <div>
        <h2>Todo Items</h2>
        <ul>
          {todoItems.map((todo) => (
            <li><TodoItem todo={todo} onDelete={deleteTodoItems} key={todo.id} /></li>
          ))}
        </ul>
      </div>
      <div>
        <h2>Create a Todo Item</h2>
          <form onSubmit={createTodoItems}>
            <label htmlFor="title">Title:</label>
            <br />
            <input
                type="text"
                id="title"
                name="title"
                required
                onChange={(e) => setTitle(e.target.value)}
                value={title}
            />
            <label htmlFor="description">Description:</label>
            <br />
            <textarea
                id="description"
                name="content"
                required
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            ></textarea>
            <br />
            <input type="submit" value="Submit"></input>
          </form>
      </div>
    </>
  )
}

export default TodosPage
