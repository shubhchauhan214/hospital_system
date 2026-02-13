from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Prescription(BaseModel):
    medicine: str
    dosage: str
    duration: str

class MedicalRecord(BaseModel):
    patient_id: int
    diagnosis: str
    visit_date: date
    prescriptions: List[Prescription]
    notes: Optional[str] = None
