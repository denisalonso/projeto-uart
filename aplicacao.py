#####################################################
# Camada Física da Computação
#Carareto
#11/08/2022
#Aplicação
####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 


from enlace import *
import time
import numpy as np


serialName = "COM9"

def main():
    try:
        print("Iniciou o main")
        # declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com1 = enlace(serialName)
        
        # ativa comunicacao. Inicia os threads e a comunicação seiral 
        com1.enable()

        # se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        print("Abriu a comunicação")
                  
        # aqui você deverá gerar os dados a serem transmitidos. 
        # seus dados a serem transmitidos são um array bytes a serem transmitidos. Gere esta lista com o 
        # nome de txBuffer. Esla sempre irá armazenar os dados a serem enviados.
        
        imageR = './uart.png'
        imageW = './copia-recebida.png'

        # txBuffer = imagem em bytes!
        txBuffer = open(imageR, 'rb').read()
       
        print("meu array de bytes tem tamanho {}" .format(len(txBuffer)))
         
        # finalmente vamos transmitir os todos. Para isso usamos a funçao sendData que é um método da camada enlace.
        print('A transmissão vai começar!')
        com1.sendData(np.asarray(txBuffer))
    
        # A camada enlace possui uma camada inferior, TX possui um método para conhecermos o status da transmissão
        # O método não deve estar fincionando quando usado como abaixo. deve estar retornando zero. Tente entender como esse método funciona e faça-o funcionar.

        # print('getAllBuffer: {}'.format(com1.rx.getBuffer(com1.rx.getBufferLen())))

        # print('Bufferlen rx: {}'.format(com1.rx.getBufferLen()))
        txSize = com1.tx.getStatus()

        # print('getAllBuffer: {}'.format(com1.rx.getAllBuffer(com1.rx.getBufferLen())))
        
        print(f'enviou = {txSize:.0f} bytes')
        
        #Agora vamos iniciar a recepção dos dados. Se algo chegou ao RX, deve estar automaticamente guardado
        #Observe o que faz a rotina dentro do thread RX
        #print um aviso de que a recepção vai começar.
        
        #Será que todos os bytes enviados estão realmente guardadas? Será que conseguimos verificar?
        #Veja o que faz a funcao do enlaceRX  getBufferLen
      
        #acesso aos bytes recebidos
        txLen = len(txBuffer)
        rxBuffer, nRx = com1.getData(txLen)
        print("recebeu {} bytes" .format(len(rxBuffer)))

        f = open(imageW, 'wb')
        f.write(rxBuffer)

        # print('Buffer len rx:{}'.format(com1.rx.getBufferLen()))
        
        # print('getAllBuffer: {}'.format(com1.rx.getAllBuffer(com1.rx.getBufferLen())))

        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        

if __name__ == "__main__":
    main()
