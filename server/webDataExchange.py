import socket

# Press ⌃R to execute it.

ap_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
gcs_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ap_out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
gcs_out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ap_socket.setblocking(False)
gcs_socket.setblocking(False)

apDetected=0
gcsDetected=0

def main():
    apInAddress = ('localhost', 1234)
    gcsInAddress = ('localhost', 4321)

    apOutAddress = ('localhost', 1235)

    gcsOutAddress = ('localhost', 4320)
    apData = bytearray(1024)
    gcsData = bytearray(1024)
    apDataCounter = 0
    gcsDataCounter = 0
    print('Webserver has been started')
    createApSocket(apInAddress)
    createGcsSocket(gcsInAddress)
    while True:
        try:
            # receive data on socket 1
            apData, apAddress = ap_socket.recvfrom(1024)
            apDataCounter = apDataCounter + 1
            print(f'AP data received from {apAddress[0]}:{apAddress[1]} :{apData}')
            #apOutAddress=(apAddress[0],apAddress[1])
            gcs_out_socket.sendto(apData,gcsOutAddress)
            apDataCounter -= 1

            # process the data as needed
        except socket.error:
            pass

        try:
            # receive data on socket 2
            gcsData, gcsAddress = gcs_socket.recvfrom(1024)
            gcsDataCounter += 1
            print(f'Gcs data received from {gcsAddress[0]}:{gcsAddress[1]} : {gcsData}')
            #gcsOutAddress=(gcsAddress[0],gcsAddress[1])
            ap_out_socket.sendto(gcsData,apOutAddress)
            gcsDataCounter -= 1

            # process the data as needed
        except socket.error:
            pass

def bindSocket(ipAdress, portNumber)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipAdress, portNumber))
    return sock

def createApSocket(_apInAddress):
    print(f'AP socket has been created at {_apInAddress}')
    ap_socket.bind(_apInAddress)
    #return ap_socket

def createGcsSocket(_gcsInAddress):
    print(f'Gcs socket has been created at {_gcsInAddress}')
    gcs_socket.bind(_gcsInAddress)
    #return gcs_socket

def getLocalIpAddress()
    # Get the hostname of the current machine
    hostname = socket.gethostname()
    # Get the IP address associated with the hostname
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def bindAp()
    sock.bind((UDP_IP, UDP_PORT))


if __name__ == "__main__":
    main()
