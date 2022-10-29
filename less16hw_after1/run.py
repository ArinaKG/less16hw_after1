from Flask import flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.init_app(app)
        db.create_all()
        from . import migrate
        migrate.load_users('data/users.json')

    app.app_context().push()
    return app


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


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)