import socket


def portscanner(ip4):
    vlajka = False
    porty_na_skenovanie = [21, 22, 80, 447, 8000]  # FTP-Nesifrovane, SSH-sifrovane, 80-HTTP, 447-HTTPS, port 8000
    for port in porty_na_skenovanie:
        obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = obj.connect_ex((ip4, port))  # jeden argument - tuple()
        if result == 0:
            print('ADRESA :', ip4, 'PORT :', port, ' JE AKTIVNY')
            vlajka = True
        else:
            pass
        obj.close()
    return True

portscanner('188.121.170.77')  # adresa naseho servera
