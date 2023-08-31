import graphene


class Weather(graphene.ObjectType):
    city = graphene.String()
    temp = graphene.String()
