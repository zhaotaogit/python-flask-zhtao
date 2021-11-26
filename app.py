import random

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    lst = ["赵德雨","周锡阳","周增远","张亚龙","朱德全"]
    name = random.choice(lst)
    return f"<h1>{name}全都会!</h1>"

if __name__ == '__main__':
    app.run(debug=True)