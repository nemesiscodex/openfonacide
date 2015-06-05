from django.forms import ModelForm
from models import Reportes

class ReporteForm(ModelForm):
    class Meta:
        model = Reportes
        fields = (
            'id_prioridad', 'tipo', 'codigo_establecimiento', 'codigo_institucion', 'nombre_institucion', 'periodo',
            'cedula', 'nombre', 'apellido', 'email', 'telefono', 'motivo', 'observacion'
        )
