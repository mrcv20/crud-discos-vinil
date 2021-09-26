from app import ma
from ..models import *


class DiscoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VinylDisc
        load_instance = True
        include_fk = True
        #Fields to skip during serialization
        load_only = ("artista")

disco_schema = DiscoSchema()
discos_schema = DiscoSchema(many=True)


class ArtistSchema(ma.SQLAlchemyAutoSchema):
    discos = ma.Nested(DiscoSchema, many=True)
    class Meta:
        model = Artist
        load_instance = True
        include_fk = True

artista_schema = ArtistSchema()
artistas_schema = ArtistSchema(many=True)


