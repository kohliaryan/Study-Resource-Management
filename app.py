from flask import Flask
import view

def create_app():
    app = Flask(__name__)
    view.create_view(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)