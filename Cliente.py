import socket

mi_socket = socket.socket()
mi_socket.connect(('localhost',8000)) # Dirección y puerto a los que se se conecta el cliente

text = "Saludos desde el cliente"
mi_socket.send(text.encode("ascii")) # Envío de mensaje

respuesta = mi_socket.recv(1024) # recibe la respuesta del servidor, 1024 bytes


print(respuesta.decode("ascii"))

mi_socket.close() # Cierre de la conexión