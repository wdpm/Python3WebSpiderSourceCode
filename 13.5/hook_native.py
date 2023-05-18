import frida
import sys

CODE = open('hook_native.js', encoding='utf-8').read()
PROCESS_NAME = 'com.germey.appbasic2'


def on_message(message, data):
    print(message)


process = frida.get_usb_device().attach(PROCESS_NAME)
script = process.create_script(CODE)
script.on('message', on_message)
script.load()
sys.stdin.read()
