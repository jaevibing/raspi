from flask import Flask, request, jsonify
import time
import asyncio
import RPi.GPIO as GPIO

# references, not actual variables
led = 18
bigchungus = 11
screamer = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

app = Flask(__name__)

async def LED(i):
    pin = 11
    if i == 0:
        pin = 18
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(pin, GPIO.LOW)

@app.route("/toggleLED", methods=["GET"])
def toggleLED():
    LED(0)
    return (jsonify(success=True))

@app.route("/togglescream", methods=["GET"])
def togglescream():
    if request.args.get("isOn") == True:
        GPIO.output(13, GPIO.LOW)
    else:
        GPIO.output(13, GPIO.HIGH)
    return (jsonify(success=True))

@app.route("/chungus", methods=["GET"])
def chungus():
    LED(1)
    return (jsonify(success=True))

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
