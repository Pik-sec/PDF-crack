import PySimpleGUI as sg
import webbrowser
import threading
import pikepdf


# pdf解密
def unlock_file(file):
	pdf = pikepdf.open(file, allow_overwriting_input=True)
	fs = file.rsplit(".",1)
	op_file = fs[0]+"_removepwd."+fs[1]
	pdf.save(op_file)
	print('ヾ(≧▽≦*)o 恭喜，移除成功!')
	print(f"解密的文件保存在了{op_file}哦")

button_click_count = 0

# 设置主题
sg.theme('PDF-crack')

def openBrowser():
    webbrowser.open("https://github.com/Pik-sec")

frameLayout = [[sg.Text("BY:Pik", click_submits=True, key="hello", text_color="red"), sg.Text("版本：0.1.0"), sg.Text("更新日期：2022-10-24")],
               [sg.Text("移除PDF限制密码")],
               [sg.Text("输出文件和源文件同路径，名称带_removepwd")]]

tab1_layout = [
        [sg.Text("路径:"), sg.InputText("请选择解密文件", key="file", size=(45, 1)),sg.FileBrowse("浏览", target="file"),sg.Button("开始", key="start")],
        [sg.Output(size=(70,10))]]

tab2_layout = [[sg.Frame(layout=frameLayout, title="说明", size=(590, 300))]]

win_layout = [
    [sg.TabGroup(
        [
            [sg.Tab('密码移除', tab1_layout, key='tools', tooltip=''),
             sg.Tab('功能说明', tab2_layout, key='instruduction', tooltip=''),
             ]
        ],
        key='tabgroup'
    )]
]

# 设置窗口
window = sg.Window('文档密码移除', win_layout, font=("Console", 15),default_element_size=(60, 1), size=(680, 310))

# 输入检查
def input_check(values):
    if("pdf" not in values["file"]):
        print("请输入正确的文件路径！！")
		# sg.popup('请输入正确的文件路径！！')
        window["file"].update("")
        return True
    return False

# 主窗口进程
while True:
    event, values = window.read()

    # 关闭窗口
    if event == sg.WIN_CLOSED:
        break
    
    # 开始处理
    if(event == 'start'):
        s = input_check(values)
        if(s):
            continue
        if(button_click_count!=0 ):
            print("请勿重复点击开始按钮")
            continue
        else:
            button_click_count = 1
            # 线程1处理底盘
            t1 = threading.Thread(target=unlock_file, args=(values["file"],), name="unlock", daemon=True)
            t1.start()
            print("正在移除密码...")

    # 点击关于作者
    if(event == "hello"):
        openBrowser()
    
window.close()
