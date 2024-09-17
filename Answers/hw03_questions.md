# Fully Functional Gitty Psychedelic Robotic Turtles

## Instructions

**_<span style="color:red">
    VERY IMPORTANT: Make a copy of this file. DO NOT EDIT IT DIRECTLY!
</span>_**

Please replace each `Replace this text with your answer` 
with your answer to the question above.

## SECTION 1: 

1.a. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color purple. 
     What are the R, G, and B values?

```
   The R vaule is 100, the G vaule is 32, and the B vaule is 168.
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    The R vaule is 114, the G vaule is 81, and the B vaule is 53.
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    The R vaule is 115, the G vaule is 134, and the B vaule is 120.
```

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    An alternate command that can be used to move the turtle forward besides the 'turtle.forward()' is turtle.fd()
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
   The command from the turtle library that can be used to print the turtle's current location is turtle.position() or turtle.pos()

```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    To set the turtle's speed to maximum speed, you would use the turtle.speed() function and the maximum speed is represented by the value 0. So, turtle.speed(0) will make the turtle move at the maximum speed, showing no animation, making it automatically draw your code.
```

2.d. How would you change the turtle's color to xanadu? 

```
    To change the turtle's color to xanadu, you would use turtle.color() function and pass the RGB values for xanadu. You would use turtle.colormode(255) which would allow you to use RGB values between 0 and 255, and then you would do turtle.color((115, 134, 120)) to set the turtle's color to the RGB values for the color xanadu.
```

2.e. How would you fill a shape with the color xanadu?

```
    To fill a shape with the color xanadu, you will use turtle.colormode(255) which would allow you to use RGB values between 0 and 255. Next, you will use turtle.fillcolor(115, 134, 120) to set the fill color to xanadu using its RGB values. Next, you will use turtle.begin_fill() to tell the turtle that you are about to draw a shape that should be filled. Next, you will draw the shape you desire. Lastly, you will use turtle.end_fill() to fill the enclosed shape you drew with the specified fill color xanadu.
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    Cloning the repo refers to the process of creating a local copy of a remote repository onto your own machine. When you clone a repo, you download the entire project, including its files, commit history, branches, and other data, allowing you to work on the project locally on your own machine.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    The repository is a storage location for a project’s code, files, and history that is tracked using a version control system. The repository stores all the project’s files, along with the complete history of commits, branches, and other data. When you clone a repository or create a new one on your computer, it exists on your local machine.  When the repository is hosted on GitHub, it's a remote repository. This remote repository serves as the master version of the project that can be accessed by multiple people.
```


- What is a **commit**? Why does it need a commit message?

```
    A commit is a history of changes made to a project's files in a version control system, making it an important point in your development process where you want to save progress, which is done by tagging changes, or revisions, in a document. It needs a commit message to provide context and reasoning for the changes, helping others and myself understand what was modified and why.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    To push your code means to save and upload the changes you’ve made, which saves on Github’s servers. The code is being pushed to the remote repository from the local repository.
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    It is important to pull before you push because it ensures that your local repository is up-to-date with the latest changes from the remote repository, preventing conflicts and merge conflicts, and keeping the project history consistent.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    There are 120 branches in the repository. I see my branch, and I see other people's branches.
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
   My branch and the master branch are mainly the same, the only difference is the answers PDF file in both branches. It shows a change by me in my own branch in the answers PDf file.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    Everything disappears in the master branch, except the README.md file. So basically the master branch changed, except the README.md file.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    Yes, my file is back. Branching useful because it allows teams to track different versions of the codebase, allows for a structured code review process, and allows collaborative work.
```

---

## SECTION 5
- A lot happened in this assignment, and often, you do things without fully 
  understanding them. Your last task is to formulate a question and ask it. 
  To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the instructor 
  will do our best to answer them. Paste the link to your question in Slack here:

```
    https://bereacs.slack.com/archives/C3QACGH8R/p1726546070666829 
```



