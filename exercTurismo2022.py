def criarMenu():
    print('1 - cadastrar cliente')
    print('2 - listar clientes')
    print('3 - cadastrar Destino')
    print('4 - listar Destinos')
    print('5 - cadastrar Viagem')
    print('6 - listar viagens')
    print('7 - listar por categorias')
    print('8 - listar para uma cidade')
    print('9 - calcular pontos de clientes')
    print('10 - efetuar pagamento')
    print('11 - informar destino mais procurado')
    print('12 - Dicionario de pontos')

def verificarSeExiste(valor, matriz, coluna):
    for i in range(len(matriz)):
        if valor == matriz[i][coluna]:
            return True
    return False

def verificarIdade(age):
    if age >= 18:
        return True
    else:
        return False

def cadastrarCliente(name, age, matriz):
    lista = [name, age, 0, 0]
    matriz.append(lista)

def listarDados(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def salvarDestino(cidade, valor, min, matriz):
    lista = [cidade, valor, min]
    matriz.append(lista)

def verificarMinimoDiarias(dias, dest, matriz):
    for i in range(len(matriz)):
        if matriz[i][0].upper() == dest.upper():
            if dias >= matriz[i][2]:
                return True #significa que pode fazer a viagem
    return False

def buscarValorDestino(local, matriz):
    for i in range(len(matriz)):
        if matriz[i][0].upper() == local.upper():
            return matriz[i][1]

def cadastrarViagem(cli, dest, dias, tot, matriz):
    lista = [cli, dest, dias, tot]
    matriz.append(lista)

def atualizarValorCliente(name, tot, matriz):
    for i in range(len(matriz)):
        if matriz[i][0].upper() == name.upper():
            matriz[i][2] = matriz[i][2] + tot

def criarListaCidades(matriz):
    lista  = []
    for i in range(len(matriz)):
        existe = False
        for j in range(len(lista)):
            if matriz[i][1] == lista[j]:
                existe = True
        if existe == False:
            lista.append(matriz[i][1])
    return lista

def listarPorCidades(matriz, lista):
    for cidade in lista:
        print('Viagens para '+cidade)
        for i in range(len(matriz)):
            if cidade == matriz[i][1]:
                print(matriz[i])

def calcularPontos(matriz):
    for i in range(len(matriz)):
        pontos = (matriz[i][2]/1000)*100 #poderia dividir por 10
        matriz[i][3] = pontos


def buscarClientesPremiados(matriz):
    lista = []
    for i in range(len(matriz)):
        if matriz[i][3] >= 1500:
            lista.append(matriz[i][0])
    return lista

def buscarDivida(name, matriz):
    for i in range(len(matriz)):
        if matriz[i][0].upper() == name.upper():
            return matriz[i][2]

def abaterDivida (name, divid, matriz):
    for i in range(len(matriz)):
        if name.upper() == matriz[i][0].upper():
            matriz[i][2] = matriz[i][2] - divid

def cadastrar(lis, matriz):
    matriz.append(lis)

def encontrarDestinoMaisProcurado(matriz):
    dicDestinos = {}
    for i in range(len(matriz)):
        if matriz[i][1] in dicDestinos:
            dicDestinos[matriz[i][1]] = dicDestinos[matriz[i][1]] +1
        else:
            dicDestinos[matriz[i][1]] = 1
    print(dicDestinos)
    maior = 0
    cidade = ''
    for chave in dicDestinos.keys():
        if dicDestinos[chave] > maior:
            maior = dicDestinos[chave]
            cidade = chave
    return cidade

def criarDicionarioPontos(matriz):
    dicPontos = {}
    for i in range(len(matriz)):
        if matriz[i][0] in dicPontos:
            dicPontos[matriz[i][0]] = dicPontos[matriz[i][0]] + matriz[i][2]/10
        else:
            dicPontos[matriz[i][0]] = matriz[i][2]/10
    return dicPontos

opcao = -1
clientes = []
destinos = []
viagens = []
while opcao !=0:
    criarMenu()
    opcao = int(input('Digite a opcao: '))
    if opcao == 1:
        nome = input('Digite o nome: ')
        idade = int(input('Digite a idade: '))
        if verificarSeExiste(nome,clientes,0 ) == False:
            if verificarIdade(idade) == True:
                    lista = [nome, idade, 0 , 0]
                   # cadastrar(lista, clientes)
                    cadastrarCliente(nome, idade, clientes)
            else:
                print('Cliente nao tem idade mínima')
        else:
            print('Nome já cadastrado')
    elif opcao ==2:
        listarDados(clientes)
    elif opcao ==3:
        destino = input('Digite o destino: ')
        diaria = float(input('Digite o valor de diária: '))
        minimo = int(input('Digite o nro mínimo de diárias: '))
        salvarDestino(destino, diaria, minimo, destinos)
      #  lista = [destino, diaria, minimo]
      #  cadastrar(lista, clientes)
    elif opcao ==4:
        listarDados(destinos)
    elif opcao ==5:
        cliente = input('Digite o nome do cliente: ')
        if verificarSeExiste(cliente, clientes,0) == True:
            destino = input('Digite o destino: ')
            if verificarSeExiste(destino, destinos, 0) == True:
                diarias = int(input('Digite o total de diárias: '))
                if verificarMinimoDiarias(diarias, destino, destinos) == True:
                    divida = buscarDivida(nome, clientes)
                    if divida < 10000:
                        valor = buscarValorDestino(destino, destinos)
                        total = valor * diarias
                        cadastrarViagem(cliente, destino, diarias, total, viagens)
                        atualizarValorCliente(cliente, total, clientes)
                        print('Dados atualizados com sucesso!')
                    else:
                        print('Divida maior que 10 mil')
                else:
                    print('Nao atende ao minimo de diárias!')
            else:
                print('Destino não existe!')
        else:
            print('Cliente não existe')
    elif opcao ==6:
        listarDados(viagens)
    elif opcao == 7:
        listaDestinos = criarListaCidades(viagens)
        listarPorCidades(viagens, listaDestinos)
    elif opcao ==8:
        cidade = input('Digite o destino desejado')
        listaUnica = [cidade]
        listarPorCidades(viagens, listaUnica)
    elif opcao ==9:
        calcularPontos(clientes)
        listarDados(clientes)
        listaPremiados = buscarClientesPremiados(clientes)
        print(listaPremiados)

    elif opcao == 10:
        nome = input('Digite o nome do cliente: ')
        if verificarSeExiste(nome, clientes, 0) ==True:
            divida = buscarDivida(nome, clientes)
            print('Divida: ' + str(divida))
            valor = float(input('Digite o valor que irá pagar: '))
            if valor > divida: #tem troco
                troco = valor -divida
                print('Troco: ' + str(troco))
                abaterDivida (nome, divida, clientes)
            else:
                abaterDivida(nome, valor, clientes)
        else:
            print('Cliente nao existe!')

    elif opcao == 11:
        destinoMaisProcurado = encontrarDestinoMaisProcurado(viagens)
        print('Destino Mais procurado: ' + destinoMaisProcurado)
    elif opcao ==12:
        dic = criarDicionarioPontos(clientes)
        print('Total de pontos')
        for chave in dic.keys():
            print(chave + ' tem ' + str(dic[chave]) + ' pontos')


