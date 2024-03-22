import subprocess
def separate_vocals(file_path):
    command = ["demucs", "--mp3", file_path]
    try:
        #Execute the demucs command
        result = subprocess.run(command, check=True,capture_output=True, text=True)
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occured While running demucs: {e}")
if __name__ == "__main__":
    file_path = ""C:\Users\ASUS\Music\perfect.mp3" "
    separate_vocals(file_path)
