import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [notes, setNotes] = useState([]);

  const fetchNotes = () => {
    fetch("/notes")
      .then(res => res.json())
      .then(res => setNotes(res))
  }
  useEffect(() => {
    fetchNotes();
  }, []);

  return (
    <div className="App">
      <body>
        <h1>Hello World</h1>
        <ul>
          {notes.map(note => {
            return <li>{note}</li>
          })}
        </ul>
      </body>
    </div>
  );
}

export default App;
