
### Story 1: Send a Notification (slack)

#### Objectives:
- Understand python repository structure. Just as Code Style, API Design, and Automation are essential for a healthy 
  development cycle. Repository structure is a crucial part of your project’s architecture.
- Send a notification in slack.
- Start with a feedback loop.

#### Steps:
- Fork this repository into your account on github.com, then clone the same. (Alternatively, clone this repository and push to a new repository on your own github.com account)
- Join `#python_workshop_tio_tmp` channel on `tioengineering` workspace.
- Create following directory structure at root `mkdir -p ./scripts/aws-console-changes/`
```
setup.py (visit later)
aws-console-changes/__init__.py
aws-console-changes/notification.py
tests/test_notification.py
```
- Copy below code into the `aws_console_changes/notification.py`
```python
import argparse
import json
from http import HTTPStatus

import requests

python_workshop_webhook_url = 'shh!! Its a SECRET. Supplied during workshop.'  # python_workshop channel in TIOEngineering workspace.
message = "Super! {username}, you have successfully completed kata `{kata}` in your journey of learning python best " \
          "practices. "


def send_notification(username):
    slack_data = {'text': message.format(username=username, kata=get_kata_number())}
    response = requests.post(
        python_workshop_webhook_url, data=json.dumps(slack_data), headers={"Content-Type": "application/json"}
    )
    if response.status_code != HTTPStatus.OK:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )


def get_kata_number():
    parser = argparse.ArgumentParser()
    parser.add_argument('--kata', type=int)
    args = parser.parse_args()
    if args.kata is None:
        return 0
    return args.kata


if __name__ == "__main__":
    username = "-- YOUR USERNAME --"
    send_notification(username)
```
- Ensure updating SLACK Webhook and your name placeholders in the code.
- Open a terminal (preferably `bash`, `zsh` etc) and change directory to `/aws_console_changes`
- Ensure you have `python3.8`
- Execute
```shell
python3 notification.py --kata=1
```
--- or ---
```shell
python notification.py --kata=1 # (if using pyenv)
```
- If you get below `ERROR`, install `requests` module using `pip install requests` 
and execute again.
```
Traceback (most recent call last):
  File "notification.py", line 3, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
```
- If you get error `NoSchemaSupplied`, you must have forgotten updating slack webhook.
- You should have a notification in slack now.
- Commit the code to version control.
- onwards to [kata-2](../kata-2/HOW-TO.md)