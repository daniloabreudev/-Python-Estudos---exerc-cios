from abc import ABC,abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    def __init__(self,nome,salario):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = salario
        self.sal_min = 1612
        self.inss = 7.5

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        conteudo = f" O salário de [blue]{self.nome}[/] é de [green]{self.calc_sal()}[/]\n e corresponde a [yellow]{self.calc_sal()/ self.sal_min:.2f}[/] salários mínimos."
        print(Panel(conteudo,title="Análise de sálario",expand=False))

class Horista(Funcionario):
    def __init__(self,nome,valor_hora,horas_trab):
        super().__init__(nome,valor_hora)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        desconto = (self.inss * self.sal_bruto)/100
        return self.sal_bruto - desconto


class Mensalista(Funcionario):
    def __init__ (self,nome, salario):
        super().__init__(nome,salario)

    def calc_sal(self):
        desconto = (self.inss * self.salario)/100
        return self.salario - desconto



