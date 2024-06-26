#!/usr/bin/python3
from flask import Flask, make_response, render_template, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import json
import random
import sqlite3
import sqlitedb

sqlitedb.connectDB()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///JoyOfCoding.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)
mm = Marshmallow(app)

db.Model.metadata.reflect(db.engine)

class Episodes(db.Model):
    __tablename__ = 'Episodes'
    __table_args__ = { 'extend_existing': True }
    index = db.Column(db.Integer, index=True)
    Thumbnail = db.Column(db.Text)
    Title = db.Column(db.Text, primary_key=True)
    Season = db.Column(db.Integer)
    Episode = db.Column(db.Integer)
    Youtube = db.Column(db.Text)
    Black_Gesso = db.Column('Black Gesso', db.Integer)
    Bright_Red = db.Column('Bright Red', db.Integer)
    Burnt_Umber = db.Column('Burnt Umber', db.Integer)
    Cadmium_Yellow = db.Column('Cadmium Yellow', db.Integer)
    Dark_Sienna = db.Column('Dark Sienna', db.Integer)
    Indian_Red = db.Column('Indian Red', db.Integer)
    Indian_Yellow = db.Column('Indian Yellow', db.Integer)
    Liquid_Black = db.Column('Liquid Black', db.Integer)
    Liquid_Clear = db.Column('Liquid Clear', db.Integer)
    Midnight_Black = db.Column('Midnight Black', db.Integer)
    Phthalo_Blue = db.Column('Phthalo Blue', db.Integer)
    Phthalo_Green = db.Column('Phthalo Green', db.Integer)
    Prussian_Blue = db.Column('Prussian Blue', db.Integer)
    Sap_Green = db.Column('Sap Green', db.Integer)
    Titanium_White = db.Column('Titanium White', db.Integer)
    Van_Dyke_Brown = db.Column('Van Dyke Brown', db.Integer)
    Yellow_Ochre = db.Column('Yellow Ochre', db.Integer)
    Alizarin_Crimson = db.Column('Alizarin Crimson', db.Integer)
    Apple_Frame = db.Column('Apple Frame', db.Integer)
    Aurora_Borealis = db.Column('Aurora Borealis', db.Integer)
    Barn = db.Column(db.Integer)
    Beach = db.Column(db.Integer)
    Boat = db.Column(db.Integer)
    Bridge = db.Column(db.Integer)
    Building = db.Column(db.Integer)
    Bushes = db.Column(db.Integer)
    Cabin = db.Column(db.Integer)
    Cactus = db.Column(db.Integer)
    Circle_Frame = db.Column('Circle Frame', db.Integer)
    Cirrus = db.Column(db.Integer)
    Cliff = db.Column(db.Integer)
    Clouds = db.Column(db.Integer)
    Conifer = db.Column(db.Integer)
    Cumulus = db.Column(db.Integer)
    Deciduous = db.Column(db.Integer)
    Diane_Andre = db.Column('Diane Andre', db.Integer)
    Dock = db.Column(db.Integer)
    Double_Oval_Frame = db.Column('Double Oval Frame', db.Integer)
    Farm = db.Column(db.Integer)
    Fence = db.Column(db.Integer)
    Fire = db.Column(db.Integer)
    Florida_Frame = db.Column('Florida Frame', db.Integer)
    Flowers = db.Column(db.Integer)
    Fog = db.Column(db.Integer)
    Framed = db.Column(db.Integer)
    Grass = db.Column(db.Integer)
    Guest = db.Column(db.Integer)
    Half_Circle_Frame = db.Column('Half Circle Frame', db.Integer)
    Half_Oval_Frame = db.Column('Half Oval Frame', db.Integer)
    Hills = db.Column(db.Integer)
    Lake = db.Column(db.Integer)
    Lakes = db.Column(db.Integer)
    Lighthouse = db.Column(db.Integer)
    Mill = db.Column(db.Integer)
    Moon = db.Column(db.Integer)
    Mountain = db.Column(db.Integer)
    Mountains = db.Column(db.Integer)
    Night = db.Column(db.Integer)
    Ocean = db.Column(db.Integer)
    Oval_Frame = db.Column('Oval Frame', db.Integer)
    Palm_Trees = db.Column('Palm Trees', db.Integer)
    Path = db.Column(db.Integer)
    Person = db.Column(db.Integer)
    Portrait = db.Column(db.Integer)
    Rectangle_3d_Frame = db.Column('Rectangle 3d Frame', db.Integer)
    Rectangular_Frame = db.Column('Rectangular Frame', db.Integer)
    River = db.Column(db.Integer)
    Rocks = db.Column(db.Integer)
    Seashell_Frame = db.Column('Seashell Frame', db.Integer)
    Snow = db.Column(db.Integer)
    Snowy_Mountain = db.Column('Snowy Mountain', db.Integer)
    Split_Frame = db.Column('Split Frame', db.Integer)
    Steve_Ross = db.Column('Steve Ross', db.Integer)
    Structure = db.Column(db.Integer)
    Sun = db.Column(db.Integer)
    Tomb_Frame = db.Column('Tomb Frame', db.Integer)
    Tree = db.Column(db.Integer)
    Trees = db.Column(db.Integer)
    Triple_Frame = db.Column('Triple Frame', db.Integer)
    Waterfall = db.Column(db.Integer)
    Waves = db.Column(db.Integer)
    Windmill = db.Column(db.Integer)
    Window_Frame = db.Column('Window Frame', db.Integer)
    Winter = db.Column(db.Integer)
    Wood_Framed = db.Column('Wood Framed', db.Integer)
    Month = db.Column(db.Text)
    Day = db.Column(db.Text)
    Year = db.Column(db.Text)

class EpisodesSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Episodes
        ordered = True

@app.route("/")
def search():
    parameterDict = {}
    if len(request.args) < 1:
        randIndex = random.randint(0,403)
        episode = Episodes.query.filter_by(index=randIndex).first()
        allEps = Episodes.query.all()
        return render_template("home.html", episode=episode, allEps=allEps)
    requestList = []
    for param in request.args:
        if request.args.get(param) == '0' or request.args.get(param) == '1':
            requestList.append(param)
        else:
            requestList.append(request.args.get(param))
        if param == "Color":
            parameterDict[request.args.get(param)] = 1
        else:
            parameterDict[param] = request.args.get(param)
    results = Episodes.query.filter_by(**parameterDict).all()
    episodeSchema = EpisodesSchema(many=True)
    serializedResults = episodeSchema.dump(results)
    resultDict = {}
    x = 0
    for result in serializedResults:
        resultDict[x] = result
        x = x + 1
    # jsonResults = json.dumps(resultDict, indent=1)
    return render_template("search.html", results=results, requestList=requestList)
    # return make_response(jsonResults)

if __name__ == "__main__":
    app.run(debug=True)