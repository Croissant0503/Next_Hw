import { useReducer, useState } from 'react';
import './App.css';

function Header({ children, onChangeMode }) {
    return <h1 onClick={() => onChangeMode()}>{children}</h1>;
}
function Nav({ list, onChangeMode }) {
    return (
        <nav>
            <ol>
                {list.map((item) => (
                    <li key={item.id} onClick={() => onChangeMode(item.id)}>
                        <div>{item.title}</div>
                    </li>
                ))}
            </ol>
        </nav>
    );
}
function Article({ title, content }) {
    return (
        <article>
            <h2>{title}</h2>
            <p>{content}</p>
        </article>
    );
}

function Create({ onCreate }) {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    const handleClick = () => {
        onCreate(title, content);
        setTitle('');
        setContent('');
    };

    return (
        <div>
            <p>
                <input type="text" placeholder="title" value={title} onChange={(e) => setTitle(e.target.value)}></input>
            </p>
            <p>
                <textarea placeholder="content" onChange={(e) => setContent(e.target.value)}></textarea>
            </p>
            <p>
                <button type="button" onClick={handleClick}>
                    생성
                </button>
            </p>
        </div>
    );
}

function Update({ onUpdate, item }) {
    const [title, setTitle] = useState(item.title);
    const [content, setContent] = useState(item.content);

    const handleClick = () => {
        onUpdate(title, content);
    };

    return (
        <div>
            <p>
                <input type="text" placeholder="tile" value={title} onChange={(e) => setTitle(e.target.value)}></input>
            </p>
            <p>
                <textarea placeholder="content" value={content} onChange={(e) => setContent(e.target.value)}></textarea>
            </p>
            <p>
                <button type="button" onClick={handleClick}>
                    수정
                </button>
            </p>
        </div>
    );
}

function App() {
    const [mode, setMode] = useState('HOME');
    const [id, setId] = useState(-1);

    const [list, setList] = useState([
        { id: 0, title: '이름', content: '이민지' },
        { id: 1, title: '생년월일', content: '2001.05.03' },
        { id: 2, title: '학력', content: '고려대학교' },
    ]);

    let title;
    let content;

    if (mode === 'HOME') {
        title = '글 작성';
        content = '오늘 할 일을 작성해주세요!';
    } else if (mode === 'READ') {
        title = list[id].title;
        content = list[id].content;
    }

    const handleCreate = (title, content) => {
        setList([...list, { title, content, id: list.length }]);
        setMode('HOME');
    };

    const handleUpdate = (title, content) => {
        setList(list.map((item) => (item.id === id ? { ...item, title, content } : item)));
        setMode('READ');
    };

    const handleDelete = () => {
        setList(list.filter((item) => item.id !== id));
        setMode('HOME');
        setId(-1);
    };

    return (
        <>
            <Header onChangeMode={() => setMode('HOME')}>민지의 투두리스트</Header>
            <Nav
                list={list}
                onChangeMode={(_id) => {
                    setMode('READ');
                    setId(_id);
                }}
            ></Nav>
            <Article title={title} content={content}></Article>
            {mode === 'CREATE' && <Create onCreate={handleCreate} />}
            {mode === 'HOME' && <button onClick={() => setMode('CREATE')}>글 생성</button>}
            {mode === 'READ' && (
                <>
                    <button onClick={() => setMode('UPDATE')}>글 수정</button>
                    <button onClick={handleDelete}>글 삭제</button>
                </>
            )}
            {mode === 'UPDATE' && <Update onUpdate={handleUpdate} item={list.find((item) => item.id === id)} />}
        </>
    );
}

export default App;
