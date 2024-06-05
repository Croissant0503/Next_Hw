import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Main from './Main';
import Detail from './Detail';

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
