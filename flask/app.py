from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def login():
        return render_template('sample.html')

@app.route('/link')
def sagar():
    return render_template('redirect.html')
if __name__ == '__main__':
   app.run(debug = True)