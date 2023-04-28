import subprocess
import pyautogui
import time
import pyperclip
from dotenv import load_dotenv
import os
load_dotenv()

ssh_username = os.getenv('SSH_USERNAME')
ssh_password = os.getenv('SSH_PASSWORD')
pg_username = os.getenv('PG_USERNAME')
pg_password = os.getenv('PG_PASSWORD')

subprocess.Popen(['start', 'cmd'], shell=True)
time.sleep(2)

pyperclip.copy(f'ssh {ssh_username}@ssh2.pgip.universite-paris-saclay.fr')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(0.5)
pyperclip.copy(ssh_password)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(0.5)
pyperclip.copy(f'psql -h tp-postgres -U {pg_username}')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(0.5)
pyperclip.copy(pg_password)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

