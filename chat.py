import threading
import time
import socket

def build_message(command, user_name, user_message):
  message = command + "|" + user_name + "|" + user_message
  return message

def parse_message(input_message):
  tokenized_message = input_message.split('|')
  command = tokenized_message[0]
  user_name = tokenized_message[1]
  user_message = tokenized_message[2]
  return (command, user_name, user_message)

def send_JOIN_announcement(s, port, my_user_name):
  application_message = build_message("JOIN", my_user_name, "")
  s.sendto(application_message.encode('utf-8'), ("255.255.255.255",port))


def sender(my_user_name, port=12000):
  isRunning = True
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

  broadcast_ip_address = "255.255.255.255"

  send_JOIN_announcement(s, port, my_user_name)

  while isRunning:
    user_message=input("")
    # This is a command
    if (user_message[:1]=="/"): 
      if(user_message[1:6].upper()=="LEAVE"):
        isRunning=False
        application_message = build_message("LEAVE", my_user_name, "")
        s.sendto(application_message.encode('utf-8'), (broadcast_ip_address, port) )
        application_message = build_message("QUIT", "", "")
        s.sendto(application_message.encode('utf-8'), ("127.0.0.1", port) )
        break
      if(user_message[1:6].upper()=="WHO"):
        application_message = build_message("WHO", "", "")
        s.sendto(application_message.encode('utf-8'), ("127.0.0.1", port) )
    # This is a regular message
    else:
      application_message = build_message("TALK", my_user_name, user_message)
      s.sendto(application_message.encode('utf-8'), (broadcast_ip_address, port) )

def get_time():
  time_string = time.strftime('%Y-%m-%d %H:%M:%S.', time.localtime() ) #extract time
  time_string += str(int(round(time.time() * 1000000)))[-6:]
  return time_string

def generate_user_list(userSet):
  resulting_string = ""
  for user_name in userSet:
    resulting_string += ( user_name + ", ")
  resulting_string = resulting_string[:-2]
  return resulting_string

def receive(my_user_name, port=12000):
  isRunning = True
  userSet = set()
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind(("", port))

  s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

  while isRunning:
    (data, _) = s.recvfrom(1024)
    received_message_decoded = data.decode('utf-8')
    (command, user_name, user_message) = parse_message(received_message_decoded)
    
    formatted_time = get_time()
    if (command=='TALK'):
      print ("{0} [{1}]: {2}".format( formatted_time, user_name, user_message ) )
    elif (command == 'JOIN'):
      print("{0} {1} joined!".format(formatted_time, user_name))
      # send a ping
      application_message = build_message("PING", my_user_name, "")
      s.sendto(application_message.encode('utf-8'), ("255.255.255.255", port) )
      # add new user
      userSet.add(user_name)
    elif (command == 'WHO'):
      print("[{0}]".format(generate_user_list(userSet) ) )
    elif (command == 'QUIT'):
      isRunning = False
    elif (command == 'PING'):
      userSet.add(user_name)
    elif (command == 'LEAVE'):
      print ("{0} {1} left.".format( formatted_time, user_name ) )
      if user_name in userSet:
        userSet.remove(user_name)
    else:
      print("I received a command that I did not recognize")
  print ("Bye now!")
      

def main():
  name = input("Enter your name: ")
  port=12000
  try:
    threading.Thread(target=receive, args=(name, port,)).start()
    time.sleep(0.1)
    threading.Thread(target=sender, args=(name, port)).start()
  except:
   print("Error: unable to start thread")

main()