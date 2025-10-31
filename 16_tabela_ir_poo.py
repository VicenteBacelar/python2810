class TabelaIr():
    def __init__(self):
        self.tabela = [
            {"faixa":(0,1903), "aliquota":0, "deducao":0},
            {"faixa":(1903,2826), "aliquota":7.5, "deducao":142},
            {"faixa":(2826,3751), "aliquota":15.0, "deducao":354},
            {"faixa":(3751,4664), "aliquota":22.5, "deducao":636},
            {"faixa":(4664,float("inf")), "aliquota":27.5, "deducao":869},
        ]

class CalculadoraIR():
    def __init__ (self, salario_bruto, tabela_ir):
        self.salario_bruto = salario_bruto
        self.tabela_ir = tabela_ir

    def calcular(self) :
        imposto = 0
        for faixa in self.tabela_ir.tabela:
            if self.salario_bruto > faixa["faixa"][0] and self.salario_bruto <= faixa["faixa"][1]:
                imposto = (self.salario_bruto * faixa["aliquota"]) / 100 - faixa["deducao"]
                break
        return imposto

tabela_ir = TabelaIr()
salario_bruto = float(input("Informe seu salario bruto: "))
calculadora = CalculadoraIR(salario_bruto, tabela_ir)
imposto = calculadora.calcular()
print(f"O imposto de renda devido é de R$ {imposto:.2f}")
