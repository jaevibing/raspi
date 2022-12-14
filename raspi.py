from flask import Flask, request, jsonify
import time
import asyncio
import RPi.GPIO as GPIO

# references, not actual variables
led = 18
bigchungus = 17
screamer = 27

GPIO.setmode(GPIO.BCM)
for i in (led, bigchungus, screamer):
    GPIO.setup(i, GPIO.OUT)
buzz = GPIO.PWM(screamer, 1000)

app = Flask(__name__)

async def LED(i):
    pin = 17
    if i == 0:
        pin = 18
    GPIO.output(pin, GPIO.HIGH)
    await asyncio.sleep(2)
    GPIO.output(pin, GPIO.LOW)

async def setFreq(i):
    buzz = GPIO.PWM(screamer, i)
    await asyncio.sleep(0.1)

async def screamON():
    buzz.start(1)
    await asyncio.sleep(0.1)

async def screamOFF():
    buzz.stop()
    await asyncio.sleep(0.1)
    
@app.route("/toggleLED", methods=["GET"])
def toggleLED():
    asyncio.run(LED(0))
    return (jsonify(success=True))

@app.route("/togglescream", methods=["GET"])
def togglescream():
    if request.args.get("isOn") == 'true':
        buzz.stop()
    else:
        buzz.start(1)
    return (jsonify(success=True))

@app.route("/setfreq", methods=["GET"])
def setfreq():
    asyncio.run(setFreq(int(request.args.get("freq"))))
    return (jsonify(success=True))

@app.route("/chungus", methods=["GET"])
def chungus():
    asyncio.run(LED(1))
    return (jsonify(success=True))

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
