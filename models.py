from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    

class Cupcake(db.Model):
    
    __tablename__ = "cupcakes"
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.Text,
                     nullable=False)
    size = db.Column(db.Text,
                     nullable=False)
    rating = db.Column(db.Float)
    photo_url = db.Column(db.Text, default="https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg")
    
    
    def serialize(cupcake):
        """Serialize a dessert SQLAlchemy obj to dictionary."""
        return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "photo_url":cupcake.photo_url
    }


   