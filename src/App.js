import './App.css';
import React, {useState} from 'react';
//need code here that will fetch info from the endpoint displaying movie info
//need a save button
function App() {
  const [id, setID] = useState([]);
  //const [comment, setComment] = useState("");
  //const [rating, setRating] = useState("");

    let x= fetch("/userReviews").then(response => response.json())
     .then(data => setID(data));

  return (
    <div className="App">
      <header className="App-header">
        {id.map(com => (
        <p> THis: {com.x} </p>
        ))}
      </header>
    </div>
  );
}

export default App;
