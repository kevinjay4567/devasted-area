from django.shortcuts import render
from equipo.models import Clima
from proveedor.views import actualizar_informacion
from django.shortcuts import redirect

# Create your views here.
def mostrar_info(request):
    climas = Clima.objects.all()
    for clima in climas:
        actualizar_informacion(clima.lat, clima.lon)
    return render(request, "info.html", {"climas": climas})

def index_page(request):
    return render(request, 'index.html')

def guardar_info(request):
    if request.method == "POST":
        data = request.POST
        lat = float(data.get('lat'))
        lon = float(data.get('lon'))
        actualizar_informacion(lat, lon)
        return redirect('info')