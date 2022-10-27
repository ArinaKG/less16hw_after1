import json, db
from less16hw_after1 import models
from flask import current_app as app, request, jsonify

@app.route('/', methods=['GET', 'POST'])
def users():
    if request.method == "GET":
        result = []
        for user in models.User.query.all():
            result.append(user.to_dict())
        return "Пользователь создан"
    elif request.method == "POST":
        user_data = request.json

        new_user = models.User(**user_data)

        db.session.add(new_user)
        db.session.commit()

        for user in models.User.query.all():
            result.append(user.to_dict())
            result = []

        return jsonify(result), 200


@app.route('/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def user_function(uid):
    if request.method == "GET":
        user = models.User.query.get(uid)
        return jsonify(user.to_dict()), 200
    if request.method == "PUT":
        user_data = request.json
        user = models.User.query.get(uid)
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.age = user_data['age']
        user.email = user_data['email']
        user.role = user_data['role']
        user.phone = user_data['phone']

        db.session.add(user)
        db.session.commit()

        user = models.User.query.get(uid)
        return "Пользователь обновлён"

    if request.method == "DELETE":
        user = models.User.query.get(uid)
        db.session.delete(user)
        db.session.commit()

        return "Пользователь удален"


@app.route('/order/<int:id_order>', methods=['GET', 'PUT', 'DELETE'])
def page_order_by_id(id_order):
    if request.method == "GET":
        res = Utils()
        return jsonify(res.get_by_id(Order, id_order))
    elif request.method == 'PUT':
        content = request.json
        Utils().update_data_order(Order, content, id_order)
        return "Заказ обновлён"
    else:
        Utils().delete_data_in_bd(Order, id_order)
        return "Заказ удален"