import subprocess
subprocess.run(["python3", "-m", "venv", ".venv"])
subprocess.run([".venv/bin/pip", "install", "-r", "requirements.txt"])