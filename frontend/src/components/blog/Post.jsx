import React from "react";


function PostItem({ post }) {

    return (
        <div className="post-container">
            <p className="post-title">{post.title}</p>
            <p className="post-text">{post.text}</p>

        </div>
    );
}

export default PostItem