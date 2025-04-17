from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/licencjat')
def sus():
    return "The big amogus brigijk iroeaerg f. "  

if __name__ == '__main__':
    app.run()