import subprocess

target = r'.\keylogger\main.py'
exeLocation = r'.\keylogger\EXE'

args = f'python -m PyInstaller --onefile --distpath {exeLocation} {target}'.split()

subprocess.run(args)