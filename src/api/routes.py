"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""


from sqlalchemy.exc import SQLAlchemyError
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db 
from api.utils import generate_sitemap, APIException
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from datetime import datetime, timezone
# from cryptography.fernet import Fernet  

from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError
import traceback
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)

import smtplib
import ssl
import os
import random, string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import logging


smtp_address = os.getenv("SMTP_ADDRESS")
smtp_port = os.getenv("EMAIL_PORT")
email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")

# cryptography.fernet for the token
# Obtener la clave de encriptación desde el entorno
# encryption_key = os.getenv('ENCRYPTION_KEY')
# cipher = Fernet(encryption_key)


#middleware
api = Blueprint('api', __name__)
app = Flask(__name__)
bcrypt = Bcrypt(app)
logger = logging.getLogger(__name__)

#Funciones Utilitarias

def send_email(asunto, destinatario, body):
    message = MIMEMultipart("alternative")
    message["Subject"] = asunto
    message["From"] = email_address
    message["To"] = destinatario

    # Version HTML del body
    html = '''  
    <html>
    <body>
    <div>
    <h1></h1>
    ''' + body + '''
    </div>
    </body>
    </html> 
    '''

    # Crear elemento MIME
    html_mime = MIMEText(html, 'html')
    # adjuntamos el codigo del mensaje
    message.attach(html_mime)

    # Enviar el correo
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
            server.login(email_address, email_password)
            server.sendmail(email_address, destinatario, message.as_string())
        return True
    except Exception as error:
        print(str(error))
        return False

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

# classlevel Routes 

# Create classlevel
# @api.route('/classlevel', methods=['POST'])
# @jwt_required()
# def create_classlevel():
#     try:
#         # Obtener el usuario autenticado
#         current_user_id = get_jwt_identity()
#         current_user = User.query.get(current_user_id)

#         # Verificar que el usuario tenga permisos para crear un nivel de clase
#         if current_user.role not in {UserRoleEnum.DEV, UserRoleEnum.SERVICE, UserRoleEnum.INSTITUTION, UserRoleEnum.EDUADMIN}:
#             return jsonify({"error": "No tienes permiso para crear niveles de clase"}), 403

#         # Obtener los datos del cuerpo de la solicitud
#         level = request.json.get("level")
#         section = request.json.get("section")

#         # Asegúrate de que todos los campos obligatorios estén presentes
#         if not all([level]):
#             return jsonify({"error": "Faltan campos obligatorios"}), 400

#         # Obtener el institutionId del usuario autenticado
#         if current_user.role == UserRoleEnum.INSTITUTION or current_user.role == UserRoleEnum.EDUADMIN:
#             institutionId = current_user.institutionId
#         elif current_user.role == UserRoleEnum.DEV or current_user.role == UserRoleEnum.SERVICE:
#             institutionId = request.json.get("institutionId")
#             if not institutionId:
#                 return jsonify({"error": "Institution ID es requerido para el rol DEV o SERVICE"}), 400

#             # Validar que el institutionId exista en la base de datos
#             institution = EducationalInstitution.query.get(institutionId)
#             if not institution:
#                 return jsonify({"error": "Institution ID no válido"}), 404
#         else:
#             return jsonify({"error": "Rol no permitido"}), 403

#         # Verificar si ya existe un ClassLevel con el mismo nivel y sección en la misma institución
#         existing_classlevel = ClassLevel.query.filter_by(
#             institutionId=institutionId,
#             level=level,
#             section=section
#         ).first()

#         if existing_classlevel:
#             return jsonify({"error": "Ya existe una clase con este nivel y sección en la institución"}), 400

#         # Generar el código de nivel de clase
#         code = generate_class_level_code(institutionId, level, section)

#         # Crear una nueva instancia de ClassLevel
#         new_classlevel = ClassLevel(
#             level=level,
#             section=section,
#             institutionId=institutionId,
#             code=code
#         )

#         # Agregar el nuevo ClassLevel a la base de datos
#         db.session.add(new_classlevel)
#         db.session.commit()

#         return jsonify(new_classlevel.serialize()), 201

#     except SQLAlchemyError as e:
#         db.session.rollback()
#         return jsonify({"error": f"Error en la base de datos: {str(e)}"}), 500
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
# # Get all classlevel
# @api.route('/classlevel', methods=['GET'])
# def get_classlevels():
#     try:
#         # Obtener parámetros de consulta
#         level = request.args.get('level')
#         institution_id = request.args.get('institutionId')
#         id = request.args.get('id')  # Añadido para el filtro por ID

#         # Construir la consulta base
#         query = ClassLevel.query

#         # Aplicar filtros condicionalmente
#         if level:
#             try:
#                 level = int(level)  # Convertir a entero para comparar con el campo de tipo integer
#                 query = query.filter_by(level=level)
#             except ValueError:
#                 return jsonify({"error": "Nivel inválido"}), 400

#         if institution_id:
#             try:
#                 institution_id = int(institution_id)  # Asegurarse de que el ID sea un entero
#                 query = query.filter_by(institutionId=institution_id)
#             except ValueError:
#                 return jsonify({"error": "ID de institución inválido"}), 400

#         if id:
#             try:
#                 id = int(id)  # Asegurarse de que el ID sea un entero
#                 query = query.filter_by(id=id)
#             except ValueError:
#                 return jsonify({"error": "ID inválido"}), 400

#         # Ejecutar la consulta
#         classlevels = query.all()

#         # Serializar la lista de niveles de clase
#         classlevels_list = [classlevel.serialize() for classlevel in classlevels]

#         return jsonify(classlevels_list), 200

#     except SQLAlchemyError as e:
#         return jsonify({"error": f"Error en la base de datos: {str(e)}"}), 500
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    


# # Get classlevel by rol
# @api.route('/classlevel/user', methods=['GET'])
# @jwt_required()
# def get_classlevelsbyuser():
#     try:
#         # Obtener el usuario autenticado
#         current_user_id = get_jwt_identity()
#         current_user = User.query.get(current_user_id)

#         if not current_user:
#             return jsonify({"error": "Usuario no encontrado"}), 404

#         # Obtener parámetros de consulta
#         level = request.args.get('level')
#         institution_id = request.args.get('institutionId')
#         id = request.args.get('id')  # Añadido para el filtro por ID

#         # Construir la consulta base
#         query = ClassLevel.query

#         # Aplicar filtros según el rol del usuario
#         if current_user.role == UserRoleEnum.INSTITUTION or current_user.role == UserRoleEnum.EDUADMIN or current_user.role == UserRoleEnum.TEACHER:
#             # Filtrar por institutionId del usuario
#             query = query.filter_by(institutionId=current_user.institutionId)

#         elif current_user.role == UserRoleEnum.DEV or current_user.role == UserRoleEnum.SERVICE:
#             # Los usuarios con rol DEV pueden ver todos los niveles de clase
#             if institution_id:
#                 try:
#                     institution_id = int(institution_id)  # Asegurarse de que el ID sea un entero
#                     query = query.filter_by(institutionId=institution_id)
#                 except ValueError:
#                     return jsonify({"error": "ID de institución inválido"}), 400

#         else:
#             return jsonify({"error": "Rol de usuario no permitido"}), 403

#         # Aplicar otros filtros condicionalmente
#         if level:
#             try:
#                 level = int(level)  # Convertir a entero para comparar con el campo de tipo integer
#                 query = query.filter_by(level=level)
#             except ValueError:
#                 return jsonify({"error": "Nivel inválido"}), 400

#         if id:
#             try:
#                 id = int(id)  # Asegurarse de que el ID sea un entero
#                 query = query.filter_by(id=id)
#             except ValueError:
#                 return jsonify({"error": "ID inválido"}), 400

#         # Ejecutar la consulta
#         classlevels = query.all()

#         # Serializar la lista de niveles de clase
#         classlevels_list = [classlevel.serialize() for classlevel in classlevels]

#         return jsonify(classlevels_list), 200

#     except SQLAlchemyError as e:
#         logging.error(f"Error en la base de datos: {str(e)}")
#         return jsonify({"error": f"Error en la base de datos: {str(e)}"}), 500
#     except Exception as e:
#         logging.error(f"Error inesperado: {str(e)}")
#         return jsonify({"error": "Error inesperado", "traceback": str(e)}), 500

