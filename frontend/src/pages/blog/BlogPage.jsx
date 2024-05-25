import react, { useState, useEffect } from "react"
import PostItem from '../../components/blog/Post'

function BlogPage() {

  const [postItems, setPostItems] = useState([])

  useEffect(() => {
    fetchPostItems()
  }, []);

  const fetchPostItems = async () => {
    const response = await fetch("http://127.0.0.1:8000/api/posts/");
    const data = await response.json();
    setPostItems(data);
    console.log(data)
  };

  return (
    <>
      <div>
        <h2>Post Items</h2>
        {postItems.map((post) => (
          <PostItem post={post} />
        ))}
      </div>
    </>
  )
}

export default BlogPage
