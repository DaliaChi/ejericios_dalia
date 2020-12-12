import socket
import re
socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# nos conectamos a la direcion y al puerto del server
ip = "127.0.0.1"
port = 8001
socket_server.bind((ip,port))
socket_server.listen(5) # Màximo de conecciones
print(f"\n\nServer Listening on {ip}:{port}")



salir = False
while salir == False:
    conexion, address = socket_server.accept()
    print ("la conexion ha sido establecida")

    ar1=open("mensaje.txt","r")
    cont=ar1.read()
    print(cont)
    test_str = cont
    ar1.close()            



    while True:
        message = conexion.recv(1024)
        message = message.decode()
        print(message)    



        if message == 'exit':
            message = 'GOOD-BYE...'
            conexion.send(message.encode())
            print("\n")
            salir = True
            break



        elif message == 'HOLA':                                         
            message = ("¡HOLA! que tal como estas, soy el server DALIA ABIGAIL CHI POOT. Seleccione una opcion  :\n\n1. Variables válidas."
                        "\n2. Enteros y decimales.\n3. Operadores aritméticos.\n4. Operadores relacionales.\n"
                        "5. Palabras reservadas.\n\n")
            conexion.send(message.encode())
        

        elif message == '1':
            reg = r'(?s)^((?!hede)[^ ^$1-9])'                             
            matches = re.finditer(reg, test_str, re.MULTILINE)


            for matchNumero, match in enumerate(matches, start=1):
                    

                    message = ("Los resultados encontrados son: = {matchNumero} resultados. ".format(matchNumero = matchNumero, start = match.start(), end = match.end(), match = match.group()))                                           
            if message == '1':
                 message = ("Los resultados encontrados fueron: = 0 resultados. ")                                                           
            conexion.send(message.encode())            

        elif message == '2':
            reg = r"([0-9]{1,3$}$|[0-9]{1,3}\.[0-9]{1,9})"            
            matches = re.finditer(reg, test_str, re.MULTILINE)

            for matchNumero, match in enumerate(matches, start=1):
                    
                    message = ("Los resultados encontrados son: = {matchNumero} resultados ".format(matchNumero = matchNumero, start = match.start(), end = match.end(), match = match.group()))                                                      
            if message == '1'  or message == '2':
                 message = ("Los resultados encontrados fueron: = 0 resultados ")                                                           
            conexion.send(message.encode())





        elif message == '3':
            reg = r'([+]|[]^[]|[*]|-|//|/|%)'                                   
            matches = re.finditer(reg, test_str, re.MULTILINE)

            for matchNumero, match in enumerate(matches, start=1):
                    
                    message = ("Los resultados encontrados son: = {matchNumero} resultados ".format(matchNumero = matchNumero, start = match.start(), end = match.end(), match = match.group()))                                       
            if message == '1'  or message == '3':
                 message = ("Los resultados encontrados fueron: = 0 resultados ")                                                           
            conexion.send(message.encode()) 


        elif message == '4':
            reg = r'(!=|>=|<=|==|<|=|>|<)'                                      
            matches = re.finditer(reg, test_str, re.MULTILINE)

            for matchNumero, match in enumerate(matches, start=1):
                    
                    message = ("Los resultados encontrados son: = {matchNumero} resultados ".format(matchNumero = matchNumero, start = match.start(), end = match.end(), match = match.group()))                                                        
            if message == '1'  or message == '4':
                 message = ("Los resultados encontrados fueron: = 0 resultados ")                                                           
            conexion.send(message.encode())


        elif message == '5':
            reg = r'(?i)(\W|^)(False|await|where|else|import|pass|None|break|except|in|raise|True|class|finally|is|return|and|continue|for|lambda|try|as|def|from|nonlocal|while|assert|del|global|not|with|async|elif|if|or|yield)(\W|$)'                                 
            matches = re.finditer(reg, test_str, re.MULTINE)

            for matchNumero, match in enumerate(matches, start=1):
                    
                    message = ("Los resultados encontrados son: = {matchNumero} resultados. ".format(matchNumero = matchNumero, start = match.start(), end = match.end(), match = match.group()))                                        
            if message == '1' or message == '5':
                 message = ("Los resultados encontrados fueron: = 0 resultados. ")                                                           
            conexion.send(message.encode())                            

        else:
            message = 'No entiendo lo que dices ingresa HOLA de nuevo'            
            conexion.send(message.encode())

conexion.close()
print("Servidor Finalizado")