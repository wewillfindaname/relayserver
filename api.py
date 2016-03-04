from flask import Flask
import RPi.GPIO



RPi.GPIO.setmode(RPi.GPIO.BOARD)

RPi.GPIO.setup(8,RPi.GPIO.OUT)
RPi.GPIO.output(8, RPi.GPIO.LOW)

def lower():
    RPi.GPIO.output(8,RPi.GPIO.HIGH)

def higher():
    RPi.GPIO.output(8,RPi.GPIO.LOW)


app = Flask(__name__)

@app.route('/low')
def low():
    lower()
    return "IS OFF....................."

@app.route('/high')
def high():
    higher()
    return "IS ON......................"



if __name__ == '__main__':
    app.run(host='192.168.1.20', port=5000, debug=True)

