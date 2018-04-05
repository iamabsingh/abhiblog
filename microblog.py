
from app import app, db
from app.models import User, Post

#app=Flask(__name__)
@app.shell_context_processor
def make_shell_context():
    from sqlalchemy.testing import db
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == "__main__":
    app.run(port=8000, debug=True, use_reloader=True)