import requests
import yaml
import bs4
from datetime import datetime

user_id = ""
success_status = 4


def get_user_id():
    global user_id

    if user_id:
        return user_id

    with open("config.yaml") as file:
        config = yaml.load(file, Loader=yaml.BaseLoader)
        user_id = config["user_id"]
        return user_id


def get_formatted_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")


def get_timestamp(soup: bs4.BeautifulSoup):
    try:
        return soup.select_one(
            "#status-table > tbody > tr:nth-child(1) > td:last-child > a"
        ).attrs["data-timestamp"]
    except:
        print("해당 사용자 존재하지 않음")
        exit(1)


def main():
    user_id = get_user_id()
    status_page_url = (
        f"https://www.acmicpc.net/status?user_id={user_id}&result_id={success_status}"
    )

    raw = requests.get(status_page_url)
    soup = bs4.BeautifulSoup(raw.text, "html.parser")
    last_problem_solved_time = get_timestamp(soup)

    last_problem_solved_date = get_formatted_timestamp(int(last_problem_solved_time))
    today = get_formatted_timestamp(int(datetime.now().timestamp()))

    if last_problem_solved_date == today:
        print("오늘 문제 풀기 완료")
        exit(0)
    else:
        print("오늘 문제 아직 안 풀었음")
        exit(1)


if __name__ == "__main__":
    main()
