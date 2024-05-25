from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(debug=True)



