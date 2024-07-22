from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class AtividadeFisica(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateField()
    duracao = models.DurationField()
    atividade = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.data}, {self.duracao}, {self.atividade}"
    class Meta:
        verbose_name = "Atividade Física"
        verbose_name_plural = "Atividades Físicas"

class AtividadeAlimentar(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateField()
    refeicao = models.CharField(max_length=100)
    cardapio = models.TextField()
    def __str__(self):
        return f"{self.data}, {self.refeicao}, {self.cardapio}"
    class Meta:
        verbose_name = "Atividade Alimentar"
        verbose_name_plural = "Atividades Alimentares"

class Saude(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateField()
    pressao = models.CharField(max_length=20)
    batimentos = models.IntegerField()
    relaxamento = models.TextField()
    medicamentos = models.TextField()
    def __str__(self):
        return f"{self.data}, {self.pressao}, {self.batimentos}, {self.relaxamento}, {self.medicamentos}"
    class Meta:
        verbose_name = "Saúde"
        verbose_name_plural = "Saúde"
