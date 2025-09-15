"""
SQLAlchemy ORM model definition for Employee.

This module defines the Employee model representing employee records
in the 'employees' database table.
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float, Boolean

Base = declarative_base()  # Base class for ORM models


class Employee(Base):  # pylint: disable=too-few-public-methods
    """
    Employee model mapped to the 'employees' table.

    Attributes:
        id (int): Primary key identifier for the employee.
        name (str): Name of the employee.
        age (int): Age of the employee.
        salary (float): Salary of the employee.
        is_active (bool): Employee active status.
    """

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    salary = Column(Float, nullable=False)
    is_active = Column(Boolean, nullable=False)

    def __repr__(self):
        """
        Provide a readable string representation of the Employee instance.

        Returns:
            str: String representation of the employee.
        """
        return (
            f"[id={self.id}, name={self.name}, age={self.age}, "
            f"salary={self.salary}, is_active={self.is_active}]"
        )

    def to_dict(self):
        """
        Convert the Employee instance to a dictionary.

        Returns:
            dict: Dictionary representation of the employee.
        """
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'salary': self.salary,
            'is_active': self.is_active,
        }
