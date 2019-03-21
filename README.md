# Flask

## Flask

## views

- 使用url_for 来重定向

## 常用插件

## url 参数

```python
from flask import app
@app.route("/api/<int:id>/<string:name>")
def get_name():
    pass
```

## 会话技术

- 长连接
- 短连接


## pip 命令

```bash
pip freeze > package.txt
pip install -r package.txt

# 根据已存在sql反向生成表对象 
sqlacodegen mysql+cymysql://root:123456@127.0.0.1:3306/mall > models/models_tmp.py
```

sqlalchemy  对应关系型数据库
MongoEngine 对应非关系型数据库


## 参数获取

- get

```python
from flask import request
username = request.args.get('username')
```

- form-data 

```python
from flask import request
username = request.form.get('username')

```

- json类型

```python

from flask import  request
args = request.get_json()
args = request.json
```