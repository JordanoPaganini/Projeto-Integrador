import os

andares = {1: [0, '[1] Primeiro andar', 4], 2: [0, '[2] Segundo andar', 4],
           3: [0, '[3] Terceiro andar', 4], 4: [0, '[4] Quarto andar', 4]}
andar = ['\033[;35m[0] Ver vagas\033[m', '\033[;32m[1] Primeiro andar\033[m', '\033[;32m[2] Segundo andar\033[m',
         '\033[;32m[3] Terceiro andar\033[m', '\033[;32m[4] Quarto andar\033[m']

alotados = []
score = 0
p = '\033[;31m/\033[m'
o = '\033[;32m|\033[m'

while True:

        escolha = int(input('''Deseja:
        [1] Estacionar seu veículo
        [2] Sair com seu veículo\n> '''))
        print()

        if escolha == 1:
                #estacionar
                print('Olá, bem vindo ao estacionamento. Por favor digite o andar qual deseja estacionar')
                #start
                    
                user_input = int(input(f'''\n{'   '.join(andar)}\n\n> '''))
                print('')
                os.system('cls')
                #user_inputs reader and values manager:

                if -2 < user_input <= len(andares):
                    

                    
                    if user_input == 0:
                        for e in andares.keys():
                            print(f"{e}° Andar -> {andares[e][2] * o + (4 - andares[e][2]) * p}")
                        print(f'\nVeículos estacionados hoje: {score}')
                    elif andares[user_input][0] == 4:
                        print('\nAndar Lotado')
                    else:
                        andares[user_input][0] += 1
                        andares[user_input][2] -= 1
                        print(f'''Carro estacionado no {user_input}° andar
            Vagas disponiveis: {andares[user_input][2] * o + (4 - andares[user_input][2]) * p}''')
                        if andares[user_input][0] == 4:
                            alotados.append(andares[user_input][1])
                            andar[user_input] = '\033[;31m' + andares[user_input][1] + '\033[m'
                        score += 1
                        print(f'\nCarros estacionados hoje: {score}')
                    
                   
                    
                else: 
                    print('Andar impossivel')
            
              
                
        elif escolha == 2:
            
                #"desestacionar"
                print('Olá, bem vindo ao estacionamento. Por favor digite o andar onde deseja rertiar seu veículo')
                user_input = int(input(f'''\n\033[;35m[-1] Menu\033[m   {'   '.join(andar)}\n\n> '''))
                print('')
                os.system('cls')
                

                
                if user_input == 0:
                        for e in andares.keys():
                            print(f"{e}° Andar -> {andares[e][2] * o + (4 - andares[e][2]) * p}")
                        print(f'\nVeículos estacionados hoje: {score}')  
                elif andares[user_input][0] <= 0:
                    print(f'Nenhum veículo presente no {user_input}° andar')
                    
                else:
                    andares[user_input][0] -= 1
                    andares[user_input][2] += 1
                    print(f'''Carrro retirado do {user_input}° andar
            Vagas disponiveis: {andares[user_input][2] * o + (4 - andares[user_input][2]) * p}''')
                    if andares[user_input][0] <= 4:
                        alotados.append(andares[user_input][1])
                        andar[user_input] = '\033[;32m' + andares[user_input][1] + '\033[m'
              
           
            
        else:
            print('Escolha impossivel')
        print()
    
