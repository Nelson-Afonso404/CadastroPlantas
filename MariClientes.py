while True:
	import termcolor
	from termcolor import colored
	
	print(colored('CADASTRO DE CLIENTES', 'green'))
	nome=input(colored('digite o nome: ', 'yellow'))
	planta=input(colored('digite o nome da planta: ', 'yellow'))
	valor=input(colored('digite o valor pago: ', 'yellow'))

	arquivo = open('MariClientes.txt','a')
	arquivo.write(str(nome)  + '\n')
	arquivo.write('Comprou: ')
	arquivo.write(str(planta) + "\n")
	arquivo.write('E pagou R$')
	arquivo.write(str(valor) + "\n")
	arquivo.write('##################' + '\n')
	arquivo.close()

# Lendo o arquivo criado:
	arquivo = open('MariClientes.txt','r')
	for linha in arquivo:
	    linha = linha.rstrip()
	    print (linha)
	arquivo.close()
