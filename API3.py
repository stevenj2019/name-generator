from flask import Flask 
import random 
import string 

app = Flask(__name__)

output = list()
for i in range(1, 5):
    output.append(random.choice(string.ascii_lowercase))
return "".join(output)

app.run(host='0.0.0.0')
