import tkinter as tk
import time

# 创建主窗口
root = tk.Tk()
root.title("秒表")
root.geometry("300x200")

# ---------- 数据变量 ----------
running = False      # 是否运行中
start_time = 0       # 当前计时起点的时间戳
elapsed = 0          # 已累计秒数（暂停时存储）

# ---------- 辅助函数 ----------
def format_time(seconds):
    """将秒数格式化为 分:秒.十分之一秒"""
    minutes = int(seconds // 60)
    secs = seconds % 60
    return f"{minutes}:{secs:05.1f}"

# ---------- 核心切换函数 ----------
def toggle_timer():
    """切换开始/暂停状态"""
    global running, start_time, elapsed
    if running:   # 如果正在运行 → 暂停
        running = False
        elapsed = time.time() - start_time   # 记录累计秒数
        btn_start.config(text="继续")
        status_label.config(text="⏸ 已暂停", fg="orange")
    else:         # 如果暂停 → 开始/继续
        running = True
        start_time = time.time() - elapsed   # 调整起点
        btn_start.config(text="暂停")
        status_label.config(text="⏳ 计时中...", fg="green")

def reset_timer():
    """重置计时器归零"""
    global running, elapsed, start_time
    running = False
    elapsed = 0
    start_time = 0
    time_label.config(text="0:00.0")
    btn_start.config(text="开始")
    status_label.config(text="⟳ 已重置", fg="gray")

def update_display():
    """每0.1秒刷新时间显示"""
    if running:
        current = time.time() - start_time
        time_label.config(text=format_time(current))
    root.after(100, update_display)

# ---------- 界面组件 ----------
time_label = tk.Label(root, text="0:00.0", font=("Arial", 48))
time_label.pack(pady=20)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_start = tk.Button(btn_frame, text="开始", font=("Arial", 14),
                      width=8, command=toggle_timer)   # 绑定切换函数
btn_start.pack(side="left", padx=10)

btn_reset = tk.Button(btn_frame, text="重置", font=("Arial", 14),
                      width=8, command=reset_timer)
btn_reset.pack(side="left", padx=10)

status_label = tk.Label(root, text="就绪", font=("Arial", 12), fg="gray")
status_label.pack(pady=10)

# ---------- 启动循环 ----------
update_display()
root.mainloop()