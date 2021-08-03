
Story 1: Send a Notification (slack)

Objectives:
- Understand python repository structure. Just as Code Style, API Design, and Automation are essential for a healthy 
  development cycle. Repository structure is a crucial part of your project’s architecture.
- Explicitly declare and isolate dependencies. 

Steps:
- Fork this repository into your account on github.com, then clone the same. (Alternatively, clone this repository and push to a new repository on your own github.com account)
- Create a new directory structure at root `scripts/aws-console-changes/`
- Copy below code into the [notification.py](./aws_console_changes/notification.py)
- Ensure updating SLACK Webhook and your name placeholders in the code.
- Open a terminal (preferably `bash`, `zsh` etc) and change directory to [aws_console_changes](./aws_console_changes)
- Ensure you have python3.8
- Execute the code `python3 notification.py` or `python notification.py` (_if using pyenv_) 

```
import json

import requests

python_workshop_webhook_url = 'shh!! Its a SECRET. Supplied during workshop.'  # python_workshop channel in TIOEngineering workspace.
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
    username = "-- YOUR USERNAME --"
    send_notification(username)
```


- Verify that the web server is running at the published IP address (available as a stack output)

```    
# Print the only output value from the stack
$ aws cloudformation describe-stacks \
    --query "Stacks[0].Outputs[0].OutputValue" \
    --output text \
    --stack-name ${DEV_STACK_NAME}   

# (OPTIONAL) You may now delete the stack
$ aws cloudformation delete-stack \
    --stack-name ${DEV_STACK_NAME}   

```

- Commit the template to version control.

```
$ git checkout -b develop
$ git add templates/template.yaml
$ git commit -m "story-1 (work-in-progress)"
$ git push foo develop # If you have configured a remote (say, `foo`) that points to your own repository

```

- onwards to [kata-2](../kata-2/HOW-TO.md)