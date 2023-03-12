#uvicorn main:app --reload


from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Yelp App"}

@app.get("/restaurants/{restaurant}") #name
async def read_restaurant(restaurant: str):
    return {"restaurant": restaurant}
@app.get("/states/{state}") #location
async def read_state(state: str):
    return {"state": state}
@app.get("/stars/{stars}") #rating
async def read_stars(stars: float):
    return{"stars": stars}
@app.get("/sentiment/{sentiment}") #positive sentiment of ratings
async def read_sentiment(sentiment: float):
    return{"sentiment": sentiment}

@app.get("/dishes/{dishes}") #positive sentiment of ratings
async def read_dishes(dishes: str):
    return{"dishes": dishes}