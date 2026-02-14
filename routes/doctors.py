from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.postgres import get_db
from schemas.schemas import DoctorCreate, DoctorResponse
from crud import crud

router = APIRouter(prefix="/doctors", tags=["Doctors"])


# CREATE DOCTOR
@router.post("/", response_model=DoctorResponse)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    return crud.create_doctor(db, doctor)


#  GET ALL DOCTORS
@router.get("/", response_model=list[DoctorResponse])
def get_all_doctors(db: Session = Depends(get_db)):
    return crud.get_doctors(db)


#  GET SINGLE DOCTOR
@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = crud.get_doctor(db, doctor_id)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor


#  UPDATE DOCTOR
@router.put("/{doctor_id}", response_model=DoctorResponse)
def update_doctor(doctor_id: int, doctor: DoctorCreate, db: Session = Depends(get_db)):
    updated = crud.update_doctor(db, doctor_id, doctor)

    if not updated:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return updated


#  DELETE DOCTOR
@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_doctor(db, doctor_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return {"message": "Doctor deleted successfully"}
