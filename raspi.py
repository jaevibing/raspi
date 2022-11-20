from flask import Flask,  Response, request
import time
import RPi.GPIO as GPIO

led = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

app = Flask(__name__)

@app.route("/led", methods=["GET"])
def led():
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(led, GPIO.LOW)