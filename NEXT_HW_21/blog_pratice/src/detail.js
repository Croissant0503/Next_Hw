import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const Detail = () => {
    const { id } = useParams();
    const [post, setPost] = useState(null);

    useEffect(() => {
        const savedPosts = JSON.parse(localStorage.getItem('posts')) || [];
        setPost(savedPosts[id]);
    }, [id]);

    if (!post) return <div>Loading...</div>;

    return (
        <div className="detail-container">
            <h1>{post.title}</h1>
            <p>{post.content}</p>
            <div className="detail-images">
                {post.images.map((image, index) => (
                    <img key={index} src={image} alt={`Post Image ${index}`} />
                ))}
            </div>
        </div>
    );
};

export default Detail;
