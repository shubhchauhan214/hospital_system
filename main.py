from fastapi import FastAPI

# Routers
from routes import patients, doctors, records

# DB connection check functions
from database.postgres import check_postgres_connection
from database.mongodb import check_mongo_connection


app = FastAPI(title="Hospital Management System")


#  Include Routers
app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(records.router)


# ✅ Home Route
@app.get("/")
def home():
    return {"message": "Hospital Management System Running"}


#  Startup Event — DB Connection Verification
@app.on_event("startup")
async def startup_db_check():
    print("🔹 Checking Database Connections...")

    # PostgreSQL check
    pg_status = check_postgres_connection()
    print("Postgres:", pg_status)

    # MongoDB check
    mongo_status = await check_mongo_connection()
    print("MongoDB:", mongo_status)

    print(" System Ready!")
