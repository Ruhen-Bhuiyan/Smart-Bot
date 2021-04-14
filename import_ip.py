import socket
hostname=socket.gethostname()
myip=socket.gethostbyname(hostname)

file_object = open('C:/Users/asia/Desktop/Bot/import.txt', 'a')
file_object.write(myip)
file_object.write("\n")
file_object.close()
