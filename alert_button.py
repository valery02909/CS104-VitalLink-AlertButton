import time
import requests
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

url = 'https://api.telegram.org/bot8778899049:AAEvALq6vmJXJav90hge9p_iWBehAWkdlcU/sendMessage'
myobj = {
    "chat_id": "8365387079",
    "text": "Hey, I am Valery.Let\'s grab some cookies"
}
button_pressed = False
while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        button_pressed = True
        x = requests.post(url, json = myobj)
        print(x.text)

        print("Someone pressed the post button!")
    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False
    time.sleep(0.1)

