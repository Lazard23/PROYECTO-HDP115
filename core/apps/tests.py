from primer_proyecto.wsgi import *
from core.apps.models import subsidioTransporte

# #listar objetos
# object = subsidioTransporte.objects.all()
# #filtra
# object2 = subsidioTransporte.objects.get(pk=4)
# print(object2)
# print(object)
#
# #Insercion
# creado = subsidioTransporte(cantidadSubsidio=10.5,cantidadBuses=3,cantidadMicrobuses=3,frecuenciaUso='Semanal')
# creado.save()

#Edicicion
# object2 = subsidioTransporte.objects.get(pk=4)
# object2.cantidadSubsidio = 15
# object2.save()

#eliminacion
#eliminado = subsidioTransporte.objects.get(pk=5).delete()

#consultas avanzadas
consulta = subsidioTransporte.objects.filter(cantidadSubsidio__in=[7.00])

#contar
consulta2 = subsidioTransporte.objects.filter(cantidadSubsidio__range=[10,20]).exclude(pk=3)
#consulta3 = subsidioTransporte.objects.filter(cantidadSubsidio__iregex=).exclude()

print(consulta2)
