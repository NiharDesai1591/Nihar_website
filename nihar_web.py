from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')  # Renders the CV page with the embedded PDF

@app.route('/talks')
def talks():
    return render_template('talks.html')  # Renders the talks page

if __name__ == '__main__':
    app.run(debug=True)
