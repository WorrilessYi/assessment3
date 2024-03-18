from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
csrf = CSRFProtect(app)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    return render_template('data_collection.html')


# Define Flask Routes

if __name__ == '__main__':
    app.run(debug=True)
