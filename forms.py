from flask_wtf import FlaskForm
from wtforms import SelectField, BooleanField
from wtforms.validators import DataRequired

class FormCheckProduct(FlaskForm):
    proveedores = BooleanField('Proovedores del producto')
    poca_existencia = BooleanField('Productos con poca existencia')


class FormListUser(FlaskForm):
    rol = SelectField('Rol', choices=[('ufinal', 'Usuario Final'),('admin', 'Administrador'),('super', 'Super Administrador')])