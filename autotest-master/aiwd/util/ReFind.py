import re

def reFind(pattern, string):
    p = re.compile(pattern)
    items = re.findall(p, string)
    return items


if __name__ == '__main__':
    a = "{'code': 1, 'errorMessage': 'OK', 'data': {'totalNumber': 18, 'list': [{'id': 168, 'name': '最新市场情况', 'isHot': 1, 'isKeyword': 1, 'isExample': 1, 'createUser': 'string', 'updateUser': 'chenguan', 'createTime': 1577971232946, 'updateTime': 1578314987028, 'categ\
    ory': 'index', 'applicationCodes': ['com.rjhy.uranus']}, {'id': 167, 'name': 'A股市场涨跌分布', 'isHot': 1, 'isKeyword': 0, 'isExample': 1, 'createUser': 'string', 'updateUser': 'chenguan', 'createTime': 1577971225355, 'updateTime': 1578314420386, 'category': 'inde\
    x', 'applicationCodes': ['com.rjhy.uranus']}, {'id': 166, 'name': '大盘风向', 'isHot': 1, 'isKeyword': 1, 'isExample': 1, 'createUser': 'string', 'updateUser': 'chenguan', 'createTime': 1577971213649, 'updateTime': 1578313810941, 'category': 'index', 'applicationCo\
    des': ['com.rjhy.uranus']}, {'id': 164, 'name': '通信设备最新表现', 'isHot': 1, 'isKeyword': 0, 'isExample': 0, 'createUser': 'string', 'updateUser': 'string', 'createTime': 1577971117668, 'updateTime': 1577971117668, 'category': 'plate', 'applicationCodes': ['com.\
    rjhy.uranus']}, {'id': 148, 'name': '阿里巴巴涨跌幅', 'isHot': 1, 'isKeyword': 0, 'isExample': 1, 'createUser': 'string', 'updateUser': 'chenguan', 'createTime': 1577947574181, 'updateTime': 1577947590350, 'category': 'plate', 'applicationCodes': ['com.rjhy.uranus'\
    ]}, {'id': 137, 'name': '保险行业怎么样', 'isHot': 1, 'isKeyword': 0, 'isExample': 0, 'createUser': 'string', 'updateUser': 'string', 'createTime': 1577947115615, 'updateTime': 1577947115615, 'category': 'plate', 'applicationCodes': ['com.rjhy.uranus']}, {'id': 136\
    , 'name': '银行板块涨跌表现', 'isHot': 1, 'isKeyword': 0, 'isExample': 0, 'createUser': 'string', 'updateUser': 'string', 'createTime': 1577947096981, 'updateTime': 1577947096981, 'category': 'plate', 'applicationCodes': ['com.rjhy.uranus']}, {'id': 135, 'name': '\
    最新大盘表现', 'isHot': 1, 'isKeyword': 0, 'isExample': 0, 'createUser': 'string', 'updateUser': 'string', 'createTime': 1577947043916, 'updateTime': 1577947043916, 'category': 'index', 'applicationCodes': ['com.rjhy.uranus']}, {'id': 134, 'name': '格力电器舆情', '\
    isHot': 1, 'isKeyword': 0, 'isExample': 0, 'createUser': 'string', 'updateUser': 'string', 'createTime': 1577946994171, 'updateTime': 1577946994171, 'category': 'stock', 'applicationCodes': ['com.rjhy.uranus']}, {'id': 133, 'name': '万科A风险扫描', 'isHot': 1, 'isK\
    eyword': 0, 'isExample': 0, 'createUser': 'string', 'updateUser': 'string', 'createTime': 1577946984406, 'updateTime': 1577946984406, 'category': 'stock', 'applicationCodes': ['com.rjhy.uranus']}, {'id': 132, 'name': '中兴通讯风险舆情', 'isHot': 1, 'isKeyword': 0,\
    'isExample': 0, 'createUser': 'string', 'updateUser': 'string', 'createTime': 1577946971301, 'updateTime': 1577946971301, 'category': 'stock', 'applicationCodes': ['com.rjhy.uranus']}, {'id': 131, 'name': '最新表现', 'isHot': 1, 'isKeyword': 0, 'isExample': 0, 'cre\
    ateUser': 'string', 'updateUser': 'string', 'createTime': 1577946571605, 'updateTime': 1577946761824, 'category': 'stock', 'applicationCodes': ['com.rjhy.uranus']}, {'id': 130, 'name': '贵州茅台怎么样', 'isHot': 1, 'isKeyword': 0, 'isExample': 0, 'createUser': 'str\
    ing', 'updateUser': 'string', 'createTime': 1577946519831, 'updateTime': 1577946782169, 'category': 'stock', 'applicationCodes': ['com.rjhy.uranus']}, {'id': 95, 'name': '中信证券', 'isHot': 1, 'isKeyword': 0, 'isExample': 0, 'createUser': None, 'updateUser': None,\
     'createTime': 1577787440666, 'updateTime': 1577946793566, 'category': 'stock', 'applicationCodes': ['com.rjhy.uranus']}]}}"
    b = "'isHot': 1"
    result = reFind(b, a)
    print(result)
    print(type(result))