import socket
import ipaddress
from colorama import Fore, Style

#je mes beaucoup d'ashta

# Fonction de v�rification de l'adresse IP
def is_valid_ip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False

# Fonction de scan de port
def port_scan(host, port):
    # Cr�ez un objet socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        # Tentez de vous connecter � l'adresse et au port sp�cifi�s
        s.connect((host, port))
        print(f"{Fore.GREEN}Le port {port} est ouvert{Style.RESET_ALL}")
    except:
        # Si la connexion �choue, le port est probablement ferm�
        print(f"{Fore.RED}Le port {port} est ferm�{Style.RESET_ALL}")
    finally:
        # Fermer la connexion
        s.close()

# Afficher une banni�re "Port Scanner"
print(f"{Fore.CYAN}\n{'-'*50}\nPort Scanner\n{'-'*50}{Style.RESET_ALL}\n")

# Obtenez le nom d'h�te ou l'adresse IP du site web � scanner
target_host = input("Entrez l'adresse IP du site web � scanner: ")

# V�rifier si l'adresse IP est valide
if not is_valid_ip(target_host):
    print(f"{Fore.RED}Adresse IP invalide{Style.RESET_ALL}")
    exit()

# D�finir les ports � scanner (par d�faut, nous scannerons les ports 1 � 1024)
target_ports = range(1, 1025)

# Demander � l'utilisateur s'il souhaite ex�cuter le scanner de port ou acc�der aux informations
option = input("Entrez '1' pour scanner les ports, ou '2' pour acc�der aux informations: ")

if option == "1":
    # Boucle � travers les ports cibles et effectuez le scan de port
    for port in target_ports:
        port_scan(target_host, port)
elif option == "2":
    # Afficher les informations
    print(f"{Fore.CYAN}\n{'-'*50}\nInformations\n{'-'*50}{Style.RESET_ALL}\n")
    print("Voici mon Youtube : https://youtube.com/@zeidensad4923")
    print("Voici mon Discord : https://discord.gg/")
else:
    print("Option invalide. Veuillez entrer '1' ou '2'.") 