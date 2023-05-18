import frida
import sys

CODE = open('hook_java.js', encoding='utf-8').read()
PROCESS_NAME = 'com.germey.appbasic1'


def on_message(message, data):
    print(message)

process = frida.get_usb_device().attach(PROCESS_NAME)
script = process.create_script(CODE)
#  监听JavaScript代码中任何通过se∩d方法发送的数据
script.on('message', on_message)
script.load()
sys.stdin.read()
