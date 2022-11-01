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
        result = users.add_user(name)

        print(result)

        return result, 200

    else:
        print("Invalid content_type, must be application/json")
        return "Invalid content_type, must be application/json", 405

@app.route('/logout', methods=['POST'])
def logout():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        
        name = find_name(json)
        result = users.remove_user(name)  # data contains associated data

        print(result)

        return result, 200

    else:
        print("Invalid content_type, must be application/json")
        return "Invalid content_type, must be application/json", 405


@app.route('/current', methods=['GET'])
def current():
    return jsonify(current_num = users.return_current()), 200

if __name__ == '__main__':
    app.run(debug=True)