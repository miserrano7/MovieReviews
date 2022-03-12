import './App.css';
import React, {useState,useEffect} from 'react';
import { render } from '@testing-library/react';
 //need code here that will fetch info from the endpoint displaying movie info
 //need a save button
  //need a child component for each review
  function Review(props) {
    return (<button onClick={props.onClickButton}> Delete Review  </button>);
  }

function App() {
  const [reviews, setReview] = useState([]);
  const [edit, setEdit] = useState("");

  useEffect(() => { fetch("/userReviews").then(response => response.json())
  .then(data => setReview(data));
  },[])   

  function handleUpdateRat(event,id){
   const newRatings = [...reviews].map(revs => { 
     if(revs.id===id) {
       revs.ratings=event;
     }
     return revs;
   })

   setReview(newRatings)
   setEdit(event)
  }

  function handleClick(i) {
  const newReview = [...reviews].filter((revs, revs) => 
  { console.log("Revs: ",revs); return revs !==i});   
  console.log("update: ", newReview);
  setReview(newReview)
    }

    function renderReview(revs,i) { 
      return <Review value={revs} onClickButton={() => handleClick(i,revs)}/>;
    }

    function saveClick(){
      fetch("/newRoute", {
        method: "POST",
        headers: {"content-type": "application/json",
        },
        body: JSON.stringify(reviews)
      })
    }


  return (
    <div className="App">
      <header className="App-header">
        <p style={{color: "pink",fontSize:50,fontWeight: 'bold'}}> The comments and ratings you have entered </p>
        {reviews.map((revs,i) => (
          <p> ID: {revs.id}, MovieID: {revs.movieid}, Comment: {revs.comments}
          <form>
            Rating:
          <input type="number" value={revs.ratings} min="1" max="10" onChange={(event) => handleUpdateRat(event.target.value,revs.id)}/> 
         </form>
         {renderReview(revs.comments, i)}
          </p>
        ))} 
        <button onClick={saveClick}> Save Review</button>
      </header>
    </div>
  );
}
export default App;
