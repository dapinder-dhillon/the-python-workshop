
## Story 4: Refactor Notification Module to Object-Oriented

### Objectives: (**20 mins**)
- Write Object-Oriented Code (following SRP Single Responsibility Principle)

### Steps:
- Convert `notification.py` to a class.
- Prefix `https://` to `PYTHON_WORKSHOP_WEBHOOK_URL's` constant's value to favor testing. (_will see later_)
- :point_right: Try to give each class or method **_Single Responsibility_**.
  - Classes (or python modules _aka files_) should follow Single Responsibility, and they should have only ONE reason to change.
  This allows classes/modules to get change only when requirement for that class is modified. If you put multiple 
  responsibilities say notification, read_s3, etc in same class, change to `read_s3` will impact and whole needs to be tested again. 
  - Following Single Responsibility in methods allows them to be small, clean, maintainable, readable and testable. 
  You dont need to provide documentation for a method following SRP.
- `send_notification` method current is owning two responsibilities:
  1) creating/formatting slack message
  2) sending slack notification
- Let's separate the responsibilities, this will **even help us later during testing**.
```python
import argparse
import json
from http import HTTPStatus

import requests


class Notification:
    PYTHON_WORKSHOP_WEBHOOK_URL = 'https://shh!! Its a SECRET. Supplied during workshop.'  # python_workshop channel in TIOEngineering workspace.
    MESSAGE = "Super! {username}, you have successfully completed kata `{kata}` in your journey of learning python " \
              "best practices."

    def send_notification(self, user_name: str) -> int:
        slack_data = self.get_slack_message(user_name=user_name)
        response = requests.post(
            Notification.PYTHON_WORKSHOP_WEBHOOK_URL, data=json.dumps(slack_data),
            headers={"Content-Type": "application/json"}
        )
        if response.status_code != HTTPStatus.OK:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
            )
        return response.status_code

    def get_slack_message(self, user_name: str) -> dict:
        slack_data = { 'text': Notification.MESSAGE.format(username=user_name.strip(), kata=self.get_kata_number())}
        return slack_data

    def get_kata_number(self) -> int:
        parser = argparse.ArgumentParser()
        parser.add_argument('--kata', type=int)
        args = parser.parse_args()
        if args.kata is None:
            return 0
        return args.kata


if __name__ == "__main__":
    notification = Notification()
    username = "Dapinder"
    notification.send_notification(user_name=username)
```
- Execute `notification.py`
```shell
pipenv run python python/logs_processor/notification.py --kata=4
```
- You should have a notification in slack now _"Super! Dapinder, you have successfully completed kata 4 in your journey"_. 
- onwards to [kata-5](../kata-5/HOW-TO.md)

#### Achieved objective? :question: Learnings? :thinking:
- Write Object-Oriented Code :white_check_mark: