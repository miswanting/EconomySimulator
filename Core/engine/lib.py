import secrets


def random_hash(level=4):
    """
    # 随机哈希值生成器
    返回随机生成的哈希字符串
    - level == n，返回长度为2n的字符串，在16^n个项目中随机，任意两个值相同的概率为1/16^n/2。
    """
    return secrets.token_hex(level).upper()


def fix_path():
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.join(os.path.dirname(__file__), '../..')
    os.chdir(datadir)
