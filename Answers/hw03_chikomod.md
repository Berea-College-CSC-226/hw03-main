# Fully Functional Gitty Psychedelic Robotic Turtles

## Instructions

**_<span style="color:red">
    VERY IMPORTANT: Make a copy of this file. DO NOT EDIT IT DIRECTLY!
</span>_**

1. Make a copy of this file by selecting the file and hitting CTRL+C. 
2. Paste your copy into the `Answers` folder.
3. Name the file `hw03_username.md` replacing `username` with your username.
4. Replace each `Replace this text with your answer` with your answer to the question above it.

## SECTION 1

1.a. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color purple. 
     What are the R, G, and B values?

```
    R is 255, G is 0, and B is 255
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    R is 110, G is 13, and B is 37.
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    R is 115, G is 134, and B is 120.
```

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    turtle.fd()
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
    turtle.pos()
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    turtle.speed(0)
```

2.d. How would you change the turtle's color to xanadu? 

```
    turtle.colormode(255)
    turtle.color(115,134,120)
```

2.e. How would you fill a shape with the color xanadu?

```
    turtle.colormode(255)
    turtle.color(115,134,120)
    turtle.begin_fill()
    # Draw shape
    turtle.end_fill()
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    It means creating a copy of git repository from a remote source, github to the computer.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    A repository is a storage space where project files are stored. Repositories exist locally on
    the computer and also remotely on hosting platforms like github.
```


- What is a **commit**? Why does it need a commit message?

```
    A commit is like saving a version of your work but with added power to track changes, collaborate,
    and revert to previous states if needed. It needs a message to explain what changed and why so that
    should understand commit's purpose without reading the code.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    Pushing your code means uploading your local changes (commits) from the computer to a remote
    repository. The code is being pushed from the local repository on the computer to the remote 
    repository on github.
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    To prevent conflict merges as others might have updated the work in the remote repository so its
    important to have up-to-date work.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    24
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    Yes
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    My changes were not saved to the original branch. All the prompts reverted back to the original state.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    Yes, you get to work on your own without interfering in the whole project.
```

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will do our best to answer them. Paste the link to your question in Slack here:

```
    I wanted to ask this question but when i opened slack i found out that Ahna Watt had already asked it so I read Dr. Scott's response to the question. 
    https://bereacs.slack.com/archives/C3QACGH8R/p1738673977169939?thread_ts=1738640407.489679&cid=C3QACGH8R
```

---