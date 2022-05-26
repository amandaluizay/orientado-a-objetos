from restaurante import Restaurante

nome= input("Informe o nome do restaurante: ")
tipo_cozinha= input("Informe o tipo da cozinha: ")
novoRest = Restaurante(nome,tipo_cozinha)
print(novoRest)
print(novoRest.exibir())
novoRest.situacao()
print(novoRest.horario())
print(novoRest.pessoas_atendidas)
valor=novoRest.set_pessoas_atendidas()
print(valor)

