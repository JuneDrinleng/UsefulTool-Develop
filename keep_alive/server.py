from http.server import BaseHTTPRequestHandler, HTTPServer
from LogUtils import get_log_path, log


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            try:
                with open(get_log_path(), "r", encoding="utf-8") as f:
                    log_content = f.read()
            except Exception as e:
                log_content = f"无法读取日志文件: {e}"

            html = f"""
            <html><head><meta charset="utf-8"><title>实时热搜记录</title></head>
            <body>
            <h1>📟 实时热搜记录</h1>
            <pre>{log_content}</pre>
            </body></html>
            """
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_error(404, "页面未找到")

def run_http_server():
    server = HTTPServer(('localhost', 8080), SimpleHandler)
    log("本地 HTTP 服务已启动：http://localhost:8080")
    server.serve_forever()
