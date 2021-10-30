from database.db import get_db

#-----------------------------consulta email, nombre y contraseña----------------------------------
def consult_email(email):
    db=get_db()
    cursor=db.cursor()
    statement="SELECT  email_usua FROM usuario WHERE email_usua=?"
    cursor.execute(statement,[email])
    return cursor.fetchone()

def consult_name(name):
    db=get_db()
    cursor=db.cursor()
    statement="SELECT usuari_usua FROM usuario WHERE usuari_usua=?"
    cursor.execute(statement,[name])
    return cursor.fetchone()

def consult_password(usuario):
    db=get_db()
    cursor=db.cursor()
    statement="SELECT passw_usua FROM usuario WHERE usuari_usua=?"
    cursor.execute(statement,[usuario])
    return cursor.fetchone()


def consult_password_email(email):
    db=get_db()
    cursor=db.cursor()
    statement="SELECT passw_usua FROM usuario WHERE email_usua=?"
    cursor.execute(statement,[email])
    return cursor.fetchone()

def consult_nombre_email(name):
    db=get_db()
    cursor=db.cursor()
    statement="SELECT nom_usua FROM usuario WHERE email_usua=?"
    cursor.execute(statement,[name])
    return cursor.fetchone()

def consult_nombre_usua(name):
    db=get_db()
    cursor=db.cursor()
    statement="SELECT nom_usua FROM usuario WHERE usuari_usua=?"
    cursor.execute(statement,[name])
    return cursor.fetchone()
    
#---------------------------------------------------------------------CRUD USUARIO---------------------------------------------
def insert_usuario(id,nombre,usuario,contraseña,email,imagen,fingreso,rol,telefono):
    db = get_db()
    cursor = db.cursor()
    statement= "INSERT INTO usuario(identif_usua,nom_usua, usuari_usua, passw_usua, email_usua, img_usua, fecha_ingreso_usua, rol_usua, tel_usua) VALUES(?,?,?,?,?,?,?,?,?)"
    cursor.execute(statement,[id,nombre,usuario,contraseña,email,imagen,fingreso,rol,telefono])
    db.commit()
    db.close()
    return True

def edit_usuario(id,nombre,usuario,contraseña,email,imagen,fingreso,rol,telefono):
    db = get_db()
    cursor = db.cursor()
    statement= "UPDATE usuario SET nom_usua = ?, usuari_usua = ?, passw_usua = ?, email_usua = ?, img_usua = ?, fecha_ingreso_usua = ?, rol_usua = ?, tel_usua = ? WHERE identif_usua = ?;"
    cursor.execute(statement,[nombre,usuario,contraseña,email,imagen,fingreso,rol,telefono,id])
    db.commit()
    return True

def dell_usuario(id):
    db = get_db()
    cursor = db.cursor()
    statement= "DELETE FROM usuario WHERE identif_usua=?;"
    cursor.execute(statement,[id])
    db.commit()
    db.close()
    return True

def get_one_usuario(id):
    db = get_db()
    cursor = db.cursor()
    statement= "SELECT identif_usua,nom_usua, usuari_usua, passw_usua, email_usua, img_usua, fecha_ingreso_usua, rol_usua, tel_usua FROM usuario WHERE identif_usua=?;"
    cursor.execute(statement,[id])
    return cursor.fetchone()

def get_all_usuario():
    db = get_db()
    cursor = db.cursor()
    query= "SELECT identif_usua,nom_usua, usuari_usua, passw_usua, email_usua, img_usua, fecha_ingreso_usua, rol_usua, tel_usua FROM usuario;"
    cursor.execute(query)
    return cursor.fetchall()

#---------------------------------------------------------------------CRUD PROVEEDOR---------------------------------------------

def insert_proveedor(id,nombre,direccion,email,fregistro,imagen,ciudad,telefono,descripcion):
    db = get_db()
    cursor = db.cursor()
    statement= "INSERT INTO proveedor(id_prov,nom_prov,dirección_prov,email_prov,fecha_ingreso_prov,img_prov,ciudad_prov,tel_prov,desc_prov) VALUES(?,?,?,?,?,?,?,?,?)"
    cursor.execute(statement,[id,nombre,direccion,email,fregistro,imagen,ciudad,telefono,descripcion])
    db.commit()
    db.close()
    return True

def edit_proveedor(id,nombre,direccion,email,fregistro,imagen,ciudad,telefono,descripcion):
    db = get_db()
    cursor = db.cursor()
    statement= "UPDATE proveedor SET nom_prov = ?, dirección_prov = ?, email_prov = ?, fecha_ingreso_prov = ?, img_prov = ?, ciudad_prov = ?, tel_prov = ?, desc_prov = ? WHERE id_prov = ?;"
    cursor.execute(statement,[nombre,direccion,email,fregistro,imagen,ciudad,telefono,descripcion,id])
    db.commit()
    return True

def dell_proveedor(id):
    db = get_db()
    cursor = db.cursor()
    statement= "DELETE FROM proveedor WHERE id_prov=?;"
    cursor.execute(statement,[id])
    db.commit()
    db.close()
    return True

def get_one_proveedor(id):
    db = get_db()
    cursor = db.cursor()
    statement= "SELECT id_prov,nom_prov,dirección_prov,email_prov,ciudad_prov,img_prov,fecha_ingreso_prov,desc_prov,tel_prov FROM proveedor WHERE id_prov=?;"
    cursor.execute(statement,[id])
    return cursor.fetchone()

def get_all_proveedor():
    db = get_db()
    cursor = db.cursor()
    query= "SELECT id_prov,nom_prov,dirección_prov,email_prov,fecha_ingreso_prov,img_prov,ciudad_prov,desc_prov,tel_prov FROM proveedor;"
    cursor.execute(query)
    return cursor.fetchall()

#---------------------------------------------------------------------CRUD PRODUCTO---------------------------------------------

def insert_producto(id,nombre,direccion,email,imagen,fregistro,ciudad,telefono,descripcion):
    db = get_db()
    cursor = db.cursor()
    statement= "INSERT INTO producto(id_prod,nom_prod,cant_min_prod,cant_max_prod, desc_prod,img_prod,fecha_ing_prod,cant_prod) VALUES(?,?,?,?,?,?,?,?,?)"
    cursor.execute(statement,[id,nombre,direccion,email,fregistro,imagen,ciudad,telefono,descripcion])
    db.commit()
    db.close()
    return True

def edit_producto(id,nombre,usuario,contraseña,email,imagen,fingreso,rol,telefono):
    db = get_db()
    cursor = db.cursor()
    statement= "UPDATE usuario SET nom_usua = ?, usuari_usua = ?, passw_usua = ?, email_usua = ?, img_usua = ?, fecha_ingreso_usua = ?, rol_usua = ?, tel_usua = ? WHERE identif_usua = ?;"
    cursor.execute(statement,[nombre,usuario,contraseña,email,imagen,fingreso,rol,telefono,id])
    db.commit()
    return True

def dell_producto(id):
    db = get_db()
    cursor = db.cursor()
    statement= "DELETE FROM proveedor WHERE id_prov=?;"
    cursor.execute(statement,[id])
    db.commit()
    db.close()
    return True

def get_one_producto(id):
    db = get_db()
    cursor = db.cursor()
    statement= "SELECT id_prov,nom_prov,dirección_prov,email_prov,fecha_ingreso_prov,img_prov,ciudad_prov,desc_prov,tel_prov FROM proveedor WHERE id_prov=?;"
    cursor.execute(statement,[id])
    return cursor.fetchone()

def get_all_producto():
    db = get_db()
    cursor = db.cursor()
    query= "SELECT id_prov,nom_prov,dirección_prov,email_prov,fecha_ingreso_prov,img_prov,ciudad_prov,desc_prov,tel_prov FROM proveedor;"
    cursor.execute(query)
    return cursor.fetchall()

