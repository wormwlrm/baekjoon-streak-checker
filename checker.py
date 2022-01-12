import requests
import yaml
import bs4
import sys
from datetime import datetime

user_id = ""
success_status = 4


def get_user_id():
    global user_id

    if user_id:
        return user_id

    with open("config.yml") as file:
        config = yaml.load(file, Loader=yaml.BaseLoader)
        user_id = config["user_id"]
        return user_id


def get_formatted_timestamp(timestamp, am6=False):
    if am6:
        form = "%Y-%m-%d 06:00:00"
    else:
        form = "%Y-%m-%d %H:%M:%S"

    return datetime.fromtimestamp(timestamp).strftime(form)


def get_timestamp(soup: bs4.BeautifulSoup):
    try:
        return soup.select_one(
            "#status-table > tbody > tr:nth-child(1) > td:last-child > a"
        ).attrs["data-timestamp"]
    except:
        sys.exit("[ERROR]: 사용자가 존재하지 않음")


def main():
    user_id = get_user_id()
    status_page_url = (
        f"https://www.acmicpc.net/status?user_id={user_id}&result_id={success_status}"
    )

    raw = requests.get(status_page_url)
    soup = bs4.BeautifulSoup(raw.text, "html.parser")
    last_problem_solved_timestamp = get_timestamp(soup)

    # YYYY-MM-DD hh:mm:ss
    last_problem_solved_time = get_formatted_timestamp(
        int(last_problem_solved_timestamp)
    )
    today = get_formatted_timestamp(int(datetime.now().timestamp()), am6=True)

    if today <= last_problem_solved_time:
        print("오늘 문제 풀기 완료")
        sys.exit(0)
    else:
        print("오늘 문제 아직 안 풀었음")
        sys.exit("[ERROR]: 오늘 문제를 풀지 않음")


if __name__ == "__main__":
    main()
