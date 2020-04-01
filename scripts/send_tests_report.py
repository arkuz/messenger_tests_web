import os, sys
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def send_report_link():
    CI_JOB_ID = sys.argv[1]
    EXIT_CODE = int(sys.argv[2])
    status = 'SUCCESS'
    if EXIT_CODE != 0:
        status = 'FAILED'

    repo_name = 'messenger_tests_web'

    job = f'https://gitlab.com/messenger_team/{repo_name}/-/jobs/{CI_JOB_ID}'
    report = f'https://messenger_team.gitlab.io/-/{repo_name}/-/jobs/{CI_JOB_ID}/artifacts/report/report.html'
    msg = f'`GUI web tests` CI_JOB_ID={CI_JOB_ID} - *{status}* \n Перейти к джобе: {job} \n Смотреть отчет: {report}'
    key = 'JEkKqCP1IQLzkAn'

    requests.post('https://hostname/api/message', data={
        'key': key,
        'message': f'{msg}',
        'important': 'false',
        'nopreview': 'true'

    })

if __name__ == "__main__":
    send_report_link()