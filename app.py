from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<a href=/> Home </a>' \
           '<a href=/picture> Pictures </a>' \
           '<a href=/bio> Biography </a>'

@app.route('/picture')
def picture():
    return '<a href=/> Home </a>' \
           '<a href=/picture> Pictures </a>' \
           '<a href=/bio> Biography </a>'\
           '<img src=https://i.ytimg.com/vi/J7ruuAffug8/maxresdefault.jpg></img>'

@app.route('/bio')
def biography():
    return '<a href=/> Home </a>' \
           '<a href=/picture> Pictures </a>' \
           '<a href=/bio> Biography </a>' \
           '<p> Hæ ég heiti eyþór og ég er galdrakall </p>'



if __name__ == '__main__':
    app.run()
