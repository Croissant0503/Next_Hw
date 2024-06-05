import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Main from './main'; // 정확한 대소문자 사용
import Detail from './detail';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Main />} />
                <Route path="/post/:id" element={<Detail />} />
            </Routes>
        </Router>
    );
}

export default App;
