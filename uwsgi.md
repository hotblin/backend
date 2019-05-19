# uwsgi

## 准备工作

- 提前创建 `logs`目录
- 提前创建 `uwsgi` 目录

uwsgi 配置文件需要打印logs运行uwsgi需要导出pid文件，所以需要新建文件夹

## 命令

```bash
# 启动
uwsgi --ini ./uwsgi.ini
# 查看uwsgi运行状态
ps -ef | grep uwsgi

# 停止uwsgi应用
pkill -f uwsgi -9

# 程序pid文件可以帮助我们重启或者停止
# pid 文件中存放的是该项目uwsgi程序的主id
uwsgi --reload uwsgi/uwsgi.pid # 通过pid重启
uwsgi --connect-and-read uwsgi/uwsgi.status # 读取uwsgi实时状态
uwsgi --stop uwsgi/uwsgi.pid　# 停止uwsgi任务
```

## 配置详解

```ini
[uwsgi]
master = true
socket = 127.0.0.1:5051 ; 需要和.conf中uwsgi_pass配置一样
chdir = /home/snowman/桌面/flask-wechat # 项目目录
processes = 4 ; 开启的进程数量
wsgi-file = manage.py  # python 启动程序文件
# python 程序内用以启动的应用的变量名
callable = app 
threads = 2　# 线程数量
daemonize # 使进程在后台运行，并将日志打到指定的日志文件或者udp服务器（daemonize uWSGI）。实际上最常用的，还是把运行记录输出到一个本地文件上。
```