from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from models import Schema
from service import Habit_Service, User_Service

app = Flask(__name__)
app.secret_key = "12341234"


@app.route("/")
@app.route('/login', methods=["GET", "POST"])
def login_page(self=None) -> 'html':

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        info = User_Service().check_user(username, password)

        if info is not None:
            if info[2] == username and info[3] == password:
                session['loginsuccess'] = True
                session['user_id'] = info[0]
                session['name'] = info[1]
                return redirect(url_for('entry_page'))
        else:
            return redirect(url_for('register_page'))

    return render_template('login.html')


@app.route('/logout', methods=["POST"])
def logout() -> 'str':
    session.pop('loginsuccess')
    return "You are successfully logged out!"


@app.route('/new', methods=["GET", "POST"])
def register_page() -> 'html':
    if request.method == "POST":
        params = {"Name": request.form.get('name'), "Username": request.form.get('username'),
                  "Password": request.form.get('password')}
        create_obj = User_Service().create_user(params)
        print('user created:', create_obj)
        return redirect('/login')
    return render_template('register.html')


@app.route('/entry', methods=["GET", "POST"])
def entry_page() -> 'html':
    if session['loginsuccess']:
        user = session['name']
        title = 'Welcome ' + user + '! - Create your own Habit Tracker!'
        return render_template('entry.html', the_title=title)


@app.route("/create_habit", methods=["POST"])
def create_habit():
    params = {"Title": request.form.get('title'), "Description": request.form.get('description'),
              "UserId": session['user_id']}
    Habit_Service().create_habit(params)
    return redirect('/log_habit')


@app.route("/mark_habit", methods=["POST"])
def mark_habit():
    data = request.get_json()
    user_id = session['user_id']
    if Habit_Service().update_habit(user_id, data):
        return {"Status": 'Success'}


@app.route("/log_habit", methods=["GET"])
def list_habit() -> 'html':
    user_id = session['user_id']
    result = Habit_Service().list_all_habit(user_id)
    headings = ("Habit", "Description")
    if len(result):
        list_msg = 'Your Habits are :'
    else:
        list_msg = 'No Habits listed yet, create one now! '

    return render_template('result.html', headings=headings, data=result,
                           the_title='Habitika - Your own Habit Tracker!', the_list=list_msg)


@app.route("/habitika/<item_id>", methods=["GET"])
def get_item(item_id):
    return jsonify(Habit_Service().list_by_id(item_id))


@app.route("/habitika/<item_id>", methods=["PUT"])
def update_item(item_id):
    return jsonify(Habit_Service().update_habit(item_id, request.get_json()))


@app.route("/habitika/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    return jsonify(Habit_Service().delete(item_id))


if __name__ == "__main__":
    Schema()
    app.run(debug=True, host='127.0.0.1', port=8888)
