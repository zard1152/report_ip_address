# report_ip_address


# IP Check Server
这个项目是一个简单的基于Flask的服务器，用于记录客户端的IP地址。当客户端请求服务器时，服务器会检查并记录客户端的IP地址。如果IP地址发生变化，服务器会调用`do_something`函数。

This project is a simple Flask-based server that logs the IP addresses of clients. When a client requests the server, the server checks and records the IP address of the client. If the IP address changes, the server calls the do_something function.

## 安装依赖

在运行此项目之前，请确保您已经安装了所有必需的依赖项。要安装依赖项，请运行以下命令：

```bash
pip install flask wsgiref
```

要运行服务器，请使用以下命令：
```
python ip_check_server_flask.py -p 8080
```

可将8080替换为您想要使用的端口。
可自定义 do_something 函数要进行什么操作

---

客户端, 复制 request_client.py 到电脑上运行,定时请求上报 ip

