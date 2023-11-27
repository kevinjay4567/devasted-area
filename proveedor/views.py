from equipo.models import Catastrofe
from equipo.models import Clima
from equipo.views import catastrofe_detector

# Create your views here.
def enviar_informacion(nombre, categoria, ubicacion):
    catastrofe = Catastrofe(nombre=nombre, categoria=categoria, ubicacion=ubicacion)
    catastrofe.save()
    return f"Hola desde proveedor - {catastrofe.nombre}"

def actualizar_informacion(lat, lon):
    [timezone, temperature, summary, precipitation, wind] = catastrofe_detector(lat, lon)
    clima = Clima.objects.filter(ubicacion=timezone).first()

    if clima is None:
        clima = Clima()
        clima.ubicacion = timezone
        clima.lat = lat
        clima.lon = lon
        clima.temperatura = temperature
        clima.precipitacion = precipitation
        clima.viento = wind
        clima.resumen = summary
        clima.save()
    else:
        clima.temperatura = temperature
        clima.precipitacion = precipitation
        clima.viento = wind
        clima.resumen = summary
        clima.save()
    return clima
