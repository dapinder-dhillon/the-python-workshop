
## Story 5: Write tests for Notification

### Objectives: (**30 mins**)
- Write Tests 
- Debugging in IDE (PyCharm)

### Steps:
- We would be using python package [unittest](https://docs.python.org/3/library/unittest.html) and
  [requests-mock](https://pypi.org/project/requests-mock/) to write tests.
- [unittest](https://docs.python.org/3/library/unittest.html) is an **internal module** ([internal modules index](https://docs.python.org/3.8/py-modindex.html)) unlike 
  [requests-mock](https://pypi.org/project/requests-mock/) which need to be installed from [PyPi](https://pypi.org/).  
- We need `requests-mock` only as a development package as we do not want the requests-mock to be a part of deployment. 
```shell
pipenv install requests-mock --dev --python 3.8.10
```
- Above will update your `Pipfile` and `Pipfile.lock` to include `requests-mock` under `[dev-packages]`.
- Add below code in `/python/tests/test_notification.py` created as part of kata-3, Step 1.
```python
import json
import unittest
from http import HTTPStatus
from unittest.mock import MagicMock

import requests_mock

from python.logs_processor.notification import Notification


class TestNotification(unittest.TestCase):
    TEST_USERNAME = "WORKSHOP_USER"
    notification = None
    EXPECTED_SLACK_MESSAGE = json.loads(
        '{ "text": "Super! WORKSHOP_USER, you have successfully completed kata `5` in your journey of learning '
        'python best practices."}')

    def setUp(self) -> None:
        print("I am setup, You can use me to define instructions that will be executed before each test method.")
        # create Notification Object
        self.notification = Notification()
        # mock `get_kata_number()` as our scope here is to test `get_slack_message()` function
        self.notification.get_kata_number = MagicMock(name="get_kata_number")
        self.notification.get_kata_number.return_value = 5

    def tearDown(self) -> None:
        print("I am teardown, You can use me to define instructions that will be executed after each test method.")

    def test_slack_message(self) -> None:
        slack_message_returned = self.notification.get_slack_message(user_name=TestNotification.TEST_USERNAME)
        self.assertEqual(TestNotification.EXPECTED_SLACK_MESSAGE, slack_message_returned)
```
- Execute the test
```shell
pipenv run python3 -m unittest python/tests/test_notification.py
```
- You should be getting below output
```shell
I am setup, You can use me to define instructions that will be executed before each test method.
I am teardown, You can use me to define instructions that will be executed after each test method.
.I am setup, You can use me to define instructions that will be executed before each test method.
I am teardown, You can use me to define instructions that will be executed after each test method.
.I am setup, You can use me to define instructions that will be executed before each test method.
I am teardown, You can use me to define instructions that will be executed after each test method.
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```
> Congratulations, you have successfully tested `notification.get_slack_message` method. 
- We still need to test `notification.send_notification`.
- Update and add below **POSITIVE** test case to test `notification.send_notification` in `python/tests/test_notification.py`
```python
    def test_send_notification_http_ok(self):
        with requests_mock.Mocker() as m:
            m.post(requests_mock.ANY, text=json.dumps(TestNotification.EXPECTED_SLACK_MESSAGE),
                   status_code=HTTPStatus.OK)
            status_code_returned = self.notification.send_notification(user_name=TestNotification.TEST_USERNAME)
            self.assertEqual(HTTPStatus.OK, status_code_returned)
```
- Update and add below **NEGATIVE** test case to test `notification.send_notification` in `python/tests/test_notification.py`
```python
    def test_send_notification_http_not_ok(self):
        with requests_mock.Mocker() as m:
            m.post(requests_mock.ANY, text=json.dumps(TestNotification.EXPECTED_SLACK_MESSAGE),
                   status_code=HTTPStatus.NOT_FOUND)
            with self.assertRaises(ValueError) as context:
                self.notification.send_notification(user_name=TestNotification.TEST_USERNAME)
            self.assertTrue(
                str(context.exception.args[0]).startswith("Request to slack returned an error HTTPStatus.NOT_FOUND"))
```
- Execute the test
```shell
pipenv run python3 -m unittest python/tests/test_notification.py
.
...
..
Ran 3 tests in 0.012s

OK
```
- Awesome, you have successfully written tests and tested `notification.py` in isolation.
- onwards to presentation and then to [kata-6](../kata-6/HOW-TO.md)

#### Achieved objective? :question: Learnings? :thinking:
- Write Tests :white_check_mark:
- Debugging in IDE (PyCharm) :white_check_mark: