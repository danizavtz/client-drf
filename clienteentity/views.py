import json
from urllib import parse as urlparse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from clienteentity.models import Cliente
from clienteentity.serializers import ClienteSerializer

@csrf_exempt
def cliente_list(request):
    """
    Lista todos os Clientes ou cria um novo.
    """
    if request.method == 'POST':
        return criar_cliente(request)
    clientes = Cliente.objects.all()
    serializer = ClienteSerializer(clientes,many=True)
    return JsonResponse(serializer.data, safe=False)

def criar_cliente(request):
    serializer = ClienteSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def cliente_detail(request, pk):
    """
    Pega, atualiza ou exclui cliente.
    """
    try:
        cliente = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = json.dumps(urlparse.parse_qs(request.body.decode('utf-8')))
        d1 = data.replace('[',"")
        d1 = d1.replace(']',"")
        print('Raw Data: "%s"' % d1)
        saida = json.loads(d1)
        serializer = ClienteSerializer(cliente, data=saida)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=204)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cliente.delete()
        return HttpResponse(status=204)