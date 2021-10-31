import graphene
from graphene_django import DjangoObjectType
from users.types import UserType
from users.models import User



class Query():

    user = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_user(self, info, id):
        
        return User.objects.get(id=id)
