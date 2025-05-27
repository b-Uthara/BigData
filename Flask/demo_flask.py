from flask import Flask
app = Flask(__name__)
@app.route('/')
def home_page():
    return 'Welcome to the python course'
if __name__ == '__main__':
    app.run(debug=True)