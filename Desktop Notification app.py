import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Please Drink Water Now!",
            message="Drinking water is good for your health.",
            app_icon="waterglass.ico",
            timeout=2
        )
        time.sleep(1)

