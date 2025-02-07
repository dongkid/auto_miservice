# Auto MIcont Service

## 描述
Auto MIcont Service 是一个用于监控micont_service Windows服务状态并在服务启动后停止该服务并启动小米电脑管家的Python脚本。

## 功能
- 检查micont_service服务是否正在运行。
- 如果服务正在运行，则停止该服务。
- 启动小米电脑管家程序。

## 使用方法

### 使用Python脚本
- 确保您具有管理员权限
- 修改脚本内的program_path变量为你的小米电脑管家路径
- 通过任务计划程序设置开机启动：
按 Win + R 输入 taskschd.msc
右侧菜单选择 "创建任务"
常规选项卡：
名称：MI Controller Handler  
勾选 "使用最高权限运行"
触发器选项卡 → 新建 → 选择 "登录时"
操作选项卡 → 新建：
操作：启动程序  
程序或脚本：pythonw.exe  
添加参数（可选）：C:\path\to\amis_r1.py  
起始于（可选）：C:\path\to\（脚本所在目录）  
确定保存任务

### 使用编译后的EXE文件
1. 安装编译工具：
```bash
pip install pyinstaller
```

2. 编译为独立exe文件：
```bash
pyinstaller --onefile --uac-admin amis_r1.py
```

3. 编译完成后：
- 生成的exe文件在dist目录
- exe文件会自动注册到开机启动项
- 直接运行exe即可（首次需要管理员权限）

## 编译说明
- 使用PyInstaller打包为独立可执行文件
- 添加--uac-admin参数确保获取管理员权限
- 编译后的exe可能被误报为病毒，需添加杀毒软件白名单

## 依赖
- Python 3.x
- Windows操作系统

## 注意事项
- 请确保脚本中的服务名称和程序路径正确无误。
- 脚本会尝试以管理员权限运行，如果当前用户没有管理员权限，脚本会提示并重新运行。
