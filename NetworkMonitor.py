import time
import subprocess
from datetime import datetime
import os

# Masaüstü yolu (Windows)
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
log_path = os.path.join(desktop, "log.txt")

last_status = None

print("Log dosyası burada:", log_path)

while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = subprocess.run(["ping", "-n", "1", "8.8.8.8"], capture_output=True, text=True)

    if "TTL=" in result.stdout:
        status = "OK"
    else:
        status = "KESİNTİ"

    if status != last_status:
        with open(log_path, "a") as f:
            f.write(f"{now} - {status}\n")
        print(f"{now} - {status}")

    last_status = status
    time.sleep(5)