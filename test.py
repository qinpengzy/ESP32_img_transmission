import socket
import cv2
import numpy as np
import struct

# Server address and port
SERVER_ADDR = '192.168.1.13'  # Server IP
SERVER_PORT = 8080  # Server port

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_ADDR, SERVER_PORT))

# Open video file
cap = cv2.VideoCapture('video.mp4')

while (cap.isOpened()):
    # Read frame
    ret, frame = cap.read()

    if ret == True:
        # Encode frame to jpg and get frame size
        result, frame = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
        frame_size = frame.shape
        print("Send length:", frame_size[0])

        # Send frame size
        client_socket.sendall(struct.pack('I', int(frame_size[0])))

        # Send frame data
        frame_data = frame.tobytes()
        client_socket.sendall(frame_data)

    else:
        break

    # Close socket
client_socket.close()
cap.release()