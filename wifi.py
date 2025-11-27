import subprocess

def list_wireless_profiles():
    try:
        # Run the netsh command to list profiles
        # check=True raises an error if the command fails
        # capture_output=True captures stdout/stderr
        # text=True decodes the output as string
        result = subprocess.run(
            ["netsh", "wlan", "show", "profiles"],
            capture_output=True,
            text=True,
            check=True
        )
        print("Command Output:\n")
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage for administrative inventory
# list_wireless_profiles()