from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional


# ========================
# Patient Schemas
# ========================
class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    phone: str


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attributes = True


# ========================
# Doctor Schemas
# ========================
class DoctorBase(BaseModel):
    name: str
    specialization: str
    phone: str


class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attributes = True


# ========================
# Appointment Schemas
# ========================
class AppointmentBase(BaseModel):
    date: date
    patient_id: int
    doctor_id: int


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    id: int

    class Config:
        from_attributes = True

# ========================
# Medical Record Schemas
# ========================
class Prescription(BaseModel):
    medicine: str
    dosage: str
    duration: str


class MedicalRecordCreate(BaseModel):
    patient_id: int
    diagnosis: str
    visit_date: date
    prescriptions: List[Prescription]
    notes: Optional[str] = None


class MedicalRecordResponse(BaseModel):
    id: Optional[str] = Field(alias="_id")
    patient_id: int
    diagnosis: str
    visit_date: date
    prescriptions: List[Prescription]
    notes: Optional[str] = None

    class Config:
        populate_by_name = True