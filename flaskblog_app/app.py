from datetime import datetime
from flask import Flask, render_template, url_for
app = Flask(__name__) 

tday =datetime.today().strftime('%d-%m-%Y-%H:%M:%S')

posts = [
    {
        'author':'Admin',
        'title':'Blog Post',
        'content':'Post content',
        'date_posted':tday
    },
    {
        'author':'Admin',
        'title':'Blog Post 2',
        'content':'Post content update',
        'date_posted':tday
    }
]
        
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
    
