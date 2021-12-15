from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():  # put application's code here
    return render_template("home.html")

@app.route('/coffee')
def Coffee_page():
    items = [
        {'id': 1, 'name': 'flat white', 'price': 5},
        {'id': 2, 'name': 'lattee',  'price': 4.5},
        {'id': 3, 'name': 'long black', 'price': 4}
    ]
    return render_template("coffee.html",items=items)

if __name__ == '__main__':
    app.run()

