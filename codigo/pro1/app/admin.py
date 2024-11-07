from django.contrib import admin
from app.models import modelo_mas
from django.core.exceptions import ValidationError
from django.utils import timezone

class ModeloMasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'raza', 'tipo', 'edad', 'fecha_nacimiento']

    search_fields = ['nombre', 'raza', 'tipo']

    list_filter = ['tipo', 'raza']

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser 

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def save_model(self, request, obj, form, change):
        if obj.fecha_nacimiento > timezone.now().date():
            raise ValidationError("La fecha de nacimiento no puede ser futura")
        if obj.edad > 99:
            raise ValidationError("La edad no puede ser mayor 99")
        super().save_model(request, obj, form, change)

admin.site.register(modelo_mas, ModeloMasAdmin)
