import os
import time

url = 'http://172.16.16.223:3300/'
s_id = 'abc'
prv=[]

def match(data):
  if s_id in data or '---'in data:
    return True
  elif s_id[0]+'-'+s_id[2] in data:
    return True
  elif s_id[0]+'-'+'-' in data:
    return True
  elif s_id[0]+s_id[1]+'-' in data:
    return True
  return False

def getData():
  data = os.popen('curl '+url).read()
  return(list(data.split(',')))

def action():
  data=getData()
  print(data)
  if match(data):
    print(data[-1])
    if data[-1]=='0':
      prv.clear()
    if data[-1] not in prv:
      print(data[-2])
      os.popen(data[-2])
      prv.append(data[-1])

while(True):
  try:
    action()
  except:
    print('error')
  time.sleep(5)