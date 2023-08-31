from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL

app = FastAPI()


# Sample data
@strawberry.type
class Post:
    id: strawberry.ID
    title: str
    content: str
    author_id: strawberry.ID


@strawberry.type
class Author:
    id: strawberry.ID
    name: str


# Dummy data
posts = [
    Post(id="1", title="GraphQL Introduction", content="This is an introduction to GraphQL.", author_id="101"),
]

authors = [
    Author(id="101", name="John Doe"),
]


# Define schema and queries
@strawberry.type
class Query:
    @strawberry.field
    def post(self, info, id: strawberry.ID) -> Post:
        return next((post for post in posts if post.id == id), None)


schema = strawberry.Schema(query=Query)


# Start the FastAPI server
@app.post("/")
async def graphql(query: str):
    print(query)
    result = schema.execute_sync(query)
    return result.data


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
