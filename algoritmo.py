# algoritmo para ajudar a identificar assédio moral
import numpy
import statistics
print("Este é um teste para descobrir se você sofre assédio moral.\nFoi baseado em um questionário de um estudo realizado pelo departamento pessoal de uma empresa.\n")
print("Responda às perguntas atribuindo uma nota de 1 a 5 conforme as descrições.\n")

#perguntas e pesos
cond_trabalho = {
'p1' : 'Foi exposto a uma carga de trabalho excessiva' ,
'p2' : 'Não lhe davam qualquer ocupação ou tarefas, foi excluído' ,
'p3' : 'Recebeu tarefas que exigem experiência superior às suas competências profissionais' ,
'p4' : 'Retiveram informações que eram essenciais para o seu trabalho' ,
'p5' : 'Retiraram-lhe equipamentos/instrumentos necessários para realizar o seu trabalho' ,
'p6' : 'Houve supervisão excessiva de seu trabalho' ,
'p7' : 'Discriminaram-no seus direitos (ex. salário, turnos, distribuição de tarefas, bónus, despesas de viagem, etc.)' ,
}

preconceito = {
'p8' : 'Não o cumprimentavam nem falavam com você' ,
'p9' : 'Ignoravam a sua presença na frente dos outros' ,
'p10' : 'Impediram-no de se expressar' ,
'p11' : 'Fizeram críticas sobre a sua vida privada' ,
'p12' : 'Zombaram de alguma incapacidade sua' ,
'p13' : 'Foi alvo de ataques com base nas suas crenças religiosas' ,
'p14' : 'Fizeram piadas com base nas suas origens ou nacionalidade' 
}

humilhacao = {
'p15' : 'Foi obrigado a fazer tarefas humilhantes' ,
'p16' : 'Foi humilhado ou ridicularizado em relação ao seu trabalho' ,
'p17' : 'Deram a entender que você tem problemas psicológicos' ,
'p18' : 'Ridicularizaram-no em público' ,
'p19' : 'Fizeram circular maldades e calúnias sobre você' ,
'p20' : 'Imitaram os seus gestos, a sua postura, a sua voz, etc. para o poder ridicularizar' ,
'p21' : 'Elogiavam constantemente seus atributos físicos de forma constrangedora'
}

lesao_corp = {
'p22' : 'Foi alvo de comportamentos intimidatórios tais como: empurrões, bloqueio da sua passagem, invasão do seu espaço pessoal' ,
'p23' : 'Lhe bateram com força usando as mãos (fechadas ou abertas)' ,
'p24' : 'Foi alvo de agressões obscenas' ,
'p25' : 'Atiraram objetos em você' ,
'p26' : 'Foi ferido com algum objeto' ,
'p27' : 'Foi pego pelo braço e puxado' ,
'p28' : 'Foi agredido fisicamente de alguma forma não anteriormente citada' ,
}

def desc():
	print("\
	1--> Nunca aconteceu\n\
	2--> Talvez tenha acontecido alguma vez\n\
	3--> Isso já me aconteceu algumas vezes\n\
	4--> Isso já me aconteceu várias vezes\n\
	5--> Com certeza sempre acontece\n")

lista_cond_trabalho = []
lista_preconceito = []
lista_humilhacao = []
lista_lesao_corp = []
moda = []

print("Em relação à condições de trabalho:")
for k,v in cond_trabalho.items():
	print(v)
	desc()
	resp = int(input("Sua resposta de 1 a 5: "))
	if resp > 0 and < 6:
		lista_cond_trabalho.append(resp)
		continue
	else
		print("Ops! Resposta inválida")

print("Em relação à preconceitos:")
for k,v in preconceito.items():
	print(v)
	desc()
	resp = int(input("Sua resposta de 1 a 5: "))
	if resp > 0 and < 6:
		lista_preconceito.append(resp)
	else
		print("Ops! Resposta inválida")

print("Em relação à humilhações:")
for k,v in humilhacao.items():
	print(v)
	desc()
	resp = int(input("Sua resposta de 1 a 5: "))
	if resp > 0 and < 6:
		lista_humilhacao.append(resp)
	else
		print("Ops! Resposta inválida")

print("Em relação à lesões corporais:")
for k,v in lesao_corp.items():
	print(v)
	desc()
	resp = int(input("Sua resposta de 1 a 5: "))
	if resp > 0 and < 6:
		lista_lesao_corp.append(resp)
	else
		print("Ops! Resposta inválida")

moda_preconceito = statistics.mode(lista_preconceito)
moda_humilhacao = statistics.mode(lista_humilhacao)
moda_lesao_corp = statistics.mode(lista_lesao_corp)
moda.append(moda_lesao_corp)
moda.append(moda_preconceito)
moda.append(moda_humilhacao)
moda_cond_trabalho = statistics.mode(lista_cond_trabalho)
moda.append(moda_cond_trabalho)
moda_geral = statistics.mode(moda)

print('-'*80)
print('De modo geral, suas respostas em maioria foram ',moda_geral)
if(moda_geral>=3):
	print("Suas respostas demonstram que a probabilidade de você estar sofrendo assédio moral é alta.\n")
elif(moda_geral<3):
	print("Suas respostas demonstram que a probabilidade de você estar sofrendo assédio moral é baixa. Em todo caso, fique atento!\n")

print('-'*80)
print('Em relação à condições de trabalho, a maioria das suas respostas foram ',moda_cond_trabalho)
if(moda_cond_trabalho>=3):
	print("Observe suas condições de trabalho, você pode estar correndo risco de desenvolver problemas de saúde\n")

print('-'*80)
print('Em relação à preconceitos no seu trabalho, a maioria das suas respostas foram ',moda_preconceito)
if(moda_preconceito>=3):
	print("Talvez esteja na hora de você dar mais atenção aos preconceitos que sofre, pode evoluir para algo pior.\n")

print('-'*80)
print('Em relação à humilhações no seu trabalho, a maioria das suas respostas foram ',moda_humilhacao)
if(moda_humilhacao>=3):
	print("O ambiente de trabalho deve ser um local de respeito, se você tem problemas não é motivo para ser humilhado(a). Cuide da sua saúde mental!\n")

print('-'*80)
print('Em relação à lesões corporais no seu trabalho, a maioria das suas respostas foram ',moda_lesao_corp)
if(moda_lesao_corp>=3):
	print("Se você não trabalha com lutas, artes marciais, etc., sofrer agressões físicas no trabalho é completamente errado.\nNão permita que ações dessa natureza perdurem na sua vida profissional, pode evoluir para algo pior.\n")