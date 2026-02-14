from sqlalchemy.orm import Session
from models import sql_models
from schemas.schemas import *

from database.mongodb import medical_records_collection


def create_patient(db: Session, patient: PatientCreate):
    db_patient = sql_models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patients(db: Session):
    return db.query(sql_models.Patient).all()


def create_doctor(db: Session, doctor: DoctorCreate):
    db_doctor = sql_models.Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


def get_doctors(db: Session):
    return db.query(sql_models.Doctor).all()


def create_appointment(db: Session, appointment: AppointmentCreate):
    db_appointment = sql_models.Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


def get_appointments(db: Session):
    return db.query(sql_models.Appointment).all()


async def create_medical_record(record: MedicalRecordCreate):
    result = await medical_records_collection.insert_one(record.dict())
    return str(result.inserted_id)


async def get_medical_records(patient_id: int):
    records = []
    cursor = medical_records_collection.find({"patient_id": patient_id})

    async for record in cursor:
        record["_id"] = str(record["_id"])
        records.append(record)

    return records
