import socket                   #Import the library socket
from apisockets import *        #Import the api realised on the 1st BE




Host , Port = "127.0.0.1" , 80  # 80 Le port utilisé pour les connexions HTTP
                                # "127.0.0.1" @IP de serveur apache installé localement
Rqst = b'GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n' # Requéte HTTP formaté

Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Création d'un objet socket 

Client.connect((Host,Port)) # Connection au serveur 
emission(Client,Rqst)        # Envoyer la requéte en utilisant la fonction développpé en apisockets

resp = b""      # Définir une variable pour recevoir la répense de type binaire 
while True:
    data = reception(Client) #Utilisation de la fonction reception développé en apisockets
    if not data:             #Tester si data est vide 
        break                #Au cas au data est vide donc il fait un break donc il sort de la boucle while
    resp += data

# affichage de la réponse HTTP en la décode sous la norme utf-8
print(resp.decode('utf-8'))
# Fermeture de la connexion en utilisant la fct fin_communication développé BU apisockets
fin_communication(Client)




