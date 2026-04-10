import json
import mitmproxy.http
from mitmproxy import ctx

# 存储发现的关联参数
correlation_params = {}

def response(flow: mitmproxy.http.HTTPFlow) -> None:
    if "application/json" in flow.response.headers.get("content-type", ""):
        print(11111111)
        print('这是打印的URL:' + flow.request.url)
        print(type(flow.response.text))
        print(json.loads(flow.response.text))
