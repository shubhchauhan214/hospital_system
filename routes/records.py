from fastapi import APIRouter, HTTPException
from bson import ObjectId

from database.mongodb import medical_records_collection
from schemas.schemas import MedicalRecordCreate, MedicalRecordResponse

router = APIRouter(prefix="/records", tags=["Medical Records"])


# Helper function (Mongo → JSON convert)
def record_helper(record) -> dict:
    return {
        "id": str(record["_id"]),
        "patient_id": record["patient_id"],
        "diagnosis": record["diagnosis"],
        "treatment": record["treatment"],
        "doctor_notes": record["doctor_notes"],
    }


# CREATE RECORD
@router.post("/", response_model=MedicalRecordResponse)
async def create_record(record: MedicalRecordCreate):
    new_record = await medical_records_collection.insert_one(record.dict())
    created_record = await medical_records_collection.find_one({"_id": new_record.inserted_id})
    return record_helper(created_record)


# GET ALL RECORDS
@router.get("/", response_model=list[MedicalRecordResponse])
async def get_all_records():
    records = []
    async for record in medical_records_collection.find():
        records.append(record_helper(record))
    return records


# GET SINGLE RECORD
@router.get("/{record_id}", response_model=MedicalRecordResponse)
async def get_record(record_id: str):
    record = await medical_records_collection.find_one({"_id": ObjectId(record_id)})
    
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    return record_helper(record)


#  DELETE RECORD
@router.delete("/{record_id}")
async def delete_record(record_id: str):
    result = await medical_records_collection.delete_one({"_id": ObjectId(record_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Record not found")

    return {"message": "Record deleted successfully"}
