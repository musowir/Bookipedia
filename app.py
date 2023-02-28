from flask import Flask, render_template

app = Flask(__name__)

@app.before_first_request
def do_something_on_startup():
    # Add code here to run on server startup
    
    pass

@app.route('/')
def home():
    # Add code here for your home page
    return render_template('index.html')

@app.route('/recommendations')
def recommendations():
    # Add code here to calculate and return recommended books
    pass

if __name__ == '__main__':
    app.run()
