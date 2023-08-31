from fastapi import FastAPI
import graphene
from starlette_graphene3 import GraphQLApp
from mapping import query

app = FastAPI()
app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=query)))
