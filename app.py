from flask import Flask
myapp = Flask(__name__)

@myapp.route("/")
def homepage():
    return 'Hello there!'

if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)


