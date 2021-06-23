import django.contrib.auth.models
from django.db import models
from django.forms import model_to_dict


# Create your models here.
from primer_proyecto.settings import MEDIA_URL, STATIC_URL


class Departamento(models.Model):
    nombre = models.CharField(max_length=25,verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Depatamento'
        verbose_name_plural = 'Departamentos'
        db_table = 'departamento'
        ordering = ['nombre']

class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, verbose_name='Departamento')
    codigo_postal = models.CharField(primary_key=True,max_length=5,verbose_name='Codigo postal')
    nombre = models.CharField(max_length=50,verbose_name='Nombre')


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        db_table = 'municipios'
        ordering = ['departamento','nombre']

class Usuario(models.Model):
    sexo = (('femenino','Femenino'),
            ('masculino','Masculino'),
            ('otro','Otro')
            )
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, verbose_name='Departamento')
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, verbose_name='Municipio')
    dui = models.CharField(max_length=10,verbose_name='DUI',primary_key=True)
    nombre = models.CharField(max_length=100,verbose_name='Nombres')
    apellido = models.CharField(max_length=100,verbose_name='Apellido')
    sexo = models.CharField(max_length=15,verbose_name='Sexo',choices=sexo)
    correo = models.EmailField(verbose_name='Correo electronico',null=True,blank=True)
    telefono = models.CharField(max_length=9,verbose_name='Telefono',null=True,blank=True)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    direccion = models.CharField(max_length=150,verbose_name='Direccion')

    def __str__(self):
        return self.nombre +" "+ self.apellido

    def toJSON(self):
        item = model_to_dict(self,exclude=['apellido','nombre','sexo','correo','telefono','fecha_nacimiento','departamento','municipio','direccion'])
        return item

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'
        #ordering = ['id']

class Administrador(django.contrib.auth.models.User, models.Model):
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
        db_table = 'administrador'
        ordering = ['id']

class SubsidioTransporte(models.Model):
    frecuenciaUso = (('diaramente', 'Diaramente'),
                    ('semanalmente', 'Semanalmente'),
                    ('mensualmente', 'Mensualmente')
            )
    #atributo
    pertenece = models.OneToOneField(Usuario, on_delete=models.PROTECT,verbose_name='Benefeciario',unique=True)

    cantidad_subsidio = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cantidad Subsidio',null=True,blank=True)
    cantidad_buses = models.IntegerField(verbose_name='Cantidad buses')
    cantidad_microbuses = models.IntegerField(verbose_name='Cantidad microbuses')
    frecuencia_uso = models.CharField(max_length=50,verbose_name='Frecuencia uso',choices=frecuenciaUso)

    def toJSON(self):
        item = model_to_dict(self,exclude=['cantidad_buses','cantidad_microbuses','frecuencia_uso'])
        return item

    def __str__(self):
        return 'Subsidio transporte,' +str(self.pertenece)
    
    class Meta:
        verbose_name = 'Subsidio transporte'
        verbose_name_plural = 'Subsidios transporte'
        db_table = 'subsidio_transporte'
        ordering = ['id']

class SubsidioAgua(models.Model):
    pertenece = models.OneToOneField(Usuario, on_delete=models.PROTECT,verbose_name='Benefeciario',unique=True)
    cantidad_subsidio = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Cantidad subsidiada',null=True,blank=True)
    cantidad_consumo = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Cantidad consumida',help_text='cantidad de consumo en metros cubicos')
    recibo_agua = models.ImageField(upload_to='recibos/recibosAgua',null=True)

    def __str__(self):
        return 'Subsidio agua,' +str(self.pertenece)

    def get_image(self):
        if self.recibo_agua:
            return '{}{}'.format(MEDIA_URL,self.recibo_agua)
        return  '{}{}'.format(STATIC_URL,'img/vacio.png')
    class Meta:
        verbose_name = 'Subsidio agua'
        verbose_name_plural = 'Subsidios agua'
        db_table = 'subsidio_agua'
        ordering = ['id']

class SubsidioLuz(models.Model):
    pertenece = models.OneToOneField(Usuario, on_delete=models.PROTECT,verbose_name='Benefeciario',unique=True)
    cantidad_subsidio = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Cantidad subsidioTransporte',null=True,blank=True)
    cantidad_consumo = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Cantidad consumida',help_text='cantidad de consumo en kilowatts por hora')
    recibo_luz = models.ImageField(upload_to='recibos/recibosLuz',null=True)

    def __str__(self):
        return 'Subsidio luz,' +str(self.pertenece)

    def get_image(self):
        if self.recibo_luz:
            return '{}{}'.format(MEDIA_URL,self.recibo_luz)
        return  '{}{}'.format(STATIC_URL,'img/vacio.png')
    class Meta:
        verbose_name = 'Subsidio luz'
        verbose_name_plural = 'Subsidios luz'
        db_table = 'subsidio_luz'
        ordering = ['id']

class SubsidioGasLicuado(models.Model):

    #Lista para la seleccion del tipo de establecimiento
    tipoEstablecimiento = (
        ('Hogar familiar','Hogar'),
        ('Negocio subsistencia',(
                                ('tortilleria','Tortilleria'),
                                ('pupuseria','Pupuseria'),
                                ('panaderia','Panaderia'))
         )
    )

    pertenece = models.OneToOneField(Usuario, on_delete=models.PROTECT,verbose_name='Benefeciario',unique=True)
    cantidad_subsidio = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Cantidad subsidioTransporte',null=True,blank=True)
    cantidad_consumo = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Cantidad consumida',help_text='cantidad de consumo en kilowatts por hora')
    tipo_establecimiento = models.CharField(max_length=50,verbose_name='Tipo beneficiario',choices=tipoEstablecimiento)
    num_tarjeta = models.CharField(max_length=10,verbose_name='Numero tarjeta',null=True,blank=True,default='-')
    recibo_luz = models.ImageField(upload_to='recibos/recibosGas',null=True)

    def __str__(self):
        return 'Subsidio gas licuado, ' +str(self.pertenece)

    class Meta:
        verbose_name = 'Subsidio gas licuado'
        verbose_name_plural = 'Subsidios gas licuado'
        db_table = 'subsidio_gas'
        ordering = ['id']

class Verificacion(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    estado = models.BooleanField(verbose_name='Verificacion',default=False)
    aceptado = models.BooleanField(verbose_name='Aceptada')


    def __str__(self):
        if(self.estado):
            if(self.aceptado):
                return 'Aceptada'
            else:
                return 'Rechazada'
        else:
            return 'En proceso verificacion'
    class Meta:
        verbose_name = 'Verificacion'
        verbose_name_plural = 'Verficaciones'
        db_table = 'verificacion'
        ordering = ['id']

class Solicitud(models.Model):
    pertenece = models.OneToOneField(Usuario, on_delete=models.PROTECT)
    estado = models.OneToOneField(Verificacion,on_delete=models.PROTECT)
    subsidio_transporte = models.ForeignKey(SubsidioTransporte,on_delete=models.PROTECT,blank=True,null=True)
    subsidio_luz = models.ForeignKey(SubsidioLuz,on_delete=models.PROTECT,blank=True,null=True)
    subsidio_agua = models.ForeignKey(SubsidioAgua,on_delete=models.PROTECT,blank=True,null=True)
    subsidio_gas_licuado = models.ForeignKey(SubsidioGasLicuado,on_delete=models.PROTECT,blank=True,null=True)

    def __str__(self):
        return str(self.pertenece)
    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        db_table = 'solicitud'
        ordering = ['id']

