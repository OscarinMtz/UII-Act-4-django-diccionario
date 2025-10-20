from django.shortcuts import render

def index(request):
    productos_spa = [
        {"nombre": "Mascarilla Facial de Arcilla", "precio": 35.00, "ingredientes_clave": "Arcilla verde, aloe vera"},
        {"nombre": "Aceite Corporal Relajante", "precio": 45.00, "ingredientes_clave": "Lavanda, manzanilla, aceite de almendras"},
        {"nombre": "Sales de Baño Desintoxicantes", "precio": 28.50, "ingredientes_clave": "Sales del Himalaya, eucalipto, menta"},
        {"nombre": "Exfoliante Corporal de Café", "precio": 30.00, "ingredientes_clave": "Café molido, aceite de coco, azúcar morena"},
        {"nombre": "Crema Hidratante para Manos y Pies", "precio": 22.00, "ingredientes_clave": "Manteca de karité, vitamina E, caléndula"},
    ]
    contexto = {'productos': productos_spa}
    return render(request, 'index.html', contexto)