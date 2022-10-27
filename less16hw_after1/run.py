import Flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.init_app(app)
        db.create_all()
        from . import migrate
        migrate.load_users('data/users.json')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)