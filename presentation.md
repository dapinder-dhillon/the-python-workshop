# Python Best Practices
## Agenda
- Managing Multiple Python Versions
- Follow style guidelines.
- Use the PyPI Instead of Doing it Yourself
> Katas
- Structure of the Python Project ([kata-1](./doc/kata-1/HOW-TO.md))
- Explicitly declare and isolate dependencies ([kata-2](./doc/kata-2/HOW-TO.md))
- Define types in python ([kata-3](./doc/kata-3/HOW-TO.md))
- Write Object-Oriented Code ([kata-3](./doc/kata-3/HOW-TO.md))
- Follow Single Responsibility (functions too) ([kata-4](./doc/kata-4/HOW-TO.md))
- Write Tests ([kata-4](./doc/kata-4/HOW-TO.md))
- Debugging ([kata-4](./doc/kata-4/HOW-TO.md))
- Boto3 ([kata-5](./doc/kata-5/HOW-TO.md))
- TDD (Test-Driven-Development) ([kata-6](./doc/kata-6/HOW-TO.md))

---

### Managing Multiple Python Versions
- OS Python really belongs to the operating system. After all, it came installed with the operating system.
- You are installing globally when you do `sudo pip install` on system python.
- Package managers (yum, apt, brew etc) install their packages into the global system space.
- Once again, you still don’t have control over what version of Python you can install. If you want to support and test on Python 3.4 - 3.7.
- What would happen on your system when you type python3?
- You can eliminate all these by using [pyenv](https://github.com/pyenv/pyenv). 
- pyenv is a wonderful tool for managing multiple Python versions.
- Same advantages as tfswitch or tfenv but its more important using pyenv due to more complexity around python packages.
> https://github.com/pyenv/pyenv

---

### Follow style guidelines
- The PEP8 holds some great community-generated proposals.
- **PEP** stands for **Python Enhancement Proposals** - these are guidelines and standards for development. 
  This is to make sure all Python code looks and feels the same.
- Few guidelines to go over:
  - Use proper naming conventions for variables, functions, methods, and more.
  - Variables, functions, methods, packages, modules: this_is_a_variable
  - Classes and exceptions: CapWords
  - Protected methods and internal functions: _single_leading_underscore
  - Private methods: __double_leading_underscore
  - Constants: CAPS_WITH_UNDERSCORES
  - Use 4 spaces for indentation. _Convent spaces to tabs_
  - Use an IDE (Pycharm, VSCode etc.) which can enforce these standards.
  - For more conventions, refer to [PEP8](https://www.python.org/dev/peps/pep-0008/).
> https://www.python.org/dev/peps/pep-0008/

---

### Use the PyPI Instead of Doing it Yourself
- One of the reasons behind Python’s popularity is the [PyPI](https://pypi.org/) - this is the Python Package Index; it has more than 319,515 
  projects (_at the time of writing this presentation_).
- You should use code from this instead of writing it yourself - this saves time and lets you focus on the more important 
  things.
- Install these using pip. You can also create and upload your own packages here.
- You can envision this same as using ansible galaxy collections (e.g. `ansible-galaxy collection install amazon.aws`) 
or terraform modules (CE, community etc.). 
- Do not reinvent the wheel. :point_left:
> https://pypi.org/

---
## Complete [Kata-1](doc/kata-1/HOW-TO.md) and [Kata-2](doc/kata-2/HOW-TO.md) 
---
### Type Checking
- Python is a dynamically typed language. 
- Lets work with some examples.
- The opposite of dynamic typing is static typing. e.g. Java and C.
- Python will always [remain a dynamically typed language](https://www.python.org/dev/peps/pep-0484/#non-goals). 
- However, [PEP 484](https://www.python.org/dev/peps/pep-0484/) introduced type hints, which make it possible to also do static type checking of Python code.
type hints.
- type hints has no runtime effect: they are only hints and are not enforced on their own.
- You need use a static type checker (a tool). You might already have a built in IDE like PyCharm.
- Most common tool for doing type checking is [Mypy](http://mypy-lang.org/). 
- There are more out there like pyright (microsoft), pyre (facebook) etc.

---
## Complete [Kata-3](doc/kata-3/HOW-TO.md) 
---
