from flask import Flask, request, render_template, flash, redirect, render_template, jsonify
import psycopg2
from flask_debugtoolbar import DebugToolbarExtension 
from models import db, connect_db, Cupcake




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "topsecret1"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)



@app.route('/')
def home_page():
    return render_template('home.html')
    
    
@app.route('/api/cupcakes', methods=["GET"])
def get_data_all():
    '''get data about all cupcakes'''
    cupcakes = Cupcake.query.all()
    all_cupcakes = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:id>', methods=["GET"])
def get_cupcake_details(id):
    '''get data on single cupcake'''
    cupcake= Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())
    
@app.route('/api/cupcakes', methods = ["POST"])
def create_cupcake():
    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], rating=request.json["rating"], photo_url=request.json["photo_url"])
    db.session.add(new_cupcake)
    db.session.commit()
    response_json= jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.photo_url = request.json.get('photo_url', cupcake.photo_url)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


    
@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")
     
