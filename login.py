from flask import Flask,request,render_template, make_response
app = Flask(__name__)

users=["luigi","gianni","maria"]
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] in users:
            resp=make_response(render_template("hallo.html",nome=request.form['username']))
            resp.set_cookie("utente",request.form['username'])
            return resp
        else:
            return "Non autorizzato"
    else:
        return render_template("login.html")
		
@app.route('/id', methods=['GET'])
def id():
    yourname=request.cookies.get("utente")
    return "Sei "+yourname;
