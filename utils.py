def show_status(code):
    if code == 200:
        return "请求成功"
    else:
        return f"请求失败，状态码：{code}"