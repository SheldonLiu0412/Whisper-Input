import rumps
import subprocess
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

class WhisperInputApp(rumps.App):
    def __init__(self):
        super().__init__("🎤", quit_button=None)
        
        # 加载环境变量
        load_dotenv()
        
        # 设置菜单项
        self.menu = [
            rumps.MenuItem("启动", callback=self.start_whisper),
            rumps.MenuItem("停止", callback=self.stop_whisper),
            None,  # 分割线
            rumps.MenuItem("退出", callback=self.quit_app)
        ]
        
        self.whisper_process = None
        
    def start_whisper(self, _):
        if self.whisper_process:
            print("Whisper Input 已经在运行中")
            return
            
        try:
            # 获取项目根目录
            project_path = Path(__file__).parent
            
            # 使用当前 Python 解释器
            python_path = sys.executable
            
            # 激活虚拟环境并运行 main.py
            self.whisper_process = subprocess.Popen(
                [python_path, "main.py"],
                cwd=str(project_path),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            self.title = "🎤 Hi"
            print("Whisper Input 服务已启动")
            
        except Exception as e:
            print(f"启动失败: {str(e)}")
    
    def stop_whisper(self, _):
        if self.whisper_process:
            self.whisper_process.terminate()
            self.whisper_process = None
            self.title = "🎤"
            print("Whisper Input 服务已停止")
    
    def quit_app(self, _):
        if self.whisper_process:
            self.stop_whisper(_)
        rumps.quit_application()

if __name__ == "__main__":
    WhisperInputApp().run() 