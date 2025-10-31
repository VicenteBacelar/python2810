class Calculadora:
    def somar(self, *args):   # recebe grande quantidade de elementos
        return sum(args)
    
calc = Calculadora()

print(calc.somar(1,2))
print(calc.somar(1,2,3,4,5))