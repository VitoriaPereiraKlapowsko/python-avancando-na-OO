class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title() #Title deixa todas as 1° letras em maiusculo
        self.ano = ano
        self._likes = 0
      
    @property  
    def likes(self):
        return self._likes
    
    def dar_like(self):
        self._likes += 1 # Adiciona 1 na minha contagem de likes
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter #Definindo um setter para pegar valores, no caso aqui estou pegando o valor do nome
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
        
class Filme(Programa): #Herdando informações da classe Programa
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title() 
        self.ano = ano
        self.duracao = duracao
        self._likes = 0
    
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0

vingadores = Filme('vigadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')


atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}') 