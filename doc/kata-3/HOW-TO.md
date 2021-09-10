
## Story 3: Refactor Notification Module to use Types

### Objectives: (**20 mins**)
- Define types in python

### Steps:
- Refactor the directory structure as we put more responsibilities in the repo and it's better to isolate them in separate 
  directories.
```shell
.
├── Pipfile
├── Pipfile.lock
├── python #feel free to name it scripts or as you like
│   ├── __init__.py
│   ├── logs_processor
│   │   ├── __init__.py
│   │   ├── notification.py
│   └── tests
│       ├── __init__.py
│       └── test_notification.py
└── terraform #terraform code
```
- Install `mypy` as a static type checker and install 3rd party stub required for requests package.
> These should not be installed using pipenv as these are development tools.
```shell
pip install mypy
pip install types-requests
```
- Run `mypy` on `notification.py` to ensure we dont have any issues.
```shell
> mypy python/logs_processor/notification.py #or on the structure you have.
> Success: no issues found in 1 source file
```
- Update `notification.py` to add `strip` function to the username so that we can remove the leading or trailing 
  spaces (_if any_).
```python
# adding .strip()
slack_data = {'text': message.format(username=username.strip(), kata=get_kata_number())}
```

- Change the username and assign it an int. e.g. `from username = "sing22" to username = 1` and run the `mypy` again, 
  it should still be a **SUCCESS** as you `mypy` cannot detect.
- Execute `notification.py`
```shell
> mypy python/logs_processor/notification.py #or on the structure you have.
> Success: no issues found in 1 source file
pipenv run python python/logs_processor/notification.py  --kata=3
```
- You should be getting error now as `'int' object has no attribute 'strip'`.
```shell
Traceback (most recent call last):
  File "python/logs_processor/notification.py", line 35, in <module>
    send_notification(username=username)
  File "python/logs_processor/notification.py", line 13, in send_notification
    slack_data = {'text': message.format(username=username.strip(), kata=get_kata_number())}
AttributeError: 'int' object has no attribute 'strip'
```
- Unlike strongly typed languages which do not let the code run if type does not meet expectation, python lets you. `mypy` 
  could have saved you here if have followed a practice of ensuring checking types prior run.
- IDEs play best here as they have inbuilt static type checkers and keep on provding `WARNIINGS`.
- Update `notification.py` to add `type` and use the style recommendation from [PEP8](https://www.python.org/dev/peps/pep-0008/#other-recommendations) 
  like _no space before and one space after a colon_.
```python
def send_notification(username: str): 
```
- Run `mypy` now and it will show an error.
```shell
> mypy python/logs_processor/notification.py #or on the structure you have.
> python/logs_processor/notification.py:35: error: Argument "username" to "send_notification" has incompatible type "int"; expected "str"
Found 1 error in 1 file (checked 1 source file)
```
- Update your code to mention return types as well.
```python
def send_notification(username: str) -> None: #as this method is not retruning anything.
... 
...
...
def get_kata_number() -> int: # method returning `int`
```
- Execute `notification.py`
```shell
pipenv run python python/logs_processor/notification.py --kata=3
```
- You should have a notification in slack now "_Super! Dapinder, you have successfully completed kata 3 in your journey 
  of learning python best practices._"
- onwards to presentation and then to [kata-4](../kata-4/HOW-TO.md)

#### Achieved objective? :question: Learnings? :thinking:
- Define types in python. :white_check_mark:
- Static typing prevents this kind of bug/error.  Before you even try to run the program, static typing will tell you 
  that you can’t pass `1` into `send_notification()` because it expects a `str` but you are giving it an `int`.
- Traditionally, you would use docstrings if you wanted to document the expected types of a function’s arguments.
  This works, but as there is no standard for docstrings, they can’t be easily used for automatic checks.
- Type hints help you build and maintain a cleaner architecture.
- When this kind of bug happens in Python, it’s usually not in a simple function like this. The bug is usually buried 
  several layers down in the code and triggered because the data passed in is slightly different than previously expected. 
  To debug it, you have to recreate the user’s input and figure out where it went wrong.

>So much time is wasted debugging these easily preventable bugs.
