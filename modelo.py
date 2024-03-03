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
        
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'
        
class Filme(Programa): #Herdando informações da classe Programa
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) #Chamando o inicializador (__init__) da classe mãe (Programa), ou seja peguei informações que já tinham na classe Programa e juntei com as informações que tinham na classe Filme
        self.duracao = duracao
        
    def __str__(self): #Definindo uma representação textual para o meu objeto 
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'
        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'
       
vingadores = Filme('vigadores - guerra infinita', 2018, 160)
vingadores.dar_like()
atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)