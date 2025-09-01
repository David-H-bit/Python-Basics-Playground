import time, datetime

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("ALARM HAS GONE OFF")
            break
        time.sleep(1)


def main():
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)


if __name__ == "__main__":
    main()