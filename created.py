import time
import string
import random
import json

multitab = 20
print('''
  
  ###########################################################################        
           ____            ____              ____            _           _   
          |  _ \ ___  _ __|  _ \ __ _ _ __  |  _ \ _ __ ___ (_) ___  ___| |_ 
          | |_) / _ \| '__| |_) / _` | '__| | |_) | '__/ _ \| |/ _ \/ __| __|
          |  __/ (_) | |  |  __/ (_| | |    |  __/| | | (_) | |  __/ (__| |_ 
          |_|   \___/|_|  |_|   \__,_|_|    |_|   |_|  \___// |\___|\___|\__|
                                                      |__/               
                                                           Not my Idea at all
  ###########################################################################

  ''')
n=0
data ={"acc": []}
jsonobject = json.dumps(data)
def lendata(n):  
  with open("account"+str(n)+".json", "w") as outfile: 
       outfile.write(jsonobject)

while n< multitab :
     lendata(n)
     n=n+1

