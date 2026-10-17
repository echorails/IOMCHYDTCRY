import math 
from flask import Flask
from flask import request


app = Flask(__name__)

@app .route('/rpak7723_gmail_com', methods=['GET'])
def HOK():
    x = request.args.get('x')
    y = request.args.get('y')
    if x is None or y is None or not x.isdigit() or not y.isdigit():
        return "NaN", 200, {"Content-Type": "text/plain"}
    x = int(x)
    y = int(y)
    if x == 0 or y == 0:
        return "0", 200, {"Content-Type": "text/plain"}
    gcd = math.gcd(x,y)
    lcm = (x * y) // gcd
    return str(lcm), 200, {"Content-Type": "text/plain"}
app.run()

