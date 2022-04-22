from Paciente import Paciente
from Max_heap import MaxHeap

class Menu:
    def emergencia_menu():
        global ordem
        global contador
        while (True):
            print("1. Novo paciente ")
            print("2. Chamar paciente ")
            print("3. Mostrar próximo paciente ")
            print("4. Mostrar os 5 últimos pacientes ")
            escolha_opcao = int(input("Escolha sua opção: "))
            if (escolha_opcao == 1):
                nome_paciente = input("Qual o nome do paciente? ")
                tipo_sanguineo = input("Qual o tipo sanguineo do paciente? ")
                data_nascimento = input("Qual a data de nascimento do paciente? ")
                paciente = Paciente(nome_paciente, tipo_sanguineo, data_nascimento)
                prioridade_atendimento = int(input("Qual a prioridade do atendimento? "))
                ordem = 0
                item=(prioridade_atendimento, ordem, Paciente.__str__(paciente))
                maxheap.put(item)
                ordem = ordem + 1
                contador = contador - 1
                print('Limite atendimento do sus = ', contador)
            elif (escolha_opcao == 2):
                if (maxheap.peek()):
                    atendimentos.append(maxheap.peek())
                    print(maxheap.get())
                else:
                    print("Não há mais pacientes a ser atendidos!")
                    break

            elif (escolha_opcao == 3):
                if (maxheap.peek()):
                    print(maxheap.peek())
                else:
                    print("Não há pacientes na fila de espera!")
                    break
            
            elif (escolha_opcao == 4):
                if(len(atendimentos) <= 4):
                    for i in range(len(atendimentos)):
                        print(atendimentos[i])
                else:
                    for i in range(1, 6):
                        print(atendimentos[len(atendimentos) - i])
    
   
atendimentos = list()
maxheap = MaxHeap()
ordem = 0
contador = 999
Menu.emergencia_menu()