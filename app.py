import data_diff
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def get_database_connection(database_property):
    return data_diff.connect(database_property)


if __name__ == '__main__':
    app.run(debug=True)
