import socket

# Press ⌃R to execute it or replace it with your code.

to_web_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
from_web_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
to_gcs_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
from_gcs_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


ap_socket.setblocking(False)
gcs_socket.setblocking(False)


def main():
    webDestAddr = ('localhost', 4321)
    gcsDestAddr = ('localhost', 47778)
    gcsSourceAddr = ('localhost', 47777)
    webSourceAddr = ('localhost', 4320)
    apData = bytearray(1024)
    gcsData = bytearray(1024)
    apDataCounter = 0
    gcsDataCounter = 0
    print('Webserver has been started')
    from_gcs_socket.bind(gcsDestAddr)
    from_web_socket.bind(webSourceAddr)
    to_gcs_socket.bind(gcsSourceAddr)

    while True:
        try:
            # receive data from gcs sw and send to web
            gcsData, gcsAddr = from_gcs_socket.recvfrom(1024)
            gcsDataCounter = gcsDataCounter + 1
            print(f'GCS data received from {gcsAddr[0]}:{gcsAddr[1]} :{gcsData}')
            #apOutAddress=(apAddress[0],apAddress[1])
            to_web_socket.sendto(gcsData,webDestAddr)
            gcsDataCounter -= 1

            # process the data as needed
        except socket.error:
            pass

        try:
            # receive data from web server and send to gcs sw
            webData, webAddr = from_web_socket.recvfrom(1024)
            webDataCounter = webDataCounter + 1
            print(f'Web data received from {webAddr[0]}:{webAddr[1]} :{webData}')
            # apOutAddress=(apAddress[0],apAddress[1])
            to_gcs_socket.sendto(webData, gcsDestAddr)
            webDataCounter -= 1

            # process the data as needed
        except socket.error:
            pass

if __name__ == "__main__":
    main()
