
from app import create_app

# flask实例化核心对象
app = create_app()
if __name__ == '__main__':
    # 开启flask的debug模式，当程序发生改动时候，flask框架会监听改动并自动重启服务器
    # 开启debug模式后也可以把详细的错误信息显示在网页当中
    print("qpp启动{0}".format(id(app)))
    app.run("0.0.0.0", port=8888, debug=app.config['DEBUG'])
