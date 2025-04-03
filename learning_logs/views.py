from django.shortcuts import render
from .models import Topic
def index(request):
    '''
    Função da página principal do learning_log
    '''
    return render(request, 'learning_logs/index.html')


def topics(request):
    """
    Mostra todos os assuntos/tópicos do site
    """
    topic = Topic.objects.order_by
    """
    Em resumo, vou pegar todo o objeto que está no models Topic
    (tudo que está dentro do banco de dados de Topic), e eu quero ordenar para
    
    """
