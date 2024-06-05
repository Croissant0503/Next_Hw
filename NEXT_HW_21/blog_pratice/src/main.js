import React, { useEffect, useState, useRef } from 'react';
import { Link } from 'react-router-dom';
import './Main.css';

const Main = () => {
    const [posts, setPosts] = useState([]);
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [images, setImages] = useState([]);
    const [previewImages, setPreviewImages] = useState([]);
    const [isEditing, setIsEditing] = useState(false);
    const [currentPostId, setCurrentPostId] = useState(null);

    const fileInputRef = useRef();

    useEffect(() => {
        const savedPosts = JSON.parse(localStorage.getItem('posts')) || [];
        setPosts(savedPosts);
    }, []);

    const handleImageChange = (e) => {
        const files = Array.from(e.target.files);
        const newImages = files.map((file) => URL.createObjectURL(file));
        setImages(files);
        setPreviewImages(newImages);
    };

    const handleSubmit = () => {
        const newPost = { title, content, images: previewImages.length ? previewImages : [] };
        let updatedPosts;
        if (isEditing) {
            updatedPosts = posts.map((post, index) => (index === currentPostId ? newPost : post));
            setIsEditing(false);
            setCurrentPostId(null);
        } else {
            updatedPosts = [...posts, newPost];
        }
        setPosts(updatedPosts);
        localStorage.setItem('posts', JSON.stringify(updatedPosts));
        setTitle('');
        setContent('');
        setImages([]);
        setPreviewImages([]);
    };

    const handleEdit = (index) => {
        const post = posts[index];
        setTitle(post.title);
        setContent(post.content);
        setPreviewImages(post.images);
        setIsEditing(true);
        setCurrentPostId(index);
    };

    const handleDelete = (index) => {
        const updatedPosts = posts.filter((_, i) => i !== index);
        setPosts(updatedPosts);
        localStorage.setItem('posts', JSON.stringify(updatedPosts));
    };

    const handleButtonClick = () => {
        fileInputRef.current.click();
    };

    return (
        <div className="container">
            <h1>💙 민지의 블로그 💙</h1>
            {posts.map((post, index) => (
                <div key={index} className="post">
                    <h2>{post.title}</h2>
                    <p>{post.content}</p>
                    <div>
                        {post.images && post.images.length > 0 ? (
                            post.images.map((image, imgIndex) => (
                                <img key={imgIndex} src={image} alt={`Post ${index} Image ${imgIndex}`} width="100" />
                            ))
                        ) : (
                            <p>No images available</p>
                        )}
                    </div>
                    <Link to={`/post/${index}`}>자세히 보기</Link>
                    <div className="button-group">
                        <button onClick={() => handleEdit(index)}>Edit</button>
                        <button onClick={() => handleDelete(index)}>Delete</button>
                    </div>
                </div>
            ))}

            <h2>{isEditing ? 'Edit Post' : '어떤 글을 써볼까요?'}</h2>
            <div className="form-group">
                <input type="text" placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} />
                <textarea placeholder="Content" value={content} onChange={(e) => setContent(e.target.value)} />
            </div>
            <div className="button-container">
                <button className="custom-file-upload" onClick={handleButtonClick}>
                    사진 업로드하기
                </button>
                <button onClick={handleSubmit}>{isEditing ? 'Update' : '저장하기'}</button>
            </div>
            <input
                type="file"
                accept="image/*"
                multiple
                onChange={handleImageChange}
                ref={fileInputRef}
                style={{ display: 'none' }}
            />
            <div className="preview">
                {previewImages.length > 0 &&
                    previewImages.map((preview, index) => (
                        <img key={index} src={preview} alt={`Preview ${index}`} width="100" />
                    ))}
            </div>
        </div>
    );
};

export default Main;
