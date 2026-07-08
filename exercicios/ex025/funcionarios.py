from abc import ABC,abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    salario_min = 1612
    desconto_inss = 7.5
    def __init__(self,nome = None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        base = self.salario / Funcionario.salario_min
        conteudo = f" O salário de [blue]{self.nome}[/] (Funcionário {self.__class__.__name__}) é de [green]{self.salario:.2f}[/]\n e corresponde a [yellow]{base:.1f}[/] salários mínimos."
        print(Panel(conteudo,title="Análise de sálario",expand=False))

class Horista(Funcionario):
    def __init__(self,nome,valor_hora = 7.37,horas_trab = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora *self.horas_trab

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.desconto_inss/100)



class Mensalista(Funcionario):
    def __init__ (self,nome, salario = 1612):
        super().__init__(nome)
        self.sal_bruto = salario

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.desconto_inss/100)




