from requests import get
from base64 import b64decode

def validate(key):
    dictobj = get(f'https://api.github.com/repos/Cmd858/DistMgr/contents/mgr')
    b64list = eval(dictobj.text)['content'].split('\n')
    for item in b64list:
        teststr = b64decode(item).decode('utf8').strip()
        if teststr is not '' and key in teststr:
            if teststr[-1] == '1':
                return True
            else:
                return False
    return False
