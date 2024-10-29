#componentes
#Miguel Esquivel, Gabriel Pinto

def calcular_inss(salario_base):
    if salario_base <= 1100.00:
        desconto_inss = salario_base * 0.075
    elif salario_base <= 2203.48:
        desconto_inss = salario_base * 0.09
    elif salario_base <= 3305.22:
        desconto_inss = salario_base * 0.12
    elif salario_base <= 6433.57:
        desconto_inss = salario_base * 0.14
    else:
        desconto_inss = 854.36

    return desconto_inss

def calcular_irrf(salario_base, dependentes):
    if salario_base <= 2259.20:
        desconto_irrf = 0
    elif salario_base <= 2826.65:
        desconto_irrf = salario_base * 0.075
    elif salario_base <= 3751.05:
        desconto_irrf = salario_base * 0.15
    elif salario_base <= 4664.68:
        desconto_irrf = salario_base * 0.225
    else:
        desconto_irrf = salario_base * 0.275

    deducao_dependentes = dependentes * 189.59
    desconto_irrf -= deducao_dependentes
    return max(desconto_irrf, 0)

def calcular_descontos(salario_base, vale_transporte, vale_refeicao, dependentes):
    desconto_inss = calcular_inss(salario_base)
    desconto_irrf = calcular_irrf(salario_base, dependentes)

    desconto_vale_transporte = 0
    if vale_transporte.lower() == 's':
        desconto_vale_transporte = salario_base * 0.06

    desconto_vale_refeicao = vale_refeicao * 0.20
    desconto_plano_saude = dependentes * 150.00

    total_descontos = (desconto_inss + desconto_irrf + 
                       desconto_vale_transporte + desconto_vale_refeicao + 
                       desconto_plano_saude)

    salario_liquido = salario_base - total_descontos
    return salario_liquido, total_descontos

matricula = input("Digite sua matrícula: ")
senha = input("Digite sua senha: ")

salario_base = float(input("Digite seu salário base (R$): "))
vale_transporte = input("Deseja receber vale transporte? (s/n): ")
vale_refeicao = float(input("Digite o valor do vale refeição fornecido pela empresa (R$): "))

dependentes = 1

salario_liquido, total_descontos = calcular_descontos(salario_base, vale_transporte, vale_refeicao, dependentes)

print(f"\nSalário Base: R$ {salario_base:.2f}")
print(f"Total de Descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
