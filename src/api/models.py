from flask_sqlalchemy import SQLAlchemy
from sqlalchemyseeder import ResolvingSeeder
import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from datetime import datetime

db = SQLAlchemy()


# class UserRoleEnum(enum.Enum):
#     STUDENT = "student"
#     TEACHER = "teacher"
#     EDUADMIN = "eduadmin" #Educational Admin from the institution
#     INSTITUTION = "institution"
#     PARENT = "parent"
#     SERVICE = "service" #Customer Service
#     DEV = "dev"

# class User(db.Model):
#     __tablename__ = 'user'
    
#     id = db.Column(db.Integer, primary_key=True)
#     institutionId = db.Column(db.Integer, db.ForeignKey('educationalInstitution.idInstitution'), nullable=True)
#     role = db.Column(db.Enum(UserRoleEnum, name="user_role_enum"), nullable=False)
#     status = db.Column(db.Enum(UserStatusEnum, name="user_status_enum"), nullable=False, default=UserStatusEnum.ACTIVE)

#     firstName = db.Column(db.String(50), nullable=False)
#     firstLastname = db.Column(db.String(50), nullable=False)
#     secondLastname = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     password = db.Column(db.String(400), nullable=False)
#     temporaryPassword = db.Column(db.Boolean, default=True)

#     # Relación con RelatedClassLevel (para profesores y estudiantes)
#     relatedClassLevels = db.relationship('RelatedClassLevel', backref='user', lazy=True)

#     address = db.Column(db.String(200), nullable=True)
#     principalPhone = db.Column(db.String(30), nullable=False)
#     secondPhone = db.Column(db.String(30), nullable=True)
#     profilePicture = db.Column(db.String(1000), nullable=True)
#     userPosition = db.Column(db.String(100), nullable=True)
#     details = db.Column(db.String(250), nullable=True)
    
#     country = db.Column(db.String(70), nullable=False)
#     dni = db.Column(db.String(20), nullable=False)
    
#     createdAt = db.Column(db.DateTime, default=datetime.now, nullable=False)
#     updatedAt = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

#     username = db.Column(db.String(50), nullable=True)


#     def __repr__(self):
#         return f'<User {self.email}>'
    
#     def serialize(self):
#         return {
#             "id": self.id,
#             "institutionId": self.institutionId,
#             "role": self.role.value,  # Enum to string
#             "status": self.status.value,
#             "firstName": self.firstName,
#             "firstLastname": self.firstLastname,
#             "secondLastname": self.secondLastname,
#             "email": self.email,
#             "password":self.password,
#             "address": self.address,
#             "principalPhone": self.principalPhone,
#             "secondPhone": self.secondPhone,
#             "profilePicture": self.profilePicture,
#             "userPosition": self.userPosition,
#             "details": self.details,
#             "country": self.country,
#             "dni": self.dni,
#             "createdAt": self.createdAt,
#             "updatedAt": self.updatedAt,
#             "username": self.username,
#             "temporaryPassword": self.temporaryPassword,
#             "relatedClassLevels": [relatedClassLevel.serialize() for relatedClassLevel in self.relatedClassLevels]  # Serializa la lista de RelatedClassLevels
#         }