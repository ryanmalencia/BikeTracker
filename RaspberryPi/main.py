import bluetooth
import RPi.GPIO as GPIO        #calling for header file which helps in using GPIOs of PI
LED=21
 
GPIO.setmode(GPIO.BCM)     #programming the GPIO by BCM pin numbers. (like PIN40 as GPIO21)
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT)  #initialize GPIO21 (LED) as an output Pin
GPIO.output(LED,0)
 
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
server_socket.bind(("",bluetooth.PORT_ANY))
server_socket.listen(1)
port = server_socket.getsockname()[1]
uuid = 'f2801eef-31c3-4eb7-a95f-e635ada1fab4'
port = 1
bluetooth.advertise_service(server_socket,"MyServer" ,service_id=uuid)
 
client_socket,address = server_socket.accept()
print "Accepted connection from ",address
while 1:
 
 data = client_socket.recv(1024)
 print "Received: %s" % data
 if (data == "0"):    #if '0' is sent from the Android App, turn OFF the LED
  print ("GPIO 21 LOW, LED OFF")
  GPIO.output(LED,0)
 if (data == "1"):    #if '1' is sent from the Android App, turn OFF the LED
  print ("GPIO 21 HIGH, LED ON")
  GPIO.output(LED,1)
 if (data == "q"):
  print ("Quit")
  break
 
client_socket.close()
server_socket.close()
