import graphene
from rooms import schema as rooms_schema
from users import schema as users_schema
# from graphene_django import DjangoObjectType
# from rooms.models import Room


# class RoomType(graphene.ObjectType):
#     name = graphene.String()
#     address = graphene.String()
#     price = graphene.Int()
#     beds = graphene.Int()
#     lat = graphene.Decimal()
#     lng = graphene.Decimal()
#     bedrooms = graphene.Int()
#     bathrooms = graphene.Int()
#     check_in = graphene.Time()
#     check_out = graphene.Time()
#     instant_book = graphene.Boolean()

# class RoomType(DjangoObjectType):
#     class Meta:
#         model = Room

# class Query(graphene.ObjectType):
#     rooms = graphene.List(RoomType)

#     def resolve_rooms(self, info):
#         return Room.objects.all()


class Query(rooms_schema.Query, users_schema.Query, graphene.ObjectType):
    pass

class Mutation:
    pass


schema = graphene.Schema(query=Query)