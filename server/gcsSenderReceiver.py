import socket
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddress = 'localhost'
sourceAddress = (serverAddress, 4322)
sock.bind(sourceAddress)
sock.setblocking(False)

# Set the destination address and port
dest_addr = ('localhost', 4321)


def main():
    counter = 1000
    startTime = 0

    try:
        while True:
            currentTime = time.monotonic()
            deltaTime = currentTime - startTime

            if deltaTime >= 1:
                counter += 2
                # print(counter)
                # Convert the counter to bytes
                data = str(counter).encode()
                # Send the data to the destination address and port
                sock.sendto(data, dest_addr)
                print(f'{data} is sent to {dest_addr}')
                startTime = currentTime

            try:
                # receive data on socket 1
                recData, recAddr = sock.recvfrom(1024)
                print(f'Data received from {recAddr[0]}:{recAddr[1]} :{recData}')
            except socket.error:
                pass

    except KeyboardInterrupt:
        print("Terminating the script...")
        sock.close()
        print("Socket has been closed")


if __name__ == "__main__":
    main()
