import subprocess

target = r'.\WIFIPasswords\comp.py'
exeLocation = r'.\WIFIPasswords\exeinhere'

args = f'python -m PyInstaller --onefile --distpath {exeLocation} {target}'.split()

subprocess.run(args)
