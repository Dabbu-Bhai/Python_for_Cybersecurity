import subprocess

#directly executes the command on terminal 
# subprocess.run(["echo","hello world"])

## Using subprocess to execute a command and capture its output
# result = subprocess.run(["ls","-la"], capture_output=True, text=True)
# print(result.stdout)

##popen allows continuous interaction with process such as ping command
# process = subprocess.Popen(["ping","-c","4","google.com"], stdout=subprocess.PIPE, text=True)
# for line in process.stdout:
#     print(line, end="")

# TIPS: 
# Avoid shell=True for untrusted input
# Sanitize inputs
# Use subprocess.run over os.system