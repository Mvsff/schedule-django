from django.db import models

# Create your models here.
class Topic(models.Model):
    """
    Um assunto sobre o qual o usuário está aprendendo
    (Comentários é uma boa prática de programação)
    """
    text = models.CharField(max_length=255)

    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
    #Vai obter a data e a hora do sistema, e inserir junto ao 'text'.


class Entry(models.Model):
    """
    Adiciona uma descrição sob o tópico que foi criado
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    #Chave estrangeira, para relacionar a classe "Topic" com o atributo "topic"
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Classe criada APENAS para correção de erro de linguagem do Django,
        quando o Django quiser usar Entry no plural, por padrão ele só
        adiciona um "S" ao final do nome da classe, neste caso ficaria Entrys.
        Ou seja, é unicamente para ajustar esse erro.
        Não é obrigatório, apenas uma boa prática.
        """
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + '...'

    #Retorna apenas os 50 primeiros caracteres de text.

   
        
