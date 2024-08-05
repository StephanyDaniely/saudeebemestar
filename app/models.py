from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class TipoAtividadeFisica(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Tipo Atividade Fisíca"
        verbose_name_plural = "Tipo Atividade Fisíca"

class Refeicao(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Refeição"
        verbose_name_plural = "Refeição"

class AtividadeRelaxamento(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Atividade Relaxamento"
        verbose_name_plural = "Atividade Relaxamento"

class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    descrição = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nome}, {self.descrição}, {self.dose}"
    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"

class Alimento(models.Model):
    nome = models.CharField(max_length=100)
    calorias = models.IntegerField()
    def __str__(self):
        return f"{self.nome}, {self.calorias}"
    class Meta:
        verbose_name = "Alimento"
        verbose_name_plural = "Alimentos"

class AtividadeFisica(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateField()
    duracao = models.DurationField()
    atividade = models.ForeignKey(TipoAtividadeFisica, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.data}, {self.duracao}, {self.atividade}"
    class Meta:
        verbose_name = "Atividade Física"
        verbose_name_plural = "Atividades Físicas"

class AtividadeAlimentar(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateField()
    refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE)
    # alimentos_consumidos = models.ForeignKey(Consumo, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.data}, {self.refeicao}"
    class Meta:
        verbose_name = "Atividade Alimentar"
        verbose_name_plural = "Atividades Alimentares"

class Saude(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateField()
    pressao = models.CharField(max_length=20)
    batimentos = models.IntegerField()
    relaxamento = models.ForeignKey(AtividadeRelaxamento, on_delete=models.CASCADE)
    medicamentos = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.data}, {self.pressao}, {self.batimentos}, {self.relaxamento}, {self.medicamentos}"
    class Meta:
        verbose_name = "Saúde"
        verbose_name_plural = "Saúde"
