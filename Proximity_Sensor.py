# Libraries

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# pins
trigger = 18
echo = 16
buzzer = 20

GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)


def distance():
    # set Trigger to HIGH
    GPIO.output(trigger, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trigger, False)

    start_time = time.time()
    stop_time = time.time()

    # save StartTime
    while GPIO.input(echo) == 0:
        start_time = time.time()

    # save time of arrival
    while GPIO.input(echo) == 1:
        stop_time = time.time()

    # time difference between start and arrival
    time_elapsed = stop_time - start_time

    # multiply with the sonic speed
    distance_object = (time_elapsed * 17150)

    return distance_object


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            if dist < 3000:
                GPIO.output(buzzer, GPIO.HIGH)
                time.sleep(0.5)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
