import socket                   #Import the library socket
from apisockets import *        #Import the api realised on the 1st BE

HOST, PORT = '', 80           #Define 8080 as a port of the server

def serveClient(client):             #Definir une fonction qui prend en paramétres le client 
    rqstData = reception(client).decode('utf-8')    #Rcevoire la requéte envoyé par le client et la décoder en modéle utf-8
    rqstMethod, rqstPath, _ = rqstData.split(' ', 2) 
    """ Mettre la méthode (GET ou HEAD) dans la 1er variable et le chemin de fichier demandé dans  la 2eme variable et le reste de 
    la requéte dans la variable _ qu'on va plus utilisé dans notre programme """
    if rqstMethod == 'GET' or rqstMethod == 'HEAD':     #on vérifie si la méthode de la requéte est bien un GET ou HEAD
        if rqstPath == '/':
            fileName = 'index.html'                            
            rqstPath = "/"+fileName
        try:                            #On essaye si le ficier HTML demander est trouvé           
            f = open('./' + rqstPath, 'r')          #Ouvrir le fichier html
            fileContent= f.read()                      #Lire le fichier HTML
            f.close()
            respHeaders = f'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(fileContent)}\r\n\r\n'
            #Envoyer une réponse HTTP avec le Code 200 0K indiquant que la requéte est traité avec succés et que le contenue de la réponse seras un fichier html
            if rqstMethod == 'GET':
                respBody = fileContent #Si la méthode est un "GET" en renvoi le contenue de fichier HTML qui vas étre affiché dans le navigateur
            else:
                respBody = ''          #Si la méthode est un "HEAD" rien ne seras pas afficher sur le navigateur
        except FileNotFoundError:      #Si on trouve pas un fichier HTML demandé
            respHeaders = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\n'
            #Envoyer une réponse HTTP avec le code 404 indiquant que le serveur n'as pas trouvé le fichier HTML demandé
            respBody = '404 Not Found'  #Le contenue afficher en navigateur
    else: #Si la méthode n'est pas ni GET ni HEAD
        respHeaders = 'HTTP/1.1 405 Method Not Allowed\r\nContent-Type: text/plain\r\n\r\n'
        #encoyer une réponse HTTP avec le code 405 indiquant que la méthode n'est pas reconnue
        respBody = 'Method Not Allowed'  #Le contenue afficher en navigateur
    resp = respHeaders.encode('utf-8') + respBody.encode('utf-8')   #La reponse est donc La réponse HTTP et le fichier ou le contenue à afficher dans le navigateur
    emission(client,resp)  #Envoyer la réponse au client
    fin_communication(client)   # Fermer la connexion avec le client

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverHTTP:
    serverHTTP.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverHTTP.bind((HOST, PORT))    #Lier le serveur avec le port et le host
    serverHTTP.listen()              #mettre le serveur en mode écoute et attendre les connexions entrantes.
    print(f'Listening on {HOST}:{PORT}')
    while True:     #Tant que le serveur est en mode écoute
        client_socket, client_address = serverHTTP.accept()   #Accepter la connexion qui retourne le client socket et son adresse
        print('Connected by', client_address)
        serveClient(client_socket)                     #Appel de la fonction serveClient qui permet de servir le client