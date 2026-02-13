from fastapi import FastAPI
from database.postgres import check_postgres_connection
from database.mongodb import check_mongo_connection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hospital System Running"}

@app.get("/test-db")
async def test_db():
    return {
        "postgres": check_postgres_connection(),
        "mongodb": await check_mongo_connection()
    }
