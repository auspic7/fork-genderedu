import argparse
import re
import time
from cau_session import get_login_session
from bs4 import BeautifulSoup


def get_play_buttons(session):
    response = session.get('https://genderedu.cau.ac.kr/index.php?mid=m03')
    main_page = BeautifulSoup(response.text, 'html.parser')

    play_buttons = main_page.find_all('a', class_="button icon play")
    return play_buttons


def get_first_available(play_buttons):
    for i, play_button in enumerate(play_buttons):
        if "alert" in play_button['onclick']:
            return play_buttons[i-1]
    return None


def pwn_video(session, url):
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'iframe',
        'Referer': 'https://genderedu.cau.ac.kr/',
        'Accept-Language': 'ko',
    }
    response = session.get('https://player.vimeo.com/video/525417090?player_id=video_525417090&app_id=122963', headers=headers)
    duration = re.findall(r'(?<="duration":)\d*', response.text)[0]
    response = session.get(url)
    video_page = BeautifulSoup(response.text, 'html.parser')

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'Accept': 'text/html, */*; q=0.01',
        'DNT': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://genderedu.cau.ac.kr',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://genderedu.cau.ac.kr/gen_edu.php?mid=m03&pact=course&uid=520&cid=igTzkv0RYWwHek77P%2BYaTgghUdTm%2FzxJRPydUuon3v0%3D',
        'Accept-Language': 'ko',
    }
    data = {
        'mid': '<?=$mid?>',
        'act': 'getTime',
        'a': video_page.find(id="vid")['value'],
        'ntime': str(int(time.time()))
    }
    session.post('https://genderedu.cau.ac.kr/include/gen_ajax.php', headers=headers, data=data)
    time.sleep(int(duration))
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'Accept': 'text/html, */*; q=0.01',
        'DNT': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://genderedu.cau.ac.kr',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://genderedu.cau.ac.kr/gen_edu.php?mid=m03&pact=course&uid=509&cid=M2hskvkDakAlVIaBT27icPHmoJvbkOVMJqevU0Y8xhc%3D',
        'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8',
    }

    data = {
        'mid': '<?=$mid?>',
        'act': 'getComplete',
        'a': video_page.find(id="vid")['value'],
        'b': duration,
        'ntime': str(int(time.time()))
    }
    response = session.post('https://genderedu.cau.ac.kr/include/gen_ajax.php', headers=headers, data=data)
    print(response.text)
    if 'Y' in response.text:
        print(video_page.find(id="vid")['value'], "Clear")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('username')
    parser.add_argument('password')
    args = parser.parse_args()

    session = get_login_session(args.username, args.password)
    buttons = get_play_buttons(session)
    while first_button := get_first_available(buttons):
        print(first_button['onclick'])
        url = "https://genderedu.cau.ac.kr" + re.findall(r"'[^']*'", first_button['onclick'])[1][1:-1]
        pwn_video(session, url)