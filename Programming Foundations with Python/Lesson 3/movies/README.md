# [Nanodegree](https://www.udacity.com/nanodegree)

## [Programming Foundations with Python](https://www.udacity.com/course/ud036)
---
### [Lesson 3](https://www.udacity.com/course/viewer#!/c-ud036/l-997889780)
---

 Lesson 3 YouTube playlist ID: [PLBxMIgvbjWQgmvBhmcSOAWGKM3-9XAfBn](https://www.youtube.com/playlist?list=PLBxMIgvbjWQgmvBhmcSOAWGKM3-9XAfBn)

___

#### Movie Website Mini-Project

  - Generate an HTML file that plays movie trailers
    - [Python Source](https://github.com/CrandellWS/Udacity-Nanodegree/tree/9e8353fd04c0e6de35a468c4ff8f2059c1a3de31/Programming%20Foundations%20with%20Python/Lesson%203/movies)
    - [Live Example](http://bl.ocks.org/CrandellWS/raw/2e7d918cbae163ca9c1b)
    - [Live Example with source](http://bl.ocks.org/CrandellWS/2e7d918cbae163ca9c1b)
    - [YouTube Video of Mini-Project](https://youtu.be/NC5MoSRxAwQ)
    
#### Notes

##### How to used `fresh_tomatoes.py` as a submodule
 - [Git Submodules](https://git-scm.com/docs/git-submodule)
    1. Fork the orignal repository at https://github.com/adarsh0806/ud036_StarterCode
    2. Get the url to your clone fork (SSH or HTTPS your preference)
      - Example of my fork:
        - SSH -> git@github.com:CrandellWS/ud036_StarterCode.git
        - HTTPS -> https://github.com/CrandellWS/ud036_StarterCode.git
    3. Add the repository as a submodule using the terminal
      - Example with SSH
        - git submodule add git@github.com:CrandellWS/ud036_StarterCode.git
  - Important Notes
    - When making changes to the submodule
      - `cd` into the submodule directory Then
        - When changes are made to the actual submodule
          - `git add -A` -> add all changes to the submodule
          - `git commit` -> commit all changes to the submodule
          - `git push` -> push changes to the remote submodule's repository
        - When changes are made to the submodule's repository
          - `git pull`-> pull changes from the remote submodule's repository
          - `git add -A` -> add all changes to the submodule
          - `git commit` -> commit all changes to the submodule
      - `cd ..` change directories to main project
      - `git add -A ` -> add all submodule changes to the project
      - `git commit` -> commit all submodule changes to the project
      - `git push` -> push all changes to the project's remote repository
    - To use **`from ud036_StarterCode import fresh_tomatoes`**
      - Must add **`__init__.py`** to the *ud036_StarterCode* directory
        - `__init__.py` can be an empty file
        - see -> https://docs.python.org/tutorial/modules.html#packages
