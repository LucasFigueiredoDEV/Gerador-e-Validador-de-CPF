import re
import sys
entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()


nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
indice_dez_digitos = dez_digitos[:10]
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito2 in indice_dez_digitos:
    resultado_digito_2 += int(digito2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = ('{}{}{}'.format(nove_digitos, digito_1, digito_2))
print('CPF: {}'.format(cpf_gerado))

if cpf_enviado_usuario == cpf_gerado:
    print('CPF válido.')
else:
    print('CPF inválido.')
    