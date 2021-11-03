# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articulos(models.Model):
    idarticulos = models.IntegerField(db_column='idArticulos', primary_key=True)  # Field name made lowercase.
    donativos_iddonativos = models.IntegerField()
    articulos_categoria_idarticulos_categoria = models.IntegerField(db_column='Articulos_categoria_idArticulos_categoria')  # Field name made lowercase.
    inventario_idinventario = models.IntegerField()
    articulos_nombre = models.CharField(db_column='Articulos_nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    articulos_stockminimo = models.CharField(db_column='Articulos_stockminimo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    articulos_stockmaximo = models.CharField(db_column='Articulos_stockmaximo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    articulos_estado = models.CharField(db_column='Articulos_estado', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'articulos'


class ArticulosCategoria(models.Model):
    idarticulos_categoria = models.IntegerField(db_column='idArticulos_categoria', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion_field = models.CharField(db_column='descripcion_', max_length=45, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'articulos_categoria'


class Bodega(models.Model):
    idbodega = models.IntegerField(primary_key=True)
    ciudad_bodega = models.CharField(max_length=45, blank=True, null=True)
    direccion_bodega = models.CharField(max_length=45, blank=True, null=True)
    nombre_bodega = models.CharField(max_length=45, blank=True, null=True)
    capacidad_bodega = models.IntegerField(blank=True, null=True)
    telefono_bodega = models.CharField(max_length=40, blank=True, null=True)
    correo_bodega = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bodega'


class Bodeguero(models.Model):
    idbodeguero = models.IntegerField(db_column='idBodeguero', primary_key=True)  # Field name made lowercase.
    turno_bodeguero = models.CharField(max_length=45, blank=True, null=True)
    roles_idroles = models.IntegerField()
    bodega_idbodega = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bodeguero'


class CabezaMovimiento(models.Model):
    idcabeza_movimiento = models.IntegerField(db_column='idCabeza_movimiento', primary_key=True)  # Field name made lowercase.
    numero_movimiento = models.CharField(max_length=45, blank=True, null=True)
    totaldocumento = models.CharField(max_length=45, blank=True, null=True)
    tipo_de_documento_idtipo_de_documento = models.IntegerField(db_column='Tipo_de_documento_idTipo_de_documento')  # Field name made lowercase.
    usuarios_idusuarios = models.IntegerField()
    fecha_field = models.CharField(db_column='fecha_', max_length=45, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'cabeza_movimiento'


class CategoriaBienes(models.Model):
    idcategoria_servicios = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion_field = models.CharField(db_column='descripcion_', max_length=45, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'categoria_bienes'


class CategoriaProductos(models.Model):
    idcategoria_servicios = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion_field = models.CharField(db_column='descripcion_', max_length=45, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'categoria_productos'


class CategoriaServicios(models.Model):
    idcategoria_servicios = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion_field = models.CharField(db_column='descripcion_', max_length=45, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'categoria_servicios'


class CuerpoMovimiento(models.Model):
    idcuerpo_movimiento = models.IntegerField(db_column='idCuerpo_movimiento', primary_key=True)  # Field name made lowercase.
    cantidad = models.CharField(max_length=45, blank=True, null=True)
    valor_unitario = models.CharField(max_length=45, blank=True, null=True)
    cabeza_movimiento_idcabeza_movimiento = models.IntegerField(db_column='Cabeza_movimiento_idCabeza_movimiento')  # Field name made lowercase.
    articulos_idarticulos = models.IntegerField(db_column='Articulos_idArticulos')  # Field name made lowercase.
    paquetes_idpaquetes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cuerpo_movimiento'


class DescripcionPublicacion(models.Model):
    iddescripcion_publicacion = models.IntegerField(db_column='idDescripcion_Publicacion', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion_field = models.CharField(db_column='descripcion_', max_length=45, blank=True, null=True)  # Field renamed because it ended with '_'.
    tipob = models.CharField(max_length=45, blank=True, null=True)
    ubicacion = models.CharField(max_length=45, blank=True, null=True)
    antiguedad = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    categoria_servicios_idcategoria_servicios = models.IntegerField(blank=True, null=True)
    categoria_bienes_idcategoria_servicios = models.IntegerField(blank=True, null=True)
    categoria_productos_idcategoria_servicios = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'descripcion_publicacion'


class Donativos(models.Model):
    iddonativos = models.IntegerField(primary_key=True)
    nombre_donativos = models.CharField(max_length=45, blank=True, null=True)
    descripcion_donativos = models.CharField(max_length=45, blank=True, null=True)
    usuarios_idusuarios = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'donativos'


class Kardex(models.Model):
    idinventario = models.IntegerField(primary_key=True)
    disponibilidad_inventario = models.CharField(max_length=40, blank=True, null=True)
    fecha_ingreso_inventario = models.DateField(blank=True, null=True)
    origen_inventario = models.CharField(max_length=45, blank=True, null=True)
    bodega_idbodega = models.IntegerField()
    inventario_stock = models.CharField(max_length=45, blank=True, null=True)
    inventario_preciocompra = models.CharField(max_length=45, blank=True, null=True)
    inventario_precioventa = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kardex'


class Login(models.Model):
    idlogin = models.IntegerField(primary_key=True)
    nombre_login = models.CharField(max_length=45)
    contraseña_login = models.CharField(max_length=45)
    registro_idregistro = models.IntegerField()
    roles_idroles = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'


class MetodoDePago(models.Model):
    efectivometododepago = models.CharField(max_length=40, blank=True, null=True)
    idmetododepago = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'metodo_de_pago'


class Paquetes(models.Model):
    idpaquetes = models.IntegerField(primary_key=True)
    nombre_paquete = models.CharField(max_length=45, blank=True, null=True)
    valor_paquete = models.IntegerField(blank=True, null=True)
    usuarios_idusuarios = models.IntegerField()
    metodo_pago = models.ForeignKey(MetodoDePago, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'paquetes'


class Personas(models.Model):
    idpersonas = models.IntegerField(primary_key=True)
    nombrepersona = models.CharField(max_length=45)
    apellidopersona = models.CharField(max_length=45, blank=True, null=True)
    fecha_n_persona = models.DateField(blank=True, null=True)
    genero_persona = models.CharField(max_length=45, blank=True, null=True)
    estado_civil_persona = models.CharField(max_length=45, blank=True, null=True)
    ciudad_origen_persona = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personas'


class Publicaciones(models.Model):
    idpublicaciones = models.IntegerField(primary_key=True)
    tipo_publicacion_idtipo_publicacion = models.IntegerField(db_column='Tipo_publicacion_idTipo_publicacion')  # Field name made lowercase.
    descripcion_publicacion_iddescripcion_publicacion = models.IntegerField(db_column='Descripcion_Publicacion_idDescripcion_Publicacion')  # Field name made lowercase.
    usuarios_idusuarios = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'publicaciones'


class Registro(models.Model):
    idregistro = models.PositiveIntegerField(primary_key=True)
    nombredeusuario_registro = models.CharField(max_length=45)
    codigodeverificacion_registro = models.IntegerField()
    telefono_registro = models.CharField(max_length=45, blank=True, null=True)
    preguntaseguridad_registro = models.CharField(max_length=45)
    personas_idpersonas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registro'


class Roles(models.Model):
    idroles = models.IntegerField(primary_key=True)
    administrador_roles = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class TipoDeDocumento(models.Model):
    idtipo_de_documento = models.IntegerField(db_column='idTipo_de_documento', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion_field = models.CharField(db_column='descripcion_', max_length=45, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'tipo_de_documento'


class TipoPublicacion(models.Model):
    idtipo_publicacion = models.IntegerField(db_column='idTipo_publicacion', primary_key=True)  # Field name made lowercase.
    tipo_publicacion_nombre = models.CharField(db_column='Tipo_publicacion_nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_publicacion'


class Usuarios(models.Model):
    idusuarios = models.IntegerField(primary_key=True)
    ciudad_actual_usuarios = models.CharField(max_length=45, blank=True, null=True)
    intereses_usuarios = models.CharField(max_length=45, blank=True, null=True)
    correo_usuarios = models.CharField(max_length=45, blank=True, null=True)
    telefono_usuarios = models.CharField(max_length=50, blank=True, null=True)
    direccion_usuarios = models.CharField(max_length=45)
    roles_idroles = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios'
