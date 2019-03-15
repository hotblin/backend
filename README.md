```bash
pip freeze > package.txt
pip install -r package.txt
sqlacodegen mysql+cymysql://root:123456@127.0.0.1:3306/mall > models/models_tmp.py
```