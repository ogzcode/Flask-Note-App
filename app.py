from flask import Flask, render_template, request, redirect, flash, url_for, abort
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = "rm&jLg2wKK12"

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_note(id):
    conn = get_db_connection()

    note = conn.execute("SELECT * FROM notes WHERE id = ?", (str(id))).fetchone()
    conn.close()

    if not note:
        abort(404)

    return note

@app.route('/')
def main():
    conn= get_db_connection()
    notes = conn.execute("SELECT * FROM notes").fetchall()
    conn.close()
    return render_template("home.html", notes=notes)


@app.route('/create', methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Title is required!!")
        elif not content:
            flash("Content is required!!")
        else:
            conn = get_db_connection()
            conn.execute("INSERT INTO notes (title,content) VALUES (?,?)", (title, content))
            conn.commit()
            conn.close()

            return redirect(url_for("main"))
        
    return render_template("create.html")

@app.route('/<int:id>/delete', methods=["POST"])
def delete(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM notes WHERE id = ?", (str(id)))
    conn.commit()
    conn.close()
    
    return redirect(url_for("main"))
