import graphene


class courses(graphene.ObjectType):
    name=graphene.String()
    level=graphene.String()
    duration_in_years=graphene.Int()