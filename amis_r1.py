import ctypes
import sys
import subprocess
import time

def is_service_running(service_name):
    """检查服务是否正在运行"""
    try:
        result = subprocess.run(
            ['sc', 'query', service_name],
            capture_output=True,
            text=True,
            check=True
        )
        return "RUNNING" in result.stdout
    except subprocess.CalledProcessError:
        return False

def stop_service(service_name):
    """停止指定服务"""
    try:
        subprocess.run(
            ['net', 'stop', service_name],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"服务 {service_name} 已成功停止")
    except subprocess.CalledProcessError as e:
        print(f"停止服务失败: {e.stderr}")

def launch_program(program_path):
    """启动指定程序"""
    try:
        subprocess.Popen(
            program_path,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f"已启动程序: {program_path}")
    except Exception as e:
        print(f"启动程序失败: {str(e)}")

def main():
    # 等待服务启动（最长等待5分钟）
    max_retries = 60
    service_name = "micont_service"
    program_path = r"C:\Program Files\MI\XiaomiPCManager\Launch.exe"

    print("正在监控服务状态...")
    for _ in range(max_retries):
        if is_service_running(service_name):
            print("检测到服务已启动，正在尝试停止...")
            stop_service(service_name)
            print("正在启动目标程序...")
            launch_program(program_path)
            return
        time.sleep(5)
    
    print("等待超时，未能检测到服务启动")

if __name__ == "__main__":
    # 检查管理员权限
    if not ctypes.windll.shell32.IsUserAnAdmin():
        # 重新以管理员权限运行
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    
    main()
