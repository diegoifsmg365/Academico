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
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação da Pessoa")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

# Gerenciar Instituições de Ensino
class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Institução de Ensino")
    site = models.CharField(max_length=100, verbose_name="Site da Instituição de Ensino")
    telefone = models.CharField(max_length=19, verbose_name="Telefone da Instituição de Ensino")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da Instituição de Ensino")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

# Gerenciar Áreas do Saber
class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Área do Saber")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"

# Gerenciar Cursos
class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
    carga_horaria_total = models.IntegerField(verbose_name="Carga Horária Total")
    duracao_meses = models.IntegerField(verbose_name="Duração em Meses")
    areaSaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Nome da Área do Saber")
    instituicaoEnsino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Nome da Instituição de Ensino")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

# Gerenciar Turmas
class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Curso")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

# Gerenciar Disciplinas
class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    areaSaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Nome da Área do Saber")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

# Gerenciar Matrículas
class Matricula(models.Model):
    instituicaoEnsino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Nome da Instituição de Ensino")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome da Pessoa")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_previsao_termino = models.DateField(verbose_name="Data de Término")

    def __str__(self):
        return f"{self.data_inicio}, {self.data_previsao_termino}"

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

# Gerenciar Tipos de Avaliação
class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Tipo de Avaliação")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"

# Gerenciar Avaliações
class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Nome da Disciplina")                        
    avaliacaoTipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE, verbose_name="Nome do Tipo de Avaliação")

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

# Gerenciar Frequência
class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Nome da Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome da Pessoa")
    numero_faltas = models.IntegerField(verbose_name="Número de Faltas")

    def __str__(self):
        return self.numero_faltas

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"

# Gerenciar Turnos
class Turno(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Turno")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

# Gerenciar Ocorrências/Advertências
class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Nome da Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome da Pessoa")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

# Gerenciar Disciplinas por Cursos
class CursoDisciplina(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Nome da Disciplina")
    carga_horaria = models.IntegerField(verbose_name="Carga Horária")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do Curso")
    periodo = models.CharField(max_length=100, verbose_name="Período")

    def __str__(self):
        return self.disciplina
    
    class Meta:
        verbose_name = "Curso Disciplina"
        verbose_name_plural = "Cursos Disciplinas"