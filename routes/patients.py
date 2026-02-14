from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.postgres import get_db
from schemas.schemas import PatientCreate, PatientResponse
from crud import crud

router = APIRouter(prefix="/patients", tags=["Patients"])


# CREATE PATIENT
@router.post("/", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db, patient)


# GET ALL PATIENTS
@router.get("/", response_model=list[PatientResponse])
def get_all_patients(db: Session = Depends(get_db)):
    return crud.get_patients(db)


#  GET SINGLE PATIENT
@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id)
    
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient


#  UPDATE PATIENT
@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: int, patient: PatientCreate, db: Session = Depends(get_db)):
    updated = crud.update_patient(db, patient_id, patient)
    
    if not updated:
        raise HTTPException(status_code=404, detail="Patient not found")

    return updated


#  DELETE PATIENT
@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_patient(db, patient_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Patient not found")

    return {"message": "Patient deleted successfully"}
