from flask import Flask
from routes import book_routes, member_routes

app = Flask(__name__)

# Register routes
app.register_blueprint(book_routes)
app.register_blueprint(member_routes)

if __name__ == "__main__":
    app.run(debug=True)
