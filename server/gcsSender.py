import socket
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAdress='localhost'
sourceAddress = (serverAdress, 4322)
sock.bind(sourceAddress)

# Set the destination address and port
dest_addr = ('localhost', 4321)

# Start the counter at 0
counter = 1

# Send the counter value every second
while True:
    # Increment the counter
    counter += 2
    print(counter)

    # Convert the counter to bytes
    data = str(counter).encode()

    # Send the data to the destination address and port
    sock.sendto(data, dest_addr)

    # Wait for 1 second before sending the next data
    time.sleep(1)

# Close the socket (this should never happen in this script)
sock.close()
