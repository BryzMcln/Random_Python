import time, os


def clr():
    os.system("cls")


def stopwatch():
    clr()
    input("Press Enter to start the stopwatch.")
    start_time = time.time()
    try:
        while True:
            elapsed_time = time.time() - start_time
            minutes, seconds = divmod(int(elapsed_time), 60)
            hours, minutes = divmod(minutes, 60)
            print(f"\r{hours:02d}:{minutes:02d}:{seconds:02d}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        print("\nStopwatch stopped.")


if __name__ == "__main__":
    stopwatch()
