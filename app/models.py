from django.db import models

# Gerenciar Cidades
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"
    
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

# Gerenciar Ocupações Pessoais
class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Ocupação Pessoal")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

# Gerenciar Pessoas
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Pessoa")
    pai = models.CharField(max_length=100, verbose_name="Nome do Pai")
    mae = models.CharField(max_length=100, verbose_name="Nome da Mãe")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF da Pessoa")
    data_nasc = models.DateField(verbose_name="Data de Nascimento da Pessoa")
    email = models.CharField(max_length=100, verbose_name="E-mail da Pessoa")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da Pessoa")
    ocupacao = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Ocupação da Pessoa")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

# Gerenciar Instituicões de Ensino
class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Institução de Ensino")
    site = models.CharField(max_length=100, verbose_name="Site da Instituição de Ensino")
    telefone = models.CharField(max_length=19, verbose_name="Telefone da Instituição de Ensino")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da Instituição de Ensino")

# 3.2.1
    # Gerenciar Áreas do Saber