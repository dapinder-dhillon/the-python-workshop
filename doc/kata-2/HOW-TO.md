
###Story 1: Explicitly declare and isolate dependencies

#### Objectives:
- Explicitly declare and isolate dependencies. 

#### Steps:
- Fork this repository into your account on github.com, then clone the same. (Alternatively, clone this repository and push to a new repository on your own github.com account)
- Join `#python_workshop` channel on tioengineering workspace.
- Create following directory structure at root `mkdir -p ./scripts/aws-console-changes/`
```
setup.py (visit later)
aws-console-changes/__init__.py
aws-console-changes/notification.py
tests/test_notification.py
```
- Copy below code into the `aws_console_changes/notification.py`
```python
import json

import requests

python_workshop_webhook_url = 'shh!! Its a SECRET. Supplied during workshop.'  # python_workshop channel in TIOEngineering workspace. #CHECK
message = "Super! {username} is learning python best practices together :python:"


def send_notification(username):
    slack_data = {'text': message.format(username=username)}
    response = requests.post(
        python_workshop_webhook_url, data=json.dumps(slack_data), headers={"Content-Type": "application/json"}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )


if __name__ == "__main__":
    username = "-- YOUR USERNAME --" #CHECK
    send_notification(username)
```
- Ensure updating SLACK Webhook and your name placeholders in the code.
- Open a terminal (preferably `bash`, `zsh` etc) and change directory to `/aws_console_changes`
- Ensure you have `python3.8`
- Execute
```
python3 notification.py
   --- or ---
python notification.py (if using pyenv)
```
- If you get below ERROR, install `requests` module using `pip install requests` 
and execute again. Great if you dont.
```
Traceback (most recent call last):
  File "notification.py", line 3, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
```
- If you get error `NoSchemaSupplied`, you must have forgot updating slack webhook.
- You should have a notification in slack now.
- Commit the code to version control.
- onwards to [kata-2](../kata-2/HOW-TO.md)