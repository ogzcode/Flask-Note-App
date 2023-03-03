from flask import Flask,render_template

app = Flask(__name__)

notes = [
    {
        "id": 1,
        "title": "Do Home Work",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit.Esse sapiente ullam consectetur placeat ex amet maxime non accusamus saepe eaque""",
        "date": "01.03.2023"
    },
    {
        "id": 2,
        "title": "Do Home Work",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit.Esse sapiente ullam consectetur placeat ex amet maxime non accusamus saepe eaque""",
        "date": "01.03.2023"
    },
    {
        "id": 3,
        "title": "Do Home Work",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit.Esse sapiente ullam consectetur placeat ex amet maxime non accusamus saepe eaque""",
        "date": "01.03.2023"
    },
    {
        "id": 4,
        "title": "Do Home Work",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit.Esse sapiente ullam consectetur placeat ex amet maxime non accusamus saepe eaque""",
        "date": "01.03.2023"
    },
    {
        "id": 5,
        "title": "Do Home Work",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit.Esse sapiente ullam consectetur placeat ex amet maxime non accusamus saepe eaque""",
        "date": "01.03.2023"
    },
    {
        "id": 6,
        "title": "Do Home Work",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit.Esse sapiente ullam consectetur placeat ex amet maxime non accusamus saepe eaque""",
        "date": "01.03.2023"
    },
    {
        "id": 7,
        "title": "Do Home Work",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit.Esse sapiente ullam consectetur placeat ex amet maxime non accusamus saepe eaque""",
        "date": "01.03.2023"
    },
    {
        "id": 8,
        "title": "Do Home Work",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit.Esse sapiente ullam consectetur placeat ex amet maxime non accusamus saepe eaque""",
        "date": "01.03.2023"
    }
]

@app.route('/')
def main():
    return render_template("home.html", notes=notes)

@app.route('/create')
def create():
    return render_template("create.html")