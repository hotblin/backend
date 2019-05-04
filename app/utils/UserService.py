import hashlib, base64


# 密码加密方式
class UserService():
    @staticmethod
    def generatedPassWord(pwd, salt):
        m = hashlib.md5()
        new_str = "%s^%s" % (base64.encodebytes(pwd), salt)
        m.update(new_str.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def decreasePassWord(pwd, salt):
        pass
