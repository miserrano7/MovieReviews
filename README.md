# URL to Heroku App 
[Follow the link here to see my Heroku app](https://moviesdisplay.herokuapp.com/)

# Technologies Used
### Frameworks 

**Flask** is a framework used to create a web application. 

**Bootstrap** is a user interface framework that helps to style your pages. In this project I used boostrap to use its grid system to have each of my divs on different sections of the page.  

### Libraries

***Requests*** is an HTTP library. This library let's you get information from HTML to python (HTTP requests).

***Flask-login*** is a library that provides different functionality that is usually handlded for a user to login. 
It allows the user to login, logout, sessions, and allowing for specific routes to be decorated with `@login_required`. There are other user managment aspects which flask-login provides such as a `remember me` functionality. 

**Pyscog2-binary** is a library that allows the connection between Python and PostgresSQL (Database Managment System).

**React** React is a javascript library that allows us to build user interfaces. The imporant thing to note about react is that it lets you set up different pages and each user interface built uses components. 

# Other Technology

### Flask-SQLAlchemy 
For project 2 we used Flask-SQLAlchemy which provided us with the ability to use SQLAlchemy with Flask. SQLAlchemy is a library which basically allows the use of databases with Python. For this project we had to create a database and we use python/Flask in order to communicate with the database. 

# APIs Used 

### The Movie DB API
This API helps get information for most movies. In order to display the title, tagline, genres and poster image calls were made to the TMBD API. With the help of ***JSON***, which allowed to view data being called from the API, in a formatted way, I was able to see the data recieved from TMBD.

### MediaWiki API 
For project 1, we used this API to find a way to get the URL to a specific wikipedia page on the selected movie, which I accessed using the title. MediaWiki had many parameter options to pass in order to return the URL to a page. Mainly, I found the opensearch parameter most useful. Apart from being able to obtain links, you can get data of anything for wikipedia such as other links, and plot lines.


# Forking the repository
Before forking, certain ***installations** need to be made (they can be found below). In your terminal use the command: `git clone < copy and paste ssh url link here>` 
Now you should be able to open up the source code within your own IDE. Below you will find API Key Instrustions that need to be followed in order to be able to access data. From here you are able to modify the project, and eventually run your project locally with the command `python3 app.py`. 

## Installations for forking 
1. Install Visual Studio Code
2. Install Flask
3. Install requests 
4. Install JSON
5. Install dotenv
6. Install Black 
7. Install flask-login
8. Install psycopg2-binary
9. Install Flask-SQLAlchemy==2.1 
10. Install postgresql
11. Brew install node


# API Key Instructions
In order to properly access information from the Movie DB API, you must request an API key at their site. [Follow the link here](https://www.themoviedb.org/settings/api?language=en-US).
Once you have your API key, create a .env file in the project folder. Within the .env file create a variable MOVIES_KEY and set it equal to your API key. Example: `MOVIES_KEY="your key here"` 
You should now be able to run the project locally, accessing data from the APIs. 

In addition to the API key, you will need a key for your DATABASE url and a SECRET key.
For the database URL, an option your have to create your database URL is creating a Heroku account, and a database. Run the following commands to obtain a database URL: 
1. `heroku addons:create heroku-postgresql:hobby-dev`
2. `heroku config (copy output)`
3. `Export DATABASE_URL='copy-paste-value-in-here`
Then you will add this key, Example: `DATABASE_URL="your DB url here"`, in your .env file.
Make sure to add this: Example: `SECRET_KEY="your secret key here"` as well. 

These secret keys must be put into your .env file to keep the information private. Since when you clone my github repo, my .env file will not be provided for you, you must create your own .env file within your project folder. The DB URL key will allow access to the DB URL in order to connect with the database you have created. 

# Questions
***a.	What are at least 3 technical issues you encountered with your project? How did you fix them?***

(1) A big issue that I had at the beginning of the project was when I was trying to render the logged in user's reviews on React. I was able to successfuly send over the list of dictionaries to React, using a `fetch`, in order to get the user's reviews. However, I could see in the terminal that when the `fetch` line ran, the page kept rerendering. After going to the group meeting to work on the project, the professor informed me to look back at the specs and consider looking at `useEffect()` to fetch. I found a useful like that explaoned that using an empty arry with use effect, will allow for it to run once after inital rendering. [This link helped.](https://www.w3schools.com/tags/att_input_required.asp)

(2) An issue is that the user was able to input a comment, without having to input a rating. However, from the specs I noticed that that was not supposed to be a valid submissons. I wanted the form to only allow for submission if at the least a rating was being input. After some google searches I found that the the HTML inptut tag provides a `required` attrubute, which is perfect for what I needed. It also provides a user friendly warning if the requirements are not being met. [This link helped provide me the syntax.](https://www.w3schools.com/tags/att_input_required.asp)
      
(3) Another issue was keeping the input for the rating to be a number, and only a number from 1-10. For this I found that `number` is an input type, which now only allowed for a number to be put into the form. Then I realized that I needed a range from only 1-10. Instead of using the `range` type for input, I simply provided a min and max for the range of the number.[This linked helped with validation.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/range) 

***b. ○	What was the hardest part of the project for you, across all milestones? What is the most useful thing you learned, across all milestones?***

Working on this milestone challenged me exactly how I expected it to. While having basic knowledge of database concepts, it helped slightly to understand the concepts of schemas/relations. While working through the planning process, it felt like maybe it would be more straightforward than it actually was for me. Learning how to use flask-login felt very confusing and took many google searches, however i was able to get down the basic concepts. Flask-login felt like the first hurddle of this project. After that, passing the same movie id from my moviesDB file; then querying for that movie ID within the database, and displaying those elements was the hardest part of this project. I had to try many different things and luckily I was able to display the desired content, which corresponds to the movie where the comment was left. However, getting the correct content for each movie took a lot of trail and error as well.


Other references: 
Worked with Chihumeya, for asscessing same movie ID which exists in the DB table. 