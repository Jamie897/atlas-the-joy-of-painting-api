#!/usr/bin/python3
from sqlalchemy import Column, Integer, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Episode(Base):
    __tablename__ = 'episodes'

    index = Column(Integer, index=True)
    Thumbnail = Column(Text)
    Title = Column(NullType, primary_key=True)
    Season = Column(Integer)
    Episode = Column(Integer)
    Youtube = Column(Text)
    Black_Gesso = Column('Black Gesso', Integer)
    Bright_Red = Column('Bright Red', Integer)
    Burnt_Umber = Column('Burnt Umber', Integer)
    Cadmium_Yellow = Column('Cadmium Yellow', Integer)
    Dark_Sienna = Column('Dark Sienna', Integer)
    Indian_Red = Column('Indian Red', Integer)
    Indian_Yellow = Column('Indian Yellow', Integer)
    Liquid_Black = Column('Liquid Black', Integer)
    Liquid_Clear = Column('Liquid Clear', Integer)
    Midnight_Black = Column('Midnight Black', Integer)
    Phthalo_Blue = Column('Phthalo Blue', Integer)
    Phthalo_Green = Column('Phthalo Green', Integer)
    Prussian_Blue = Column('Prussian Blue', Integer)
    Sap_Green = Column('Sap Green', Integer)
    Titanium_White = Column('Titanium White', Integer)
    Van_Dyke_Brown = Column('Van Dyke Brown', Integer)
    Yellow_Ochre = Column('Yellow Ochre', Integer)
    Alizarin_Crimson = Column('Alizarin Crimson', Integer)
    Apple_Frame = Column('Apple Frame', Integer)
    Aurora_Borealis = Column('Aurora Borealis', Integer)
    Barn = Column(Integer)
    Beach = Column(Integer)
    Boat = Column(Integer)
    Bridge = Column(Integer)
    Building = Column(Integer)
    Bushes = Column(Integer)
    Cabin = Column(Integer)
    Cactus = Column(Integer)
    Circle_Frame = Column('Circle Frame', Integer)
    Cirrus = Column(Integer)
    Cliff = Column(Integer)
    Clouds = Column(Integer)
    Conifer = Column(Integer)
    Cumulus = Column(Integer)
    Deciduous = Column(Integer)
    Diane_Andre = Column('Diane Andre', Integer)
    Dock = Column(Integer)
    Double_Oval_Frame = Column('Double Oval Frame', Integer)
    Farm = Column(Integer)
    Fence = Column(Integer)
    Fire = Column(Integer)
    Florida_Frame = Column('Florida Frame', Integer)
    Flowers = Column(Integer)
    Fog = Column(Integer)
    Framed = Column(Integer)
    Grass = Column(Integer)
    Guest = Column(Integer)
    Half_Circle_Frame = Column('Half Circle Frame', Integer)
    Half_Oval_Frame = Column('Half Oval Frame', Integer)
    Hills = Column(Integer)
    Lake = Column(Integer)
    Lakes = Column(Integer)
    Lighthouse = Column(Integer)
    Mill = Column(Integer)
    Moon = Column(Integer)
    Mountain = Column(Integer)
    Mountains = Column(Integer)
    Night = Column(Integer)
    Ocean = Column(Integer)
    Oval_Frame = Column('Oval Frame', Integer)
    Palm_Trees = Column('Palm Trees', Integer)
    Path = Column(Integer)
    Person = Column(Integer)
    Portrait = Column(Integer)
    Rectangle_3d_Frame = Column('Rectangle 3d Frame', Integer)
    Rectangular_Frame = Column('Rectangular Frame', Integer)
    River = Column(Integer)
    Rocks = Column(Integer)
    Seashell_Frame = Column('Seashell Frame', Integer)
    Snow = Column(Integer)
    Snowy_Mountain = Column('Snowy Mountain', Integer)
    Split_Frame = Column('Split Frame', Integer)
    Steve_Ross = Column('Steve Ross', Integer)
    Structure = Column(Integer)
    Sun = Column(Integer)
    Tomb_Frame = Column('Tomb Frame', Integer)
    Tree = Column(Integer)
    Trees = Column(Integer)
    Triple_Frame = Column('Triple Frame', Integer)
    Waterfall = Column(Integer)
    Waves = Column(Integer)
    Windmill = Column(Integer)
    Window_Frame = Column('Window Frame', Integer)
    Winter = Column(Integer)
    Wood_Framed = Column('Wood Framed', Integer)
    Month = Column(Text)
    Day = Column(Text)
    Year = Column(Text)