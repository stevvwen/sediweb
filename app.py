from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/life')
def life():
    return render_template('life.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404



if __name__ == '__main__':
    app.run()

