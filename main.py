#Este arquivo define a função principal

import frontend as frontend

afd = frontend.input_afd()
if afd:


    for i in range(int(input("Processar Quantas strings? "))):
        string_para_processar = input("Digite uma string para processar. ")
        print(afd.processa_string(string_para_processar))

else:
    print("Erro.\n")