import socket

class WAFDetecter:
    def __init__(self, host: str):
        self.host = host


    def run(self):
        hostOn = self.pingDomain()

        if hostOn == False:
            print(' \n[!] Domain is down!')
            return

        print(' \n[✓] Domain up!')



    def pingDomain(self) -> bool:
        print(' \n[#] Pinging Domain first ... ')

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.host, 80))
        except socket.gaierror:
            print('')
            return False
        else:
            sock.close()
            return True


def main():
    domain = input(' Please, type the domain which you want check if firewall exists: ')

    wafDetecter = WAFDetecter(domain)
    wafDetecter.run()



if __name__ == '__main__':
    main()
