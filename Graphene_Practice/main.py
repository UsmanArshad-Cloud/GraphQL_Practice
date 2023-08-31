import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp
data = [
    {
        "name": "Roni",
        "city": "Cologne"
    },
    {
        "name": "Usman",
        "city": "Lahore"
    },
    {
        "name": "Ali",
        "city": "Islamabad"
    }
]
class students(graphene.ObjectType):
    name = graphene.String()
    city = graphene.String()

class Person(graphene.ObjectType):
    student=graphene.List(students)
    def resolve_student(self,info):
        return data

app = FastAPI()
app.add_route("/graphql",GraphQLApp(schema=graphene.Schema(query=Person)))