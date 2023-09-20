import ping3, sys, time
from colorist import Color

with open('hosts.txt') as f1:
    devices = list(line for line in (l.strip() for l in f1) if line)

date = time.strftime("%Y%m%d")
with open(f'results_{date}.log', 'a') as f2:
    # Redirect stdout to both the console and the file
    class MultiFile(object):
        def __init__(self, *files):
            self.files = files
        def write(self, text):
            for file in self.files:
                file.write(text)
    sys.stdout = MultiFile(sys.stdout, f2)

    for device in devices:
        ping_result = ping3.ping(device)
        print(f'Ping {device} :', f'{Color.GREEN}PASS{Color.OFF}' if type(ping_result) is float else f'{Color.RED}FAIL{Color.OFF}')

# Restore stdout to its original value
sys.stdout = sys.__stdout__
