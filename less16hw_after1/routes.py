import json, db
from less16hw_after1 import models
from flask import current_app as app, request, jsonify


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