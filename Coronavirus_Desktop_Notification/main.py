from plyer import notification
import time


def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon='G:\My Projects\Python Projects\Coronavirus_Desktop_Notification\img.ico',
        timeout=15

    )


if __name__ == "__main__":
    notifyme("Lets Stop The Spread Of This Virus", "Sanitize Your Hands")
    time.sleep(1800)
