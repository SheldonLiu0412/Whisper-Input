#!/bin/zsh
cd "$(dirname "$0")"

echo "正在加载 zsh 配置..."
source ~/.zshrc

# 检查是否需要 conda 环境
if [ -f ".env" ]; then
    # 使用 export 导出环境变量
    while IFS='=' read -r key value || [ -n "$key" ]; do
        # 跳过注释和空行
        if [[ ! "$key" =~ ^[[:space:]]*# && -n "$key" ]]; then
            # 去除前后空格和引号
            key=$(echo "$key" | xargs)
            value=$(echo "$value" | xargs | tr -d '"' | tr -d "'")
            # 导出环境变量
            export "${key}=${value}"
        fi
    done < .env
fi

# 激活 conda 环境（无论是否使用 groq）
echo "正在激活 Whisper 环境..."
conda activate Whisper

# 确保所需包已安装
echo "检查必要的 Python 包..."
$CONDA_PREFIX/bin/pip install -q rumps python-dotenv

# 在后台运行程序，并将输出重定向到日志文件
echo "正在运行 statusbar.py..."
LOG_FILE="$(dirname "$0")/whisper.log"
nohup $CONDA_PREFIX/bin/python statusbar.py > "$LOG_FILE" 2>&1 &

# 等待一会确保程序启动
sleep 1

# 显示最近的日志
echo "最近的日志输出:"
tail -n 5 "$LOG_FILE"

# 退出终端
exit