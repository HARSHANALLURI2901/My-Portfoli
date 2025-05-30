from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('port.html')

@app.route('/health')
def health():
    return render_template('health.html')

@app.route('/childbirth')
def childbirth():
    return render_template('childbirth.html')

@app.route('/employee')
def employee():
    return render_template('employee.html')

if __name__ == '__main__':
    app.run(debug=True)
