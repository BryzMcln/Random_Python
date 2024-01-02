import subprocess


def ping_youtube():
    try:
        # Run the ping command with the -t option to make it continuous
        subprocess.run(["ping", "youtube.com", "-t"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    ping_youtube()
