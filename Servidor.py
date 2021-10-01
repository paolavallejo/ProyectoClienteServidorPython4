import socket #librería que permitirá crear sockets

mi_socket = socket.socket() # objeto de socket
mi_socket.bind(('localhost',8000)) # Establece la conexión (host, puerto)
mi_socket.listen(2) # Cantidad de peticiones que maneja en cola el socket 

while True:
    conexion, direccion = mi_socket.accept() # Acepta las peticiones de los clientes
    print("Nueva conexión")
    print(direccion)
    
    peticion = conexion.recv(1024)
    print(peticion)
    
    text = "Saludos desde el servidor"
    conexion.send(text.encode("ascii")) # Envío de mensaje al cliente
    conexion.close() # Cierre de la conexión