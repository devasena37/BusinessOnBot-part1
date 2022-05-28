
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import sqlite3  
  
app = Flask(__name__)  
@cross_origin()
@app.route("/" ,methods=[ "POST","GET"])  
def index():  
    return render_template("index.html");  

@app.route("/view", methods=[ "POST","GET"])  

def view():  
    con = sqlite3.connect("bank1.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    n=cur.execute("SELECT COUNT() FROM bank1").fetchone()[0]

    allrows=cur.execute("select * from bank1 order by ifsc asc").fetchall()
  
    assert n == len(allrows)  
    rows = cur.fetchall()  
    return render_template("view.html",rows = allrows)  
        
  
if __name__ == "__main__":  
    app.run(debug = True)  