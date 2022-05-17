import random

#função para tornar lista aleatoria em forma de inteiros e utilizar como index.
def randomizar(lista):
    random_numbers = random.sample(range(len(lista)), 10)
    return random_numbers
#função principal do game, responsavel ler os arquivos de perguntas e aleatoriza-las e salvar novamente nos arquivos,
# precisa de melhorias para deixar o game mais interessante 
def game_perguntas(lista,pontuacao,jogador):
        while True:  
            aleat = randomizar(lista)
            for e in aleat:
              z= lista.index(lista[e])
              print(f'''\n{lista[e]}\n
  [A] {alternativa_a[z]}
  [B] {alternativa_b[z]} 
  [C] {alternativa_c[z]} 
  [D] {alternativa_d[z]}
              ''')
            
              while True: 
                resposta = input('Resposta')
                if resposta.isnumeric() == True:
                        print('Digite apenas Letras')
                elif resposta.upper() != 'A' and resposta.upper() != 'B' and resposta.upper() != 'C' and resposta.upper() != 'D':
                      print('digite uma Alternativa A, B, C, ou D!')
                elif resposta.upper() == lista_resposta[z]:
                  print('acertou')
                  pontuacao = pontuacao + 1 
                  break
                else:
                  print('errou')
                  break
            score_total.append(pontuacao)
            jogadores.append(jogador)
            lista_teste.append(pontuacao)

            sc= open("lista_pontuação.txt",'a')
            sc.write(str(pontuacao) + "\n")
            sc.close()

            j = open("lista_jogadores.txt", 'a')
            j.write(str(jogador) + "\n")
            j.close()

            lt =open('lista_score_final.txt','a')
            lt.write(str(pontuacao) + "\n")
            lt.close()
            
            break
            
        return print(f'\n O seu Score foi {pontuacao} ponto(s).')
#função para alterar item nas listas
def alterar_lista(lista,posicao,novo):
    lista[posicao] = novo
    return print(lista)
# função para altera itens nas listas, nessa função tem o uso de uma outra função no caso a de altera_lista
def alterar_itens_lista(lista):
         while True: 
          for e in lista:
              print(f'[{lista.index(e)}]  {e}')

          posicao = (input('Qual item voce deseja alterar? Digite o indice'))
          if posicao.isnumeric() == False:
            print('\n*********DIGITE UM NUMERO********\n')
          else:  
            if int(posicao) >= len(lista):
              print(f'\n********DIGITE UM NUMERO MENOR QUE {len(lista)}!********\n')
            elif int(posicao) < len(lista):
              nome_modificar = input(f'alterar {lista[int(posicao)]} para: ')
              alterar_lista(lista,int(posicao),nome_modificar)
              
              
              return print(f'O nome foi modificado para {nome_modificar}')
#função responsavel para regravar os arquivos ou seja copiar um arquivo em cima do outro
def salvar(arquivo,lista):

 with open(arquivo, 'w') as temp_file:
    for item in lista:
        temp_file.write("%s\n" % item)
 return 
#função para criar um arquivo em lista
def mk_lista (arquivo):
    with open(arquivo, "r") as texto:
        linhas = texto.readlines()
        linhas = list(map(lambda s: s.strip(), linhas))
    return linhas
#funçao para conferir se item ja existe no arquivo
def conferir(arquivo, frase):
    with open(arquivo) as f:
        for l_num, l in enumerate(f, 1): # Anda pelas linhas a partir da 1
            if frase == l.strip(): # Verifica se a palavra esta na linha
                return l_num
        return 0 # retorna 0 caso não seja encontrada
#função para cadastro de perguntas
def dic_perg(arquivo):
  perguntas_total ={}
    #lista_prod = list()
    
  while True:
    quant_perguntas = input('Quantidade de perguntas para cadastrar: ')
    if quant_perguntas == '0':
      break
    if quant_perguntas.isnumeric() == False:
      print('Digite Apenas Numeros')
    else:
     quant_perguntas = int(quant_perguntas)
    for c in range(0,quant_perguntas):
       
        while True:  
          perguntas_total['Perguntas'] = str(input('Digite uma pergunta: '))
          if  perguntas_total['Perguntas'].isnumeric() == True:
            print('Não digite apenas números')
          elif len(perguntas_total['Perguntas']) < 10:
            print('Digite uma Frase Maior que 10 caracteres')
          elif conferir('perguntas.txt', perguntas_total['Perguntas'].strip()) >= 1:
            print('pergunta já existe')
          else: 
              break
          
        while True:
          perguntas_total['A'] = str(input('Digite a Alternativa A: '))
          if perguntas_total['A'].isnumeric() == True:
            print('Digite Palavras')
          elif len(perguntas_total['A']) < 1:
            print('Por favor digitar palavra maior que 1 digito(s))')
          elif len(perguntas_total['A']) > 30:
            print('Por favor digitar palavra menor que 30 digito(s))')
          elif conferir('alternativaA.txt',perguntas_total['A'].strip()) >= 1:
            print('Alternativa A ja existe')
          else:
            break
        while True:
          perguntas_total['B'] = str(input('Digite a Alternativa B: '))
          if perguntas_total['B'].isnumeric() == True:
            print('Digite Palavras')
          elif len(perguntas_total['B']) < 1:
            print('Por favor digitar palavra maior que 1 digito(s))')
          elif len(perguntas_total['B']) > 30:
            print('Por favor digitar palavra menor que 30 digito(s))')
          elif conferir('alternativaB.txt',perguntas_total['B'].strip()) >= 1:
            print('Alternativa B ja existe')
          else:
            break

        while True:
          perguntas_total['C'] = str(input('Digite a Alternativa C: '))
          if perguntas_total['C'].isnumeric() == True:
            print('Digite Palavras')
          elif len(perguntas_total['C']) < 1:
            print('Por favor digitar palavra maior que 1 digito(s))')
          elif len(perguntas_total['C']) > 30:
            print('Por favor digitar palavra menor que 30 digito(s))')
          elif conferir('alternativaA.txt',perguntas_total['C'].strip()) >= 1:
            print('Alternativa C ja existe')
          else:
            break 

        while True:
          perguntas_total['D'] = str(input('Digite a Alternativa D: '))
          if perguntas_total['D'].isnumeric() == True:
            print('Digite Palavras')
          elif len(perguntas_total['D']) < 1:
            print('Por favor digitar palavra maior que 1 digito(s))')
          elif len(perguntas_total['D']) > 30:
            print('Por favor digitar palavra menor que 30 digito(s))')
          elif conferir('alternativaA.txt',perguntas_total['D'].strip()) >= 1:
            print('Alternativa D ja existe')
          else:
            break
        while True:
          perguntas_total['R'] = str(input('Digite a resposta apenas a "Alternativa": '))
          if str(perguntas_total['R'].upper()).strip() != 'A' and str(perguntas_total['R'].upper()).strip() != 'B' and str(perguntas_total['R'].upper()).strip() != 'C' and str(perguntas_total['R'].upper()).strip() != 'D':
            print('Difirente')
          else:
            print(perguntas_total['R'])
            break
        perguntas.append(perguntas_total['Perguntas'])
        alternativa_a.append(perguntas_total['A'])
        alternativa_b.append(perguntas_total['B'])
        alternativa_c.append(perguntas_total['C'])
        alternativa_d.append(perguntas_total['D'])
        lista_resposta.append(perguntas_total['R'].upper())

        p= open("perguntas.txt",'a')
        p.write(str(perguntas_total['Perguntas']) + "\n")
        p.close()

        aa = open("alternativaA.txt", 'a')
        aa.write(str(perguntas_total['A']) + "\n")
        aa.close()

        ab = open("alternativaB.txt", 'a')
        ab.write(str(perguntas_total['B']) + "\n")
        ab.close()

        ac = open("AlternativaC.txt", 'a')
        ac.write(str(perguntas_total['C']) + "\n")
        ac.close()

        ad = open("AlternativaD.txt", 'a')
        ad.write(str(perguntas_total['D']) + "\n")
        ad.close()

        r= open("respostas.txt", 'a')
        r.write(str(perguntas_total['R'].upper()) + "\n")
        r.close()

    return perguntas_total

#listas
#usa a função mk_lista para transformar o arquivo em lista.
score = 0
perguntas = mk_lista('perguntas.txt')
alternativa_a= mk_lista('alternativaA.txt')
alternativa_b= mk_lista('alternativaB.txt')
alternativa_c= mk_lista('alternativaC.txt')
alternativa_d= mk_lista('alternativaD.txt')
lista_resposta= mk_lista('respostas.txt')
score_total = mk_lista('lista_pontuação.txt')
jogadores = mk_lista('lista_jogadores.txt')
lista_teste = mk_lista('lista_score_final.txt')

                

while True: #laço para finalizar apenas se a opção com break for acionada
    
    lista_score_decre = {jogadores[i]: int(score_total[i]) for i in range(len(jogadores))}#lista descrescente
    
    print('''
  [1]JOGAR
  [2]CADASTRAR PERGUNTAS
  [3]REMOVER PERGUNTAS
  [4]EDITAR PERGUNTAS
  [5]LISTA DE PERGUNTAS
  [6]SCORE GAME
  [7]FECHAR GAME
          ''')

    menu_game = str(input('DIGITE UMA OPÇÃO\n'))
#Menu Principal**************************************     
    if menu_game == '1' or menu_game == '2' or menu_game == '3' or menu_game == '4' or menu_game == '5' or menu_game == '6' or menu_game == '7': #menu
#menu 1 Inicia o jogo chamando a função*************************************************************
        if menu_game ==  '1':
          
            print('Que os jogos comecem!')
            while True:
                nickname = input('Digite seu Apelido de jogador')
                if conferir('lista_jogadores.txt', nickname.strip()) >= 1:
                    print('Nickname Já Existe')
                else:
                    game_perguntas(perguntas,score,nickname)

                    salvar('lista_jogadores.txt',jogadores)
                    salvar('lista_pontuação.txt',score_total)
                    salvar('lista_score_final.txt', lista_teste)
                    break
#menu 2 Permite cadastrar perguntas , precisa de uma implementação de senha pro adm*************************************************************
        if menu_game == '2':
            list_game = dic_perg('tudo.txt')
            print('ok')
#menu 3 Permite excluir perguntas , precisa de uma implementação de senha pro adm*************************************************************      
        if menu_game == '3':
        
              while True:
                print('Qual produto deseja excluir?')

                for e in perguntas:
                  v = perguntas.index(e)
                  print(f'{e} codigo : {v}')
                
                cod_prod_exc = (input('Digite o Codigo do produto'))
                if cod_prod_exc.isnumeric() == False:
                  print('Digite apenas numeros')
                elif int(cod_prod_exc) > v:
                  print(f'Digite um numero de 0 a {v}')
                elif int(cod_prod_exc) <= v:
                  e_index = int(cod_prod_exc)
                  print(e_index)
                  
                  del perguntas[e_index]
                  del alternativa_a[e_index]
                  del alternativa_b[e_index]
                  del alternativa_c[e_index]
                  del alternativa_d[e_index]
                  del lista_resposta[e_index]

                  salvar('perguntas.txt',perguntas)
                  salvar('alternativaA.txt',alternativa_a)
                  salvar('alternativaB.txt',alternativa_b)
                  salvar('alternativaC.txt',alternativa_c)
                  salvar('alternativaD.txt',alternativa_d)
                  salvar('respostas.txt',lista_resposta)
                  break
                else:
                  print('Codigo errado')
#menu 4 Permite editar perguntas , precisa de uma implementação de senha pro adm*************************************************************
        if menu_game == '4':
            while True: 
                  print('\nQual item você deseja modificar?\n')

                  print('''
                  [1] Nome
                  [2] Alternativa A
                  [3] Alternativa B
                  [4] Alternativa C
                  [5] Alternativa D
                  [6] Resposta
                  [0] Voltar
                  
                  ''')
                  menu_login5 = input('Digite o indice')
                  if menu_login5.isnumeric() == False:
                    print('\n*********DIGITE O NUMERO 1, 2, 3 OU 4********\n')
                  else:
                    if menu_login5 == "1":
                      alterar_itens_lista(perguntas)
                    elif menu_login5 =='2':
                      alterar_itens_lista(alternativa_a)
                    elif menu_login5 =='3':
                      alterar_itens_lista(alternativa_b)
                    elif menu_login5 =='4':
                      alterar_itens_lista(alternativa_c)
                    elif menu_login5 =='5':
                      alterar_itens_lista(alternativa_d)
                    elif menu_login5 =='6':
                      alterar_itens_lista(lista_resposta)
                    elif menu_login5 =='0':
                      break
#menu 5 Permite ver as perguntas , precisa de uma implementação de senha pro adm*************************************************************
        if menu_game == '5': 
          print('\n   LISTA \n')
          print('\nNOME : QUANTIDADE .\n')
          for e in perguntas:
                  z = perguntas.index(e)
                  print(f'{e}')
#menu 6 mostra a lista decrescente do jogadores por pontos*************************************************************      
        if menu_game == '6':
            print('SCORE GERAL\n')

            print('''PONTUAÇÃO   :  JOGADOR\n ''')
            e = 0 
            for i in sorted(lista_score_decre, key = lista_score_decre.get, reverse=True):
                e = e + 1
                if e <= 10:
                 
                 print(
                  f'''{e}     {str(lista_score_decre[i])}      :   {i}
                  ''')
                else:
                  break
#menu 7 fecha o jogo*************************************************************
        if menu_game == '7':
            break
