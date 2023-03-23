
from flask import Flask, request
import argparse
from wsgiref.simple_server import make_server


app = Flask(__name__)
previous_ip = None

def do_something(new_ip):
    print(f"IP地址已更改：从 {previous_ip} 变为 {new_ip}")

@app.route("/")
def index():
    global previous_ip
    current_ip = request.remote_addr

    if previous_ip is None:
        previous_ip = current_ip
        print("current_ip",current_ip)
    elif previous_ip != current_ip:
        do_something(current_ip)
        previous_ip = current_ip

    return "IP已记录"

def parse_arguments():
    parser = argparse.ArgumentParser(description="运行IP检查服务器")
    parser.add_argument("-p", "--port", type=int, default=8080, help="指定监听的端口 (默认: 8080)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    server = make_server('0.0.0.0', args.port, app)
    server.serve_forever()

