import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import {query, ingest} from './api';

function App() {
  const [inputValue, setInputValue] = useState('');

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleIngest = () => {

  };

  const handleQuery = (inputValue) => {
    query(inputValue);
  }

  return (
    <div className="App">
      <header className="App-header">
    <div>
      <input type="text" value={inputValue} onChange={handleChange} />
      <p>You typed: {inputValue}</p>
      <button onClick={() => handleQuery(inputValue)}>ask</button>
    </div>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
