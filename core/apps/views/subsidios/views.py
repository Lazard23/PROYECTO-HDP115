from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, FormView

from core.apps.forms import *
from core.apps.models import *



# Subsidios trasnporte
class SubsidioTrasnporteListView(ListView):
    # modelo del que sacara los objetos
    model = SubsidioTransporte
    # vista a utilizar
    template_name = 'subsidiosTransporte/lista.html'

    # sobreescribir con decoradores, solicitando que este logeado para entrar a esta pagina
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'name':'Fabio'}
        try:
            sub = SubsidioTransporte.objects.get(pk=request.POST['id']).toJSON()
        except Exception as error:
            data['error'] = str(error)
        # try:
        #     action = request.POST['action']
        #     if action == 'buscardatos':
        #         data = []
        #         for i in SubsidioTransporte.objects.all():
        #             data.append(i.toJSON())
        #     else:
        #         data['error'] = 'Ha ocurrido un error'
        # except Exception as e:
        #     data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['subtitulo'] = 'Datos subisidio transporte público'
        context['titulo'] = 'Subsidios transporte público'

        return context

    def get_queryset(self):
        return SubsidioTransporte.objects.all()
class SubsidioTransporteFormView(FormView):
    form_class = SubsidioTransporteForm
    template_name = 'subsidiosTransporte/create.html'
    success_url = reverse_lazy('apps:subsidio_transporte_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Registro subsidio transporte'
        context['titulo'] = 'Fomulario | Subsidio Transporte'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('apps:subsidio_transporte_lista')
        return context

#Subsidio agua
class SubsidioAguaListView(ListView):
    # modelo del que sacara los objetos
    model = SubsidioAgua
    # vista a utilizar
    template_name = 'subsidioAgua/lista.html'

    # sobreescribir con decoradores, solicitando que este logeado para entrar a esta pagina
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = SubsidioAgua.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['panel'] = 'Panel de administrador'
        context['subtitulo'] = 'Datos subisidio servicio agua'
        context['titulo'] = 'Servicio agua'


        return context

    def get_queryset(self):
        return SubsidioAgua.objects.all()
class SubsidioAguaCreateView(CreateView):
    model = SubsidioAgua
    form_class = SubsidioAguaForm
    template_name = 'subsidiosTransporte/create.html'
    success_url = reverse_lazy('apps:subsidio_transporte_lista')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False)

    #     form = SubsidioAguaForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request,self.template_name,context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Formulario | subsudio agua'
        context['titulo'] = 'Formulario subsidio agua'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('apps:subsidio_transporte_lista')
        return context

#Subsidio luz
class SubsidioLuzListView(ListView):
    # modelo del que sacara los objetos
    model = SubsidioLuz
    # vista a utilizar
    template_name = 'subsidiosTransporte/../../templates/subsidioLuz/lista.html'

    # sobreescribir con decoradores, solicitando que este logeado para entrar a esta pagina
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = SubsidioLuz.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['subtitulo'] = 'Datos subisidio energía eléctrica'
        context['titulo'] = 'Servicio energía eléctrica'

        return context

    def get_queryset(self):
        return SubsidioLuz.objects.all()

#Subsidio Gas
class SubsidioGasListView(ListView):
    # modelo del que sacara los objetos
    model = SubsidioGasLicuado
    # vista a utilizar
    template_name = 'subsidioGas/lista.html'

    # sobreescribir con decoradores, solicitando que este logeado para entrar a esta pagina
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscardatos':
                data = []
                for i in SubsidioTransporte.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador1'
        context['subtitulo'] = 'Datos subisidio gas licuado'
        context['titulo'] = 'Subsidios gas lucuado'

        return context

    def get_queryset(self):
        return SubsidioGasLicuado.objects.all()
class SubsidioGasCreateView(CreateView):
    model = SubsidioAgua
    form_class = SubsidioAguaForm
    template_name = 'subsidiosTransporte/create.html'
    success_url = reverse_lazy('apps:subsidio_transporte_lista')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False)

    #     form = SubsidioAguaForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request,self.template_name,context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Formulario | subsudio agua'
        context['titulo'] = 'Formulario subsidio agua'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('apps:subsidio_transporte_lista')
        return context
# Formularios
class SubsidioTransporteCreateView(CreateView):
    model = SubsidioTransporte
    form_class = SubsidioTransporteForm
    template_name = 'subsidiosTransporte/create.html'
    success_url = reverse_lazy('apps:subsidio_agua_create')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Fomulario | Subsidio Transporte'
        context['panel'] = 'Fomulario | Subsidio Transporte'
        context['subtitulo'] = 'Formulario'
        return context



