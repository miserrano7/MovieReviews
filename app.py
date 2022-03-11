from curses.ascii import DEL
import os
import flask
from flask import Flask, render_template
from moviesDB import get_movie_data
#from wiki_info import get_wiki_link
from dotenv import load_dotenv, find_dotenv
from flask import request, flash
from models import db, Users, Reviews
from flask_login import LoginManager, login_manager, current_user
from flask_login import login_required, login_user, logout_user


load_dotenv(find_dotenv())  # This is to load your API keys from .env

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# Point SQLAlchemy to your Heroku database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL1")
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

#start adding routes here 

# set up a separate route to serve the index.html file generated
# by create-react-app/npm run build.
# By doing this, we make it so you can paste in all your old app routes
# from Milestone 2 without interfering with the functionality here.
bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

# route for serving React page
@bp.route("/edits")
def index():
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    return flask.render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("login.html")    

    #adding routes from milestone2
# adding different routes for login and register
# login page
@app.route("/login_info", methods=["GET", "POST"])
def login_info():
    username = request.form.get("username")
    user = Users.query.filter_by(username=username).first()
    if user:
        login_user(user)
        return flask.redirect(flask.url_for("main"))
    elif user is None:
        flash("Username does not exist or is incorrect, try again.")
    return flask.redirect(flask.url_for("home"))


# register page
@app.route("/register_info", methods=["GET", "POST"])
def register_info():
    # if there is a post then use this otherwise render template
    if flask.request.method == "POST":
        username = request.form.get("username")
        newUser = Users(username=username)
        user = Users.query.filter_by(username=username).first()
        # if the user is found then it's already in the database
        # https://www.geeksforgeeks.org/python-string-isspace-method/#:~:text=Python%20String%20isspace()%20is,'%20'%20%E2%80%93%20Space
        checkingSpace = username.isspace()

        if user:
            flash("user already exists")
        elif user is None:
            if checkingSpace == False:
                db.session.add(newUser)
                db.session.commit()
                return flask.redirect(flask.url_for("home"))
    return render_template("register.html")


# main page
@app.route("/main", methods=["GET", "POST"])
@login_required
def main():
    titles, tagline, genres, image, urlLink, randomPICK = get_movie_data()
    if flask.request.method == "POST":
        rating = request.form.get("rating")
        comment = request.form.get("comment")
        movieid = request.form.get("movieid")
        user_name = current_user.username

        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_adding_objects.htm
        # adding both the rating and comment on the samw row/at the same time
        newData = Reviews(
            comment=comment, rating=rating, movieIDs=movieid, user_name=user_name)
        db.session.add(newData)
        db.session.commit()
        return flask.redirect(flask.url_for("main"))

    queryRatings = Reviews.query.filter_by(movieIDs=randomPICK).all()
    num = len(queryRatings)

    allRatings = [queryRatings[tple].rating for tple in range(num)]
    allComments = [queryRatings[tple].comment for tple in range(num)]
    allUsers = [queryRatings[tple].user_name for tple in range(num)]

    lenR = len(allRatings)
    lenC = len(allComments)
    lenU = len(allUsers)

    return render_template(
        "home.html",
        titles=titles,
        tagline=tagline,
        genres=genres,
        image=image,
        urlLink=urlLink,
        randomPICK=randomPICK,
        allComments=allComments,
        allRatings=allRatings,
        allUsers=allUsers,
        lenR=lenR,
        lenC=lenC,
        lenU=lenU)

#need to load the comments/ratings for each specific user
@app.route("/userReviews")
@login_required
def userReviews():
    #get the user id then for all those ids get that!!will get the whole tuple, then access the elemts at 
    #comments and at ratings then allow for changes there somehow 
    user_name=current_user.username
    queryUser = Reviews.query.filter_by(user_name=user_name).all()
    num = len(queryUser) 
    #accessing all columns from reviews table for this specific logged in user
    allIds =[queryUser[tple].id for tple in range(num)]
    allMovieIds= [queryUser[tple].movieIDs for tple in range(num)]
    allComments = [queryUser[tple].comment for tple in range(num)]
    #only need the length of one since they're all the same length
    num2= len(allComments)
    allR = [queryUser[tple].rating for tple in range(num)]
    
    #https://stackoverflow.com/questions/31181830/adding-item-to-dictionary-within-loop
    #creating list of dictionaries to jsonify and fetch from app.js file 
    test = []
    for i in range(0,num2):
        di = {'id': allIds[i],'movieid': allMovieIds[i],'comments':  allComments[i], "ratings":allR[i]} 
        test.append(di)
    return flask.jsonify(test)

@app.route("/newRoute", methods=["POST"])  
def update():
    #function to update the DB based on fetch sent from react 
    data= flask.request.json
    print(data)
    #want to query existing data in DB
    queryreviewID = Reviews.query.filter_by(id=id).all()
    num = len(queryreviewID)
    allUserData =[queryreviewID[tple].id for tple in range(num)]
    num2= len(allUserData)
    #cast id as INT !!!!!!! 
    for i in range(num2):
        if data[i]["id"] not in allUserData:
            newData = Reviews(
            comment=comment, rating=rating, movieIDs=movieid, user_name=user_name)
            db.dession.delete()
            db.session.commit()
    return ""

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return flask.redirect(flask.url_for("home"))

app.register_blueprint(bp)

app.run()
