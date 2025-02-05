import subprocess
import time
import ctypes
import os
import win32serviceutil

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def wait_for_service(service_name):
    while True:
        try:
            status = win32serviceutil.QueryServiceStatus(service_name)[1]
            if status == win32serviceutil.SERVICE_RUNNING:
                return
        except Exception as e:
            print(f"Error querying service status: {e}")
        time.sleep(1)

def stop_service(service_name):
    try:
        win32serviceutil.StopService(service_name)
        print(f"Service {service_name} stopped.")
    except Exception as e:
        print(f"Error stopping service: {e}")

def start_program(program_path):
    try:
        subprocess.Popen(program_path)
        print(f"Program {program_path} started.")
    except Exception as e:
        print(f"Error starting program: {e}")

def create_shortcut(script_path):
    path = winshell.startup()
    target = script_path
    wDir = os.path.dirname(script_path)
    icon = script_path

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(os.path.join(path, "AutoMI.lnk"))
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()

def main():
    service_name = "micont_service"
    program_path = r"C:\Program Files\MI\XiaomiPCManager\Launch.exe"

    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return

    wait_for_service(service_name)
    stop_service(service_name)
    start_program(program_path)
    create_shortcut(os.path.abspath(__file__))

if __name__ == "__main__":
    main()