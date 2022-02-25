import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

print(os.getenv("DATABASE_URL"), flush=True)
# Set up database
engine = create_engine("postgresql://bzrmofcuuoloaq:909c3613d6663b3dec7e203dbb1df52b963bc208f5b6fd1b456d23240c459030@ec2-176-34-114-78.eu-west-1.compute.amazonaws.com:5432/d79jvrpipc3rm1")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"

if __name__ == '__main__':
    app.run()
