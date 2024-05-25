import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import TodosPage from "./pages/todos/TodosPage";
import BlogPage from './pages/blog/BlogPage';

function App() {

  return (
    <BrowserRouter>
      <Routes>

        <Route path="/todos/" element={<TodosPage />} />

        <Route path="/posts/" element={<BlogPage />} />
  
      </Routes>
    </BrowserRouter>
  )

}

export default App
