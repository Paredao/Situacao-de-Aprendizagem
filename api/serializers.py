from rest_framework import serializers
from.models import Tarefa

class TarefaSerializser(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        tasks = ['id', 'titulo', 'descricao', 'completo', 'criado']
        