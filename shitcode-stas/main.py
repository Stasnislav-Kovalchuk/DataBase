# app.py
from flask import Flask

from controlers.song_controller import song_blueprint
from controlers.playlist_controller import playlist_blueprint
from controlers.user_controller import user_blueprint
from models.session import Base, engine
from controlers.procedure import procedure_bp



Base.metadata.create_all(bind=engine)


app = Flask(__name__)

# Register the user blueprint
app.register_blueprint(song_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(playlist_blueprint)

app.register_blueprint(procedure_bp)

@app.route('/')
def index():
    return "Welcome to the Flask app with Blueprints!", 200


if __name__ == '__main__':
    app.run(debug=True)
