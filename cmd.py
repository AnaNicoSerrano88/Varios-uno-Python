from subprocess import check_output

cmd_serial_number = check_output("wmic Baseboard get SerialNumber").decode().split("\n")[1].strip()

print(cmd_serial_number)