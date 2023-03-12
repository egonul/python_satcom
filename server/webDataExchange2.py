import socket

# Press ⌃R to execute it.

ap_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
gcs_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# if the script runs on the local machine set to 1; otherwise 0

myLocal = 1

if myLocal == 1:
    serverAddress = 'localhost'
else:
    # Get the hostname of the current machine
    hostname = socket.gethostname()
    # Get the IP address associated with the hostname
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(('8.8.8.8', 1))  # connect to a dummy address
        ip_address = s.getsockname()[0]
    print(f"Hostname: {hostname}")
    print(f"Ethernet adapter IP address: {ip_address}")
    serverAddress = ip_address

apInAddress = (serverAddress, 1234)
gcsInAddress = (serverAddress, 4321)


def main():
    apData = bytearray(1024)
    gcsData = bytearray(1024)
    try:
        print(f'Webserver has been started at {serverAddress}')
        apDataCounter = 0
        gcsDataCounter = 0
        apConnected = 0
        gcsConnected = 0
        try:
            ap_socket = bindSocket(apInAddress)
            gcs_socket = bindSocket(gcsInAddress)
        except socket.error:
            print('Input ports can not be opened')
            exit()
        print('Waiting for data...')
        while True:
            try:
                # receive data on socket 1
                apData, apAddr = ap_socket.recvfrom(1024)
                apAddress = (apAddr[0], apAddr[1])
                apConnected = 1
                print(f'AP data received from {apAddr[0]}:{apAddr[1]} :{apData}')
                apDataCounter = apDataCounter + 1
                if gcsConnected == 1:
                    gcs_socket.sendto(apData, gcsAddress)
                    apDataCounter -= 1
                    print(f'AP data: >{apData}< sent to GCS at >{gcsAddress}<')
            except socket.error:
                pass

            try:
                # receive data on socket 2
                gcsData, gcsAddr = gcs_socket.recvfrom(1024)
                gcsConnected = 1
                gcsDataCounter += 1
                print(f'Gcs data received from {gcsAddr[0]}:{gcsAddr[1]} : {gcsData}')
                gcsAddress = (gcsAddr[0], gcsAddr[1])
                gcsDataCounter = gcsDataCounter + 1
                if apConnected == 1:
                    ap_socket.sendto(gcsData, apAddress)
                    print(f'GCS data: >{gcsData}< sent to AP at >{apAddress}<')
                    gcsDataCounter -= 1
            except socket.error:
                pass
    except KeyboardInterrupt:
        print("Terminating the script...")
        ap_socket.close()
        gcs_socket.close()
        print("Sockets have been closed")


def bindSocket(ipAddr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(ipAddr)
    sock.setblocking(False)
    print(sock)
    return sock


def getLocalIpAddress():
    # Get the hostname of the current machine
    hostname = socket.gethostname()
    # get the IP address of the Ethernet adapter
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(('8.8.8.8', 1))  # connect to a dummy address
        ip_address = s.getsockname()[0]

    print(f"Hostname: {hostname}")
    print(f"Ethernet adapter IP address: {ip_address}")
    return ip_address


if __name__ == "__main__":
    main()
