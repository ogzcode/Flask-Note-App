from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def main():
    conn= get_db_connection()
    notes = conn.execute("SELECT * FROM notes").fetchall()
    conn.close()
    return render_template("home.html", notes=notes)


@app.route('/create')
def create():
    return render_template("create.html")
