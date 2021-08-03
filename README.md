# the-python-workshop

A workshop to learn AWS CloudFormation

The workshop promotes both the knowledge of CloudFormation concepts and skills, as well as good practices (including Continuous Deployment). For best results, templates should be developed and tested incrementally. 

The workshop is structured as a series of *code katas* (see "https://en.wikipedia.org/wiki/Kata_(programming)")

Instructions
====

- Review the [goal](doc/goal.md) 
- Engage in some planning to achieve the goal. This may yield a number of stories, similar to [these](doc/stories.md)
- Each story is achieved through a kata. Work through the katas sequentially. While each kata stands on its own, later katas build upon earlier ones.
- Instructions for each kata are documented independently, beginning with [kata 1](doc/kata-1/HOW-TO.md) 

Cleaning up afterwards!
====

- At any point, you can delete the resources provisioned and avoid incurring costs by deleting the stacks created.
    - Deleting a CloudFormation stack deletes all resources provisioned by the stack
- If you provision any pipelines to deploy other CloudFormation stacks, remember to:
    - IMPORTANT!!! delete the stack provisioned by the pipeline _first_ 
    - only delete the pipeline (or the stack that provisioned the pipeline) afterwards. The stack provisioned by the pipeline depends upon IAM roles provisioned by the pipeline, and may be left orphaned if the pipeline is deleted first. 
    - [ ] TODO: configure the pipelines to provision stacks with `termination-protection` enabled.

Pre-requisites
====

- an account on Github
- git version control client
- AWS account
- AWS CLI installed and configured with credentials privileged to operate upon:
- An IDE (Pycharm, VSCode etc)
- Python 3 installed.
- Basic Python knowledge. This course on [RELX Udemy](https://relxlearning.udemy.com/course/python-for-absolute-beginners-u/)

Organisation
====

- Templates and notes for each kata are in a folder in [`doc`](doc) named after the kata (say, [kata-1](doc/kata-1))
- Instructions for each kata are in the HOW-TO.md document (say, [HOW-TO](doc/kata-1/HOW-TO.md))
- For each kata, a tested template is provided for reference (say, [Story 1 template](doc/kata-1/story_1-template.yaml)). You may refer to it at the conclusion of the kata. 
- for Continuous Deployment pipelines: tested [CloudFormation template](doc/kata-2/pipeline.yaml) and [example parameter file](doc/kata-2/pipeline-parameters.example.json) to be used to provision stacks for the pipelines are provided
- You may review the observations accompanying a kata, as you work on it (say, [observations](doc/kata-1/observations.md)). The observations contain links to the public documentation.