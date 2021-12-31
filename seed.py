from app import app
from models import db, Cupcake


# db.drop_all()
db.create_all()

vanilla = Cupcake(
    flavor="vanilla",
    size="medium",
    rating= 6.5
)

chocolate = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    photo_url="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

red_velvet = Cupcake(
    flavor="red_velvet",
    size="large",
    rating=8,
)

strawberry = Cupcake(
    flavor="strawberry",
    size="medium",
    rating=7,
)

db.session.add(vanilla)
db.session.add(chocolate)
db.session.add(red_velvet)
db.session.add(strawberry)

db.session.commit()