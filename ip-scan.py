import socket
import ipaddress
from colorama import Fore, Style

#je mes beaucoup d'ashta

# Fonction de vérification de l'adresse IP
def is_valid_ip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False

# Fonction de scan de port
def port_scan(host, port):
    # Créez un objet socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        # Tentez de vous connecter à l'adresse et au port spécifiés
        s.connect((host, port))
        print(f"{Fore.GREEN}Le port {port} est ouvert{Style.RESET_ALL}")
    except:
        # Si la connexion échoue, le port est probablement fermé
        print(f"{Fore.RED}Le port {port} est fermé{Style.RESET_ALL}")
    finally:
        # Fermer la connexion
        s.close()

# Afficher une bannière "Port Scanner"
print(f"{Fore.CYAN}\n{'-'*50}\nPort Scanner\n{'-'*50}{Style.RESET_ALL}\n")

# Obtenez le nom d'hôte ou l'adresse IP du site web à scanner
target_host = input("Entrez l'adresse IP du site web à scanner: ")

# Vérifier si l'adresse IP est valide
if not is_valid_ip(target_host):
    print(f"{Fore.RED}Adresse IP invalide{Style.RESET_ALL}")
    exit()

# Définir les ports à scanner (par défaut, nous scannerons les ports 1 à 1024)
target_ports = range(1, 1025)

# Demander à l'utilisateur s'il souhaite exécuter le scanner de port ou accéder aux informations
option = input("Entrez '1' pour scanner les ports, ou '2' pour accéder aux informations: ")

if option == "1":
    # Boucle à travers les ports cibles et effectuez le scan de port
    for port in target_ports:
        port_scan(target_host, port)
elif option == "2":
    # Afficher les informations
    print(f"{Fore.CYAN}\n{'-'*50}\nInformations\n{'-'*50}{Style.RESET_ALL}\n")
    print("Voici mon Youtube : https://youtube.com/@zeidensad4923")
    print("Voici mon Discord : https://discord.gg/")
else:
    print("Option invalide. Veuillez entrer '1' ou '2'.") 
