import graphene
from schema import Weather
from data import read_data


class query(graphene.ObjectType):
    city_temp = graphene.Field(Weather, city=graphene.String())

    def resolve_city_temp(self, info, city):
        data = read_data()
        for row in data:
            if row["city"] == city:
                return {"city": row["city"],
                        "temp": row["temperature"]}
        return {"city": city,
                "temp": "City Not Found in the Sequence"}