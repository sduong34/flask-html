from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('p1_about.html')

@app.route('/services')
def services():
    return render_template('p2_services.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)