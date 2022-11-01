from flask import Flask, render_template, request, redirect, jsonify
from Users import Users, find_name

app = Flask(__name__)

users = Users()

@app.route('/')
def index():
    return redirect('/info')

@app.route('/info')
def server_info():
    return render_template('info.html')

@app.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        
        name = find_name(json)
        users.add_user(name)

        print(users.return_current(), name)

        return 'User was added.', 204

    else:
        print("Invalid content_type, must be application/json")
        return None, 204

@app.route('/logout', methods=['POST'])
def logout():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        
        name = find_name(json)
        result, Sdata = users.remove_user(name)  # data contains associated data

        return 'User was removed.', 204

    else:
        print("Invalid content_type, must be application/json")
        return None


@app.route('/current', methods=['GET'])
def current():
    return jsonify(users.return_current())

if __name__ == '__main__':
    app.run(debug=True)