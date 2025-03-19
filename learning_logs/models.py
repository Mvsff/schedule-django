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
    