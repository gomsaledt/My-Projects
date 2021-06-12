from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

compiler = Tk()
compiler.title("MI ZEN")


file_path = ""
count = 0

def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes = [("Python Files", "*.py")])
    with open(path, "r") as file:
        code = file.read()
        
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)
        compiler.title("MI ZEN [" + path.split("/")[-1] + "]")

def save_as():
    if file_path == "":
        path = asksaveasfilename(filetypes = [("Python Files", "*.py")])
    else:
        path = file_path
        
    with open(path, "w") as file:
        code = editor.get("1.0", END)
        file.write(code)
        set_file_path(path)
        compiler.title("MI ZEN [" + path.split("/")[-1] + "]")

def run():
    if file_path == "":
        save_prompt = Toplevel()
        text = Label(save_prompt, text = "Please save your code")
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    global count
    count += 1
    if error:
        code_output.insert(END, "\n--------------------------------------------------------------------------------\n[" + str(count) + "]")
        code_output.insert(END, output)
        code_output.insert(END, "\n[-]")
        code_output.insert(END, error)
    else:
        code_output.insert(END, "\n--------------------------------------------------------------------------------\n[" + str(count) + "]")
        code_output.insert(END, output)

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_as)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_command(label="Exit", command=exit)
menu_bar.add_cascade(label="File", menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=run)
menu_bar.add_cascade(label="Run", menu=run_bar)

compiler.config(menu=menu_bar)

editor_label = Label(compiler, text = "Code")
editor_label.pack()
editor = Text()
editor.pack()

output_label = Label(compiler, text = "Output")
output_label.pack()
code_output = Text(height=10)
code_output.pack()

compiler.mainloop()
