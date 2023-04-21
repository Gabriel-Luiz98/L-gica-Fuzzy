import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

#Variaveis de Entrada (Antecedent)
comer = ctrl.Antecedent(np.arange(0, 10, 1), 'comer')
atividade_fisica = ctrl.Antecedent(np.arange(0, 10, 1), 'atividade_fisica')

#Variaveis de saída (Consequent)
peso = ctrl.Consequent(np.arange(0, 10, 1), 'peso')


#Variaveis de Entrada (Antecedent)
comer['pouco'] = fuzz.trapmf(comer.universe, [-2, 0, 2, 3])
comer['razoavel'] = fuzz.trapmf(comer.universe, [2, 3, 5, 7])
comer['bastante'] = fuzz.trapmf(comer.universe, [3, 5, 11, 12])
atividade_fisica['rara'] = fuzz.trapmf(atividade_fisica.universe, [-2, 0, 2, 3])
atividade_fisica['regular'] = fuzz.trapmf(atividade_fisica.universe, [2, 3, 5, 7])
atividade_fisica['constante'] = fuzz.trapmf(atividade_fisica.universe, [3, 5, 11, 12])
peso['leve'] = fuzz.trapmf(peso.universe, [-1, 0, 3, 5])
peso['medio'] = fuzz.trapmf(peso.universe, [3, 5, 7, 9])
peso['pesado'] = fuzz.trapmf(peso.universe, [7, 9, 11, 12])


#Visualizando as variáveis
comer.view()
atividade_fisica.view()
peso.view()



#Criando as regras
regra_1 = ctrl.Rule(comer['bastante'] | atividade_fisica['rara'], peso['pesado'])
regra_2 = ctrl.Rule(comer['razoavel'] & atividade_fisica['regular'], peso['medio'])
regra_3 = ctrl.Rule(comer['pouco'] | atividade_fisica['constante'], peso['leve'])
regra_4 = ctrl.Rule(comer['bastante'] & atividade_fisica['constante'], peso['medio'])
controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3, regra_4])


#Simulando
CalculoPeso = ctrl.ControlSystemSimulation(controlador)

quantComida = int(input('Comida: '))
quantAtividade = int(input('Frequência de atividade física: '))
CalculoPeso.input['comer'] = quantComida
CalculoPeso.input['atividade_fisica'] = quantAtividade
CalculoPeso.compute()

valorPeso = CalculoPeso.output['peso']

print("\nQuantidade de comida %d \nQuantidade de atividade física %d \nPeso de %5.2f" %(
        quantComida,
        quantAtividade,
        valorPeso))


comer.view(sim=CalculoPeso)
atividade_fisica.view(sim=CalculoPeso)
peso.view(sim=CalculoPeso)

plt.show()