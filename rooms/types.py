import graphene
from graphene_django import DjangoObjectType
from rooms.models import Room



class RoomType(DjangoObjectType):

    # user = graphene.Field("users.tpyes.UserType")

    class Meta:
        model = Room


class RoomListResponse(graphene.ObjectType):
    
    arr = graphene.List(RoomType)
    total = graphene.Int()