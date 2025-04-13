from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

poll = {
    'question': 'What is your favorite programming language?',
    'options': ['Python', 'JavaScript', 'Java', 'C++'],
    'votes': [0, 0, 0, 0]
}


@app.route('/vote/<int:option_id>')
def vote(option_id):
    if 0 <= option_id < len(poll['options']):
        poll['votes'][option_id] += 1
    return redirect(url_for('index'))
@app.route('/')
def index():
    # Pass enumerated options along with their index
    enumerated_options = list(enumerate(poll['options']))
    return render_template('index.html', poll=poll, enumerated_options=enumerated_options)

if __name__ == '__main__':
    app.run(debug=True)
