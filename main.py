
import socket

from lib.asciiart import Color

class WAFDetecter:
    def __init__(self, host: str):
        self.host = host


    def run(self):
        hostOn = self.pingDomain()

        if hostOn == False:
            print(' \n[!] Domain not found!')
            return

        print(f' \n{Color.BOLD}{Color.GREEN}[✓] Domain up! {Color.RESET}')


    def pingDomain(self) -> bool:
        print(f' \n{Color.BOLD}{Color.YELLOW}[#] Pinging Domain first ... {Color.RESET}')

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.host, 80))
        except OSError as err:
            print(f' \n[!] OSError explodes on screen!')
            print(f' [!] Error: {err}')
            return False
        except socket.gaierror:
            print(f' \n{Color.BOLD}{Color.RED}[!] An exception explodes! {Color.RESET}')
            return False
        else:
            sock.close()
            return True


    def sendAttack(self):
        pass


def main():
    domain = input(f' \n{Color.BOLD}[.] Please, type the domain which you want check if firewall exists: {Color.RESET}')

    wafDetecter = WAFDetecter(domain)
    wafDetecter.run()



if __name__ == '__main__':
    main()
