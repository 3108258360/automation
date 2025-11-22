import tkinter as tk
from tkinter import messagebox
import pyautogui
import json
import os

class ScreenshotAreaSelector:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("截图区域选择器")
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.area_data = {}
        
        # 创建界面元素
        self.create_widgets()
        
        # 加载已保存的区域数据
        self.load_areas()

    def create_widgets(self):
        # 创建选择按钮
        self.select_btn = tk.Button(self.root, text="选择区域", command=self.start_selection)
        self.select_btn.pack(pady=10)
        
        # 创建截图按钮
        self.capture_btn = tk.Button(self.root, text="截图", command=self.capture_area)
        self.capture_btn.pack(pady=10)

    def start_selection(self):
   #     创建全屏窗口用于选择区域
        self.selection_window = tk.Toplevel(self.root)
        self.selection_window.attributes('-fullscreen', True)
        self.selection_window.attributes('-alpha', 0.3)
        
        # 创建全屏Canvas
        self.canvas = tk.Canvas(self.selection_window, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # 绑定鼠标事件到Canvas
        self.canvas.bind('<Button-1>', self.on_mouse_down)
        self.canvas.bind('<B1-Motion>', self.on_mouse_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_mouse_up)

    def on_mouse_down(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_mouse_drag(self, event):
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, event.x, event.y,
            outline='#ff0000', width=2
        )

    def on_mouse_up(self, event):
        if self.start_x and self.start_y:
            self.end_x = event.x
            self.end_y = event.y
            self.area = {
                'left': min(self.start_x, self.end_x),
                'top': min(self.start_y, self.end_y),
                'width': abs(self.end_x - self.start_x),
                'height': abs(self.end_y - self.start_y)
            }
            # 自动保存区域数据到文件
            with open('screenshot_area.json', 'w') as f:
                json.dump(self.area, f)
        self.selection_window.destroy()

    def save_area(self):
        if hasattr(self, 'area'):
            # 保存区域数据到文件
            with open('screenshot_area.json', 'w') as f:
                json.dump(self.area, f)
            messagebox.showinfo("成功", "区域已保存！")
        else:
            messagebox.showwarning("警告", "请先选择一个区域！")

    def load_areas(self):
        if os.path.exists('screenshot_area.json'):
            with open('screenshot_area.json', 'r') as f:
                self.area = json.load(f)

    def capture_area(self):
        # 如果没有area属性，尝试重新加载保存的区域
        if not hasattr(self, 'area'):
            self.load_areas()
            if not hasattr(self, 'area'):
                messagebox.showwarning("警告", "请先选择一个区域！")
                return
        
        try:
            # 使用pyautogui截图
            screenshot = pyautogui.screenshot(region=(
                self.area['left'],
                self.area['top'],
                self.area['width'],
                self.area['height']
            ))
            # 保存截图
            screenshot.save('screenshot.png')
            messagebox.showinfo("成功", "截图已保存！")
        except Exception as e:
            messagebox.showerror("错误", f"截图失败：{str(e)}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ScreenshotAreaSelector()
    app.run()
