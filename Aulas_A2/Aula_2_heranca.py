# Mesmo essa classe não tendo entre parênteses, a (classe) que ela herda, ela acaba herdando da classe object
# É a mesma coisa que "class Animal(object):"
class Animal:
    """
    Esta é a classe que representa todos os animais.;
    """
    def __init__(self, nome, especie):
        """
        Construtor para inicializar o objeto animal.
        

        Args:
            nome (str): O nome do animal.
            especie (str): A espécie do animal.
        """ 
        self.nome = nome
        self.especie = especie

    def fala(self):
        """
        Faz o animal falar.

        Returns:
            str: Uma mensagem que representa a fala do animal.
        """   
        return f"{self.nome} diz Olá!"

    def __str__(self):
        """
        String que representao animal.

        Returns:
            str: Uma string com o nome do animal e sua espécie. 
        """    
        return f"{self.nome} {self.especie}"
    
    def __repr__(self):
        pass

class Cachorro(Animal):
    """
    Uma classe que representa um Cachorro, herança da classe Animal.
    """

    def __init__(self, nome, raca):
        """
        Construtor para inicializar o objeto animal.
        

        Args:
            nome (str): O nome do animal.
            raca (str): A raça do animal.
        """ 
        super().__init__(nome, especie="Cachorro")
        self.raca = raca

    def fala(self):
        """
        Faz o latido do Cachorro.

        Returns:
            str: Uma mensagem que representa o latido do cachorro.
        """
        return f"{self.nome} late. Woof!"
    
    def abana_o_rabo(self):
        """
        Faz o Cachorro balançar o rabo.

        Returns:
            str: Uma mensagem que representa o cachorro balnaçando o rabo.
        """
        return f"{self.nome} balança esse rabo!"
    
class Gato(Animal):
    """
    Uma classe que representa um Gato, herança da classe Animal.
    """

    def __init__(self, nome, cor):
        """
        Construtor para inicializar o objeto animal.
        

        Args:
            nome (str): O nome do animal.
            cor (str): A cor do animal.
        """ 
        super().__init__(nome, especie="Gato")
        self.cor = cor

    def fala(self):
        """
        Faz o meow do Gato.

        Returns:
            str: Uma mensagem que representa o meow do Gato.
        """
        return f"{self.nome} faz meow. Meow!"
    
    def ronrona(self):
        """
        Faz o Gato ronronar.

        Returns:
            str: Uma mensagem que representa o gato ronronando.
        """
        return f"{self.nome} ronrone. Graa!"    

# Criando instâncias das classes Cachorro e Gato    
meu_cachorro = Cachorro("Bilu", "Viralata")
meu_cachorro.nome = "Chun Li"
meu_cachorro.especie = "Cadela"

# Chamando métodos para demonstrar as funcionalidades
print(meu_cachorro.fala())
print(meu_cachorro.abana_o_rabo())

# Mostre a informação sobre os animais 
print(meu_cachorro)
