
# How to run this code, by me =)


Note this is a dev environment, setup for production is completely different

Prerequisites: Python

Open up a CMD window and type:
[
    pip install quart
    pip install Flask-mail
    pip install werkzeug
    pip install requests
    pip install telethon
    pip install mysql-connector
]
(you can also run pip install -r requirements.txt, but you must be in the folder 'project' is in(it has requirements.txt, and this file) )

I don't recommend setting up a db for this, so go in the search.py file and look for 'db_add()' which is at the very bottom
above the return statement and comment it out buy putting ( # ) in front of it, and save.

After all these;

Open up Powershell, navigate to the folder 'project' is in ( not into the projects folder )  and type these:
[
    $env:QUART_APP = 'project'
    $env:QUART_DEBUG = 1
    Quart run
]

From there the server is live at localhost:5050.
You should see a bunch of text with that in it, go to that url.
An internet connection is needed to make tests on the search api.


Let me know of any errors!