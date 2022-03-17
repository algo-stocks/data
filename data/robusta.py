import time
import subprocess
from IPython.core.display import display, Javascript, clear_output

try:
  from urllib import request
except:
  import urllib2 as request


res = request.urlopen('https://auth.aicafe.one/token')
try:
  token = res.read().decode()
except:
  token = res.read()

api = 'https://auth.aicafe.one/api?token='+token

login = 'https://auth.aicafe.one/login#url=https://sites.google.com/view/aicafe1-database&token='+token
expire = str(int(token.split('.')[0]) + 180)
display(Javascript('Date.now()>'+expire+'000 || window.open("'+login+'")'))

print('If popup does not open, please click to this link')
print(login)

for _ in range(58):
  time.sleep(3)
  print('.')
  try:
    res = request.urlopen(api)
    try:
      open('zipline.sh', 'w').write(res.read().decode())
    except:
      open('zipline.sh', 'w').write(res.read())
    
    subprocess.call('sh zipline.sh', shell=True)
    break
  except:
    pass

clear_output()
