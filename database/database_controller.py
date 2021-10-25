from database.db import get_db

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

def insert_proveedor(id,nombre,direccion,email,imagen,fregistro,ciudad,telefono,descripcion):
    db = get_db()
    cursor = db.cursor()
    statement= "INSERT INTO usuario(id_prov,nom_prov,dirección_prov,email_prov,img_prov,fecha_ingreso_prov,ciudad_prov,tel_prov,desc_prov) VALUES(?,?,?,?,?,?,?,?,?)"
    cursor.execute(statement,[id,nombre,direccion,email,imagen,fregistro,ciudad,telefono,descripcion])
    db.commit()
    db.close()
    return True

def edit_proveedor(id,nombre,usuario,contraseña,email,imagen,fingreso,rol,telefono):
    db = get_db()
    cursor = db.cursor()
    statement= "UPDATE usuario SET nom_usua = ?, usuari_usua = ?, passw_usua = ?, email_usua = ?, img_usua = ?, fecha_ingreso_usua = ?, rol_usua = ?, tel_usua = ? WHERE identif_usua = ?;"
    cursor.execute(statement,[nombre,usuario,contraseña,email,imagen,fingreso,rol,telefono,id])
    db.commit()
    return True

def dell_proveedor(id):
    db = get_db()
    cursor = db.cursor()
    statement= "DELETE FROM usuario WHERE identif_usua=?;"
    cursor.execute(statement,[id])
    db.commit()
    db.close()
    return True

def get_one_proveedor(id):
    db = get_db()
    cursor = db.cursor()
    statement= "SELECT identif_usua,nom_usua, usuari_usua, passw_usua, email_usua, img_usua, fecha_ingreso_usua, rol_usua, tel_usua FROM usuario WHERE identif_usua=?;"
    cursor.execute(statement,[id])
    return cursor.fetchone()

def get_all_proveedor():
    db = get_db()
    cursor = db.cursor()
    query= "SELECT identif_usua,nom_usua, usuari_usua, passw_usua, email_usua, img_usua, fecha_ingreso_usua, rol_usua, tel_usua FROM usuario;"
    cursor.execute(query)
    return cursor.fetchall()
