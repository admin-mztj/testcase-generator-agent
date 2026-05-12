import tkinter as tk
from tkinter import filedialog, messagebox
from agent import TestCaseAgent
from file_parser import parse_upload_file
from exporter import export_to_excel

class TestCaseAgentUI:
    def __init__(self, root):
        self.root = root
        self.root.title("自动化测试用例生成 Agent")
        self.root.geometry("680x550")

        self.label = tk.Label(root, text="上传需求文档（.txt / .md）")
        self.label.pack(pady=10)

        self.upload_btn = tk.Button(root, text="选择文件", command=self.upload_file, width=20)
        self.upload_btn.pack(pady=5)

        self.gen_btn = tk.Button(root, text="生成测试用例", command=self.generate, width=20)
        self.gen_btn.pack(pady=5)

        self.export_btn = tk.Button(root, text="导出Excel", command=self.export, state=tk.DISABLED, width=20)
        self.export_btn.pack(pady=5)

        self.text = tk.Text(root, height=22, width=80)
        self.text.pack(pady=10)

        self.file_content = ""
        self.cases = []

    def upload_file(self):
        path = filedialog.askopenfilename(filetypes=[("文本文档", "*.txt"), ("Markdown", "*.md")])
        if path:
            self.file_content = parse_upload_file(path)
            self.text.insert(tk.END, "✅ 文档加载成功，点击生成测试用例\n")

    def generate(self):
        if not self.file_content:
            messagebox.showwarning("提示", "请先上传文档")
            return
        agent = TestCaseAgent()
        self.cases = agent.generate(self.file_content)
        self.text.insert(tk.END, f"✅ 测试用例生成完成！共 {len(self.cases)} 条\n")
        self.export_btn.config(state=tk.NORMAL)

    def export(self):
        path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel文件", "*.xlsx")])
        if path:
            export_to_excel(self.cases, path)
            messagebox.showinfo("成功", "测试用例已导出为Excel！")