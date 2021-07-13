import time
from time import sleep
import os
import ast
import asyncio
import mysql.connector 
from mysql.connector import Error
import quart
from quart import jsonify, request, Blueprint, make_response, render_template, session
from project.search import search, db_add
from random import randint
...
#please set username, password, db, host and port properties to their appropriate values
host='localhost'
port='3306'
usrname='usrname'
passw='password'
dbase='client'
mid = "JrkrZv28154991768076"
mkey = "trK0LKatZUvyq7Ud"
main_url = "https://telesearch.online"
amount_for_membership = 100
paytmParams = dict()
asyncio.set_event_loop(asyncio.new_event_loop())
checksum = ''

async def add_code(code):
    conn = mysql.connector.connect(
        user=usrname, 
        password=passw, 
        host=host, 
        port=port, 
        db=dbase
        )
    mycursor = conn.cursor()
    sql = "INSERT INTO paidusers (code) VALUES (%s)"
    val = str(code)
    mycursor.execute(sql, val)
    conn.commit()
 
main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
async def home():
    return await render_template('index.html')

 
@main.route('/api/v1/results', methods=['POST'])
async def checking():

    async def check(kwarg):
        
        conn = mysql.connector.connect(
            user=usrname, 
            password=passw, 
            host=host, 
            port=port, 
            db=dbase
            )
        mycursor = conn.cursor()
        reslist = []
        for i in reslist:
            mycursor.execute("SELECT * FROM results WHERE title LIKE "+str(kwarg)+"")
        reslist = []
        for result in mycursor:
            reslist.append([result])
        conn.commit()
        return reslist


    print('we got here')
    form  = (await request.form)
    if form.get("query"):
        search_term = form['query']
        print('we got here also')
        if session.get("is_loggedin"):
            reslist = check(search_term)
            print('we got here as well')
            if reslist:
                unique = []
                seen = set()
                for x in reslist:
                    if x not in seen:
                        unique.append(x)
                        set.add(x)
                res = str(unique)
                res.replace("{'channel' : ", '')
                res.replace('}', '')
                res.replace("'", '')
                reslist = ast.literal_eval(res)
                return await render_template('index.html', reslist=reslist, search2='Showing results for '+search_term, display = 'block')
            else:
                reslist = await search(search_term, 7)
                unique = []
                seen = set()
                for x in reslist:
                    if x not in seen:
                        unique.append(x)
                        set.add(x)
                res = str(unique)
                res.replace("'", '')
                reslist = ast.literal_eval(res)
                return make_response(render_template('index.html', reslist=reslist, search2='Showing results for '+search_term, display = 'block'))
 

        else:
            reslist = await search(search_term)
            unique = []
            seen = set()
            for x in reslist:
                if x not in seen: 
                    unique.append(x)
                    seen.add(x)
            res = str(unique)
            res.replace("'", '')
            reslist = ast.literal_eval(res)
            print(reslist)
            # reslist = reslis[0, 16]
            return await render_template('index.html', reslist=reslist, search2='Showing results for '+search_term, display = 'block')

    else:
        reslist =  "Error: Please enter a search term to use our services!"
        return await render_template('index.html', reslist = reslist)



@main.route('/submit_request', methods=['POST'])    
async def sendmessage():
    from . import send_mail
    if request.method == 'POST':
        send_mail(await request.form['email'], await request.form['message'])
        return await render_template('index.html')



@main.route('/support')
async def support():
    return await render_template('support.html')


@main.route('/paytm')
async def payt():
    return await render_template('buy-page.html')

@main.route('/paytm_checkout', methods=['GET','POST'])
async def pay():
    if request.method == 'POST':
        #logic for paytm goes here
        print('.')
    return await render_template('buy-page.html')

@main.route('/paytm_final', methods=['POST'])
async def pcall():
    print('.')
    #callback_url logic
            
