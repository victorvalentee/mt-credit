from flask import Flask
from utils import initialize_database


app = Flask(__name__)


if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)