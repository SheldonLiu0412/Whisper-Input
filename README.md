# Whisper Input

Whisper Input 是受到即友[FeiTTT](https://web.okjike.com/u/DB98BE7A-9DBB-4730-B6B9-2DC883B986B1)启发做的一个简单的 python 代码。可以实现按下 Option 按钮开始录制，抬起按钮就结束录制，并调用 Groq Whisper Large V3 Turbo 模型进行转译，由于 Groq 的速度非常快，所以大部分的语音输入都可以在 1-2s 内反馈。并且得益于 whisper 的强大能力，转译效果非常不错。

## 功能

| 功能           | 快捷键                          |
| -------------- | ------------------------------- |
| 多语言语音转译 | Option 或者 Alt                 |
| 中文翻译为英文 | Shift + Option 或者 Shift + Alt |



查看[视频效果演示](https://img.erlich.fun/personal-blog/uPic/WhisperInputV02_compressed.mp4)



**重点：Groq 只要注册，就提供一定的免费用量，并且在我们这个使用场景下免费已经完全够用了！**

**🧐 当然，如果你在国内使用，并且无法访问 Groq 或者无法获得 Groq API，也欢迎反馈。因为我过去还做了一个 Groq 的 Whisper 代理池，理论上可以免费提供相对比较大的并发以及日常使用。但这需要你来单独申请，我会根据大家的需求考虑在后续的代码更新里添加对应的支持**

## 使用方法

1. 注册 Groq 账户：https://console.groq.com/login
2. 复制 Groq 免费的 API KEY：https://console.groq.com/keys
3. 打开 `终端` ，进入到想要下载项目的文件夹
    ```bash
    git clone git@github.com:ErlichLiu/Whisper-Input.git
    ```
4. 创建虚拟环境 【推荐】
    ```bash
    python -m venv venv
    ```
    或者
    ```bash
    conda create -n Whisper python=3.11
    ```

5. 重命名 `.env` 文件
    ```bash
    cp .env.example .env
    ```

6. 粘贴在第 2 步复制的 API KEY 到 `.env`  文件，效果类似
    ```bash
    GROQ_API_KEY=gsk_z8q3rXrQM3o******************8dQEJCYz3QTJQYZ
    ```

7. 在最好不需要关闭的 `终端` 内进入到对应文件夹，然后激活虚拟环境
    ```bash
    # macOS / Linux
    source venv/bin/activate
    或者
    conda activate Whisper
    
    # Windows
    .\venv\Scripts\activate
    或者
    conda activate Whisper
    ```

8. 安装依赖
    ```bash
    pip install -r requirements.txt
    ```

9. 运行程序
    ```bash
    python main.py
    ```
    或者修改 `start.command` 文件，将 `source ~/.zshrc` 改为 `source ~/.bash_profile`（根据个人终端情况选择）
    然后双击 `start.command` 文件即可运行在后台并在系统状态栏显示

10. （可选）创建独立应用程序
    1. 打开 Automator（在应用程序文件夹中或使用 Spotlight 搜索）
    2. 选择"新建文稿"，然后选择"应用程序"
    3. 在左侧搜索栏中搜索"运行 Shell 脚本"，将其拖到右侧工作区
    4. 在脚本框中输入以下内容（请根据实际路径修改）：
        ```bash
        SCRIPT_PATH="你的本地路径/start.command"
        "$SCRIPT_PATH"
        ```
    5. 点击"文件" -> "存储"，将应用程序命名为"Whisper Input.app"
    6. 自定义应用图标（可选）：
        - 右键点击"Whisper Input.app"
        - 选择"显示简介"
        - 点击左上角的图标
        - 拖入你想要的图标文件（.icns 格式）或图片




**🎉  此时你就可以按下 Option 按钮开始语音识别录入啦！**



![image-20250111140954085](https://img.erlich.fun/personal-blog/uPic/image-20250111140954085.png)





关注作者个人网站，了解更多项目: https://erlich.fun





## 未来计划

[✅] 多语言转译功能

[✅] 中文或多语言转译为英文

[  ] 标点符号支持

[  ] 添加 Agents，或许可以实现一些屏幕截图，根据上下文做一些输入输出之类的



**如果你也有想法：** 欢迎 Fork 和 PR，如果你在使用当中遇到问题，欢迎提交 Issue。

## 更新日志

#### 2025.01.11

> 1. 支持快捷键按下后的状态显示【正在录音、正在转译/翻译、完成】
> 2. 支持多语言语音转换为英文输出

#### 2025.01.10

> 1. 支持基本的快捷键语音转文字输入

## 协议

遵循 MIT 协议