from sqlalchemy import Column, Integer, String, Date , ForeignKey
from sqlalchemy.orm import relationship
from database.postgres import Base

# Patient Table

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name= Column(String, nullable=False)
    age = Column(Integer)
    gender=Column(String)
    phone=Column(String)

    appointments = relationship("Appointment", back_populates="patient")

# Doctor Table

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name= Column(String, nullable=False)
    specialization = Column(String)
    phone = Column(String)

    appointments = relationship("Appointment", back_populates="doctor")


# Appointment Table

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)

    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
    