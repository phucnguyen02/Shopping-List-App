
import sqlite3
from flask import Flask, session, render_template, request, g, jsonify, url_for, redirect, json

app = Flask(__name__)
app.secret_key = "sdfdszogfikdzjfoisdzjfilkers"


@app.route("/", methods=["POST", "GET"])
def index():
    data = get_db()
    return render_template("index.html", all_data=data)


@app.route("/items", methods=["POST", "GET"])
def items():
    if request == "POST":
        return redirect(url_for('index'))
    id = request.args.get("id")
    data = get_items_db(id)
    return render_template("items.html", all_data=data)


@app.route("/add_list", methods=["POST"])
def add_list():
    db = g._database = sqlite3.connect('shopping_lists.db')
    cursor = db.cursor()
    new_name = request.get_json()[0]['name']
    cursor.execute("INSERT INTO shopping_lists (name) VALUES (:insert_name)", {
        'insert_name': new_name})
    db.commit()
    data = get_db()
    return render_template("index.html", all_data=data)


@app.route("/add_item", methods=["POST"])
def add_item():
    db = g._database = sqlite3.connect('shopping_lists.db')
    cursor = db.cursor()
    print("Data received: ", request.get_json()[0])
    new_name = request.get_json()[0]['name']
    list_id = request.get_json()[0]['id']
    cursor.execute("INSERT INTO shopping_items (list_id, name) VALUES (:id, :insert_name)", {
        'id': list_id, 'insert_name': new_name})
    db.commit()
    data = get_items_db(list_id)
    return render_template("items.html", all_data=data)


@app.route("/edit_list", methods=["POST"])
def edit_list():
    db = g._database = sqlite3.connect('shopping_lists.db')
    cursor = db.cursor()
    id = request.get_json()[0]['id']
    new_name = request.get_json()[0]['newName']
    cursor.execute("""UPDATE shopping_lists
                  SET name= :rename
                  WHERE id = :id""", {'rename': new_name,
                                      'id': id})
    db.commit()
    data = get_db()
    return render_template("index.html", all_data=data)


@app.route("/edit_item", methods=["POST"])
def edit_item():
    db = g._database = sqlite3.connect('shopping_lists.db')
    cursor = db.cursor()
    item_id = request.get_json()[0]['item_id']
    list_id = request.get_json()[0]['list_id']
    new_name = request.get_json()[0]['newName']
    cursor.execute("""UPDATE shopping_items
                  SET name= :rename
                  WHERE item_id = :item_id AND list_id = :list_id""", {'rename': new_name,
                                                                       'item_id': item_id, 'list_id': list_id})
    db.commit()
    data = get_items_db(list_id)
    return render_template("items.html", all_data=data)


@app.route("/remove_list", methods=["POST"])
def remove_list():
    db = g._database = sqlite3.connect('shopping_lists.db')
    cursor = db.cursor()
    id = request.get_json()[0]['id']
    cursor.execute("""DELETE FROM shopping_lists
                  WHERE id = :id""", {'id': id})
    db.commit()
    data = get_db()
    return render_template("index.html", all_data=data)


@app.route("/remove_item", methods=["POST"])
def remove_item():
    db = g._database = sqlite3.connect('shopping_lists.db')
    cursor = db.cursor()
    item_id = request.get_json()[0]['item_id']
    list_id = request.get_json()[0]['list_id']
    cursor.execute("""DELETE FROM shopping_items
                  WHERE item_id = :item_id AND list_id = :list_id""", {'item_id': item_id, 'list_id': list_id})
    db.commit()
    data = get_items_db(list_id)
    return render_template("items.html", all_data=data)


@app.route("/search_item", methods=["POST"])
def search_item():
    db = g._database = sqlite3.connect('shopping_lists.db')
    cursor = db.cursor()
    search_name = request.get_json()[0]['name']
    list_id = request.get_json()[0]['id']
    if not search_name:
        return items()
    cursor.execute(
        "SELECT * FROM shopping_items WHERE name LIKE :search_name AND list_id = :list_id", {'search_name': '%' + search_name + '%', 'list_id': list_id})
    data = [str(val[0]) + "/ " + str(val[1]) + ": " + val[2]
            for val in cursor.fetchall()]
    return render_template("items.html", all_data=data)


def get_db():
    db = getattr(g, '_database', None)
    db = g._database = sqlite3.connect('shopping_lists.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM shopping_lists")
    return [str(val[0]) + ": " + val[1] for val in cursor.fetchall()]


def get_items_db(id):
    db = getattr(g, '_database', None)
    db = g._database = sqlite3.connect('shopping_lists.db')
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM shopping_items WHERE list_id = :id", {'id': id})
    return [str(val[0]) + "/ " + str(val[1]) + ": " + val[2] for val in cursor.fetchall()]


@ app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()
