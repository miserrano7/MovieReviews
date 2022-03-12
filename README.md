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
We have to install Nodes_modules by running "npm ci" to get react to work properly.

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
Now you should be able to open up the source code within your own IDE. Below you will find API Key Instrustions that need to be followed in order to be able to access data. From here you are able to modify the project, and eventually run your project locally with the command `npm run build` and then `python3 app.py` .

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

(2) Another issue I had was to setting up my input box to allow the user to edit a rating. Initially, before adding logic to the `onChange` function I was 
unable to change the number or even give any input. I realized that I had to fix my onclick function first to be able to get what the user is inputting. For handling the onClick function, I had to map through the data to check which rating was being changed. Once I set the edit the user was finally able to chnage the rating. [This link helped to understand onchange better.](https://sebhastian.com/react-onchange/#:~:text=In%20React%2C%20onChange%20is%20used,the%20value%20of%20input%20elements.&text=Now%20whenever%20you%20type%20something,passed%20into%20the%20onChange%20prop.)
      
(3) Another issue I had was that I was unable to run "npm run build" to update my .js files I changed. I compared this project with the hw7 and realized that I was missing node_modules to get react to work properly. Using the command 'npm ci' helped me install those modules within this project. After I did that I was able to run my code using npm run build, and then python3 app.py.

***b. ○	What was the hardest part of the project for you, across all milestones? What is the most useful thing you learned, across all milestones?***

The hardest part over the three milestones is working with react. Understanding how to work with components and states is a tricky concept for me. In specific, it was challenging understanding how to send data from Flask server to React, and vice versa, and being able to manipulate the data. I found it hard working with states and changing their values to our needs for this project. In addition to that, working with a database is something new for me so it's been hard getting everything down.

The most useful thing has been working with new technology. In previous classes we never really got to build something that was so useful over so many concepts. Although it has been a lot of work, I think we have been able to learn a lot of valuable things. For example, in particular I was able to learn how to work with a framework and using its libraries to build on top of exisiting code, like with the login user functionality. I also think learning about react is very useful too, although that knowledge may need to get developed a bit further.

Other references: 
Worked with Chihumeya, for deletion on click. 