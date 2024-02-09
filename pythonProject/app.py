from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import random
import string

app = Flask(__name__)
Bootstrap(app)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        length = int(request.form['length'])
        if 6 <= length <= 100:
            password = generate_password(length)
            return render_template('index.html', password=password)
        else:
            return render_template('index.html', error='Please enter a valid number between 6 and 100 for password length.')
    except ValueError:
        return render_template('index.html', error='Please enter a valid number for password length.')

if __name__ == '__main__':
    app.run(debug=True)
