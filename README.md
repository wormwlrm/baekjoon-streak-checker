# baekjoon-streak-checker

🏃‍♀️ 백준과 solved.ac 스트릭을 깨트리지 않게 체크해주는 Github Action

## How to use

1. 이 저장소를 fork합니다.

1. `config.yml` 파일에 `user_id` 를 추적할 백준 아이디로 설정합니다.

    ```yaml
    user_id: howlism
    ```

1. [알림 설정](https://github.com/settings/notifications) 페이지에서 Github Action 알람을 활성화합니다.

   ![알람](setting.png)

1. Github Action 크론잡에 따라 매일 오후 11시 50분에 실행됩니다. 문제를 풀지 않은 경우 메일이 발송됩니다.

## License

MIT
