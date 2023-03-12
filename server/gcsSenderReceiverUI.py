import sys
from PyQt5.QtCore import QByteArray, QDataStream, QTimer, QIODevice
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QUdpSocket and bind it to a local address and port
        self.socket = QUdpSocket(self)
        self.socket.bind(QHostAddress.LocalHost, 4322)
        self.socket.readyRead.connect(self.process_pending_datagrams)



        # Create a QLabel to display received data
        self.label1 = QLabel(self)
        self.label1.move(20, 20)
        self.label1.setText("Waiting for data...")

        # Send data every second
        self.counter = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.send_data)
        self.timer.start(1000)

    def send_data(self):
        # Create a datagram with the current counter value
        datagram = QByteArray()
        stream = QDataStream(datagram, QIODevice.WriteOnly)
        stream.writeInt32(self.counter)
        self.counter += 1

        # Send the datagram to a remote address and port
        remote_address = QHostAddress.LocalHost
        remote_port = 4321
        self.socket.writeDatagram(self.counter.to_bytes(self.counter, 'little'), remote_address, remote_port) #counter yerine datgram vardi

    def process_pending_datagrams(self):
        # Read and process any pending datagrams
        while self.socket.hasPendingDatagrams():
            datagram, host, port = self.socket.readDatagram(self.socket.pendingDatagramSize())
            #stream = QDataStream(datagram)
            #received_value = stream.readInt32()
            self.label1.setText(f"Received data: {datagram}")
            self.label1.resize(300, 20)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.setGeometry(100, 100, 300, 200)
    widget.show()
    sys.exit(app.exec_())
