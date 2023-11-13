from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated user data for demonstration purposes
users = [
    {'username': 'user1', 'password': 'password1'},
    {'username': 'user2', 'password': 'password2'}
]

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    for user in users:
        if user['username'] == username and user['password'] == password:
            return f'Welcome, {username}!'
    
    return 'Invalid username or password. Please try again.'

if __name__ == '__main__':
    app.run(debug=True)
