"""
crud.py - CRUD operations for Patient with exception handling.
"""

from sqlalchemy.exc import SQLAlchemyError, IntegrityError  # third-party first

from app.models import db, Patient  # first-party imports after third-party
from app.logger import logger


def create_patient(patient):
    """
    Create a new patient record.

    :param patient: dict with keys id, name, age, disease
    :return: dict representation of the created patient or an error dict
    """
    try:
        patient_model = Patient(
            id=patient["id"],
            name=patient["name"],
            age=patient["age"],
            disease=patient["disease"],
        )
        db.session.add(patient_model)
        db.session.commit()
        return patient_model.to_dict()
    except IntegrityError as ie:
        db.session.rollback()
        logger.warning(f"Duplicate patient ID {patient['id']}: {ie}")
        return {"error": f"Patient with ID {patient['id']} already exists."}
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.exception(f"Database error while creating patient: {e}")
        return {"error": "Failed to create patient due to database error."}


def read_all_patients():
    """
    Read and return all patients.

    :return: list of patient dicts
    """
    try:
        patients = db.session.query(Patient).all()
        return [patient.to_dict() for patient in patients]
    except SQLAlchemyError as e:
        logger.exception(f"Database error while reading all patients: {e}")
        return []


def read_model_by_id(patient_id):
    """
    Retrieve a Patient model instance by ID.

    :param patient_id: patient identifier
    :return: Patient model instance or None
    """
    try:
        return db.session.query(Patient).filter_by(id=patient_id).first()
    except SQLAlchemyError as e:
        logger.exception(f"Database error while reading patient {patient_id}: {e}")
        return None


def read_by_id(patient_id):
    """
    Retrieve a patient as a dict by ID.

    :param patient_id: patient identifier
    :return: dict of patient data or None
    """
    patient = read_model_by_id(patient_id)
    return None if not patient else patient.to_dict()


def update(patient_id, new_patient):
    """
    Update an existing patient record.

    :param patient_id: patient identifier
    :param new_patient: dict of fields to update
    :return: updated patient dict or error dict
    """
    try:
        patient = read_model_by_id(patient_id)
        if not patient:
            return None
        patient.name = new_patient.get("name", patient.name)
        patient.age = new_patient.get("age", patient.age)
        patient.disease = new_patient.get("disease", patient.disease)
        db.session.commit()
        return patient.to_dict()
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.exception(f"Database error while updating patient {patient_id}: {e}")
        return {"error": "Failed to update patient due to database error."}


def delete_patient(patient_id):
    """
    Delete a patient record.

    :param patient_id: patient identifier
    :return: True if deleted, None if not found, or error dict
    """
    try:
        patient = read_model_by_id(patient_id)
        if not patient:
            return None
        db.session.delete(patient)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.exception(f"Database error while deleting patient {patient_id}: {e}")
        return {"error": "Failed to delete patient due to database error."}
