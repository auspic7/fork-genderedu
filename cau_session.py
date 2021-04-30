import requests
from bs4 import BeautifulSoup


def get_login_session(username, password):
    cookies = {
        'UAKEY': '77d4ac7158ff4a95b22837a186a0143e',
        'cau.ac.kr': 'T',
        'AUTHCHK': 'F',
        'NCAUPOLICYNUM': '243',
    }
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '^\\^',
        'sec-ch-ua-mobile': '?0',
        'Origin': 'https://genderedu.cau.ac.kr',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://genderedu.cau.ac.kr/',
        'Accept-Language': 'ko',
    }
    data = {
      'act': '',
      'credType': 'BASIC',
      'retURL': 'https^%^3A^%^2F^%^2Fgenderedu.cau.ac.kr^%^3A443^%^2Findex.php^%^3Fmid^%^3Dm03',
      'userID': username,
      'password': password,
      'x': '56',
      'y': '27'
    }

    s = requests.Session()
    res = s.post('https://sso2.cau.ac.kr/SSO/AuthWeb/Logon.aspx?ssosite=genderedu.cau.ac.kr', headers=headers, cookies=cookies, data=data)
    soup = BeautifulSoup(res.text, 'html.parser')
    form = soup.find(id="frmData")
    data = {}
    for input in form.children:
        data[input['name']] = input['value']
    print(data)

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'Origin': 'https://sso2.cau.ac.kr',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://sso2.cau.ac.kr/SSO/AuthWeb/Logon.aspx?ssosite=genderedu.cau.ac.kr',
        'Accept-Language': 'ko',
    }
    s.post('https://sso2.cau.ac.kr/SSO/AuthWeb/LogonDomain.aspx', headers=headers, data=data)

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'Origin': 'https://sso2.cau.ac.kr',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://sso2.cau.ac.kr/SSO/AuthWeb/LogonDomain.aspx',
        'Accept-Language': 'ko',
    }
    data = {
        'retURL': 'https://genderedu.cau.ac.kr:443/index.php?mid=m03',
        'ssosite': 'genderedu.cau.ac.kr',
        'AUTHERR': '0',
        'mode': 'clear',
        'NADomainDns': 'cau.ac.kr',
        'NADomainIp': '',
        'dupinfo': '',
        'domainCred': '',
        'NCAUPOLICYNUM': '244',
        'ipLogonUrl': '',
        'ipNACookieManageUrl': '',
        'systemID': ''
    }
    s.post('https://sso2.cau.ac.kr/SSO/AuthWeb/NACookieManage.aspx', headers=headers, cookies=cookies, data=data)

    return s


if __name__ == '__main__':
    pass