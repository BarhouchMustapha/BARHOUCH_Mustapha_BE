import socket


def attente_communication(adresse, port):
    ecoute = socket.socket()
    ecoute.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    ecoute.bind((adresse, port))
    ecoute.listen()

    # accept retourne un tuple (socket, adresse)
    client = ecoute.accept()[0]

    ecoute.close()

    return client


def initialisation_communication(adresse, port):
    serveur = socket.socket()
    serveur.connect((adresse, port))

    return serveur


def fin_communication(connexion: socket.socket):
    connexion.close()


def communication_fermee(connexion: socket.socket):
    connexion.recv()


def emission(connexion: socket.socket, donnees: str):
    envoyes = 0
    while envoyes < len(donnees):
        # Seuls les octets non envoyés du tableau sont réenvoyés
        envoyes += connexion.send(donnees[envoyes:])


def reception(connexion: socket.socket):
    octets = connexion.recv(4096)

    return octets
