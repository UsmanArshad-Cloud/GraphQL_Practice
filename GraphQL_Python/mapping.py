import graphene

from schema import courses
from data import read_data


class Query(graphene.ObjectType):
    courses = graphene.List(courses)

    def resolve_courses(self, info):
        return read_data()
