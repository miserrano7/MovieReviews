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
        <p style={{color: "pink",fontSize:50,fontWeight: 'bold'}}> The comments and ratings you have entered: </p>
        {id.map(com => (
        <p> Id: {com.id}, MovieID: {com.movieid}, Comments: {com.comments}, Ratings: {com.ratings} </p>
        ))}
      </header>
    </div>
  );
}

export default App;
