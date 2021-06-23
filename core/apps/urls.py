from django.urls import path
from core.apps.views.subsidios.views import *
from core.homepage.views.usuarios.views import UsuarioCreateView
from core.apps.views.dashboard.views import DashBoardView

app_name = 'apps'

urlpatterns = [
    #Inicio
    path('dashboard/', DashBoardView.as_view(),name='dashboard'),
    #LIstados
    #gas licuado
    path('subsidio/gas/listado/', SubsidioGasListView.as_view(),name='subsidio_gas_lista'),
    #energia electrica
    path('subsidio/luz/listado/', SubsidioLuzListView.as_view(),name='subsidio_luz_lista'),
    #servicio agua
    path('subsidio/agua/listado/', SubsidioAguaListView.as_view(),name='subsidio_agua_lista'),
    path('subsidio/agua/agregar/', SubsidioAguaCreateView.as_view(),name='subsidio_agua_create'),
    #transporte publico
    path('subsidio/transporte/listado/', SubsidioTrasnporteListView.as_view(),name='subsidio_transporte_lista'),
    path('subsidio/transporte/agregar/', SubsidioTransporteCreateView.as_view(),name='subsidio_transporte_create'),
    path('subsidio/transporte/formulario/', SubsidioTransporteFormView.as_view(),name='subsidio_transporte_form'),

]