import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/hello', methods=['GET'])
def say_hello():

    name = request.args['name']
    return f"Hello, {name}!"

@app.route('/goodbye', methods=['POST'])
def say_goodbye():
    
    name = request.form['name']
    return f"Goodbye, {name}!"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    msg = request.form['message']

    return f'Thanks {name}, you sent: "{msg}"'

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']

    return f'I am waving at {name}!'

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    vowel_count = sum([1 for char in text if char in 'aeiou'])

    return f'There are {vowel_count} vowels in "{text}"'

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

