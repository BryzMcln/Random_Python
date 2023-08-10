import subprocess

def run_ping_command():
    command = "ping youtube.com -t"
    
    try:
        # Open a new Command Prompt window and execute the command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        while True:
            # Read the output of the command
            output = process.stdout.readline()
            if not output and process.poll() is not None:
                break
            
            # Decode the output and print
            print(output.decode('utf-8').strip())
        
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    run_ping_command()
