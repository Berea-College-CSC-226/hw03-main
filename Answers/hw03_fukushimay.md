# Fully Functional Gitty Psychedelic Robotic Turtles

## Instructions

1. In the top right of Pycharm, change the display of this file to 
   `Editor and Preview` mode, so you can see the code (markdown) and the rendered output. 

![Screenshot of "Editor and Preview" mode](split_mode_markdown.png)

In PyCharm, the next line should appear red in the `Preview` mode on the right:

**_<span style="color:red">
    VERY IMPORTANT: Make a copy of this file. DO NOT EDIT IT DIRECTLY!
</span>_**

2. Make a copy of this file by selecting the file and hitting CTRL+C.
3. Paste your copy into the `Answers` folder.
4. Rename the file to `hw03_username.md` replacing `username` with your username.
5. Replace each `Replace this text with your answer` with your answer to the question above it.

_Return to the Google Doc to continue this assignment._

---

## SECTION 1

1.a. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color purple. What are the R,
G, and B values?

```
    rgb(128, 0, 128)
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    rgb(165, 42, 42)
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    rgb(115, 134, 120)
```

_Return to the Google Doc to continue this assignment._

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the
`forward()` method. What alternate command can be used to move the turtle forward, besides the `turtle.forward()`
command you are used to using?

```
    turtle.fd()
    turtle.back()
```

2.b. Which command from the turtle library can be used to print the turtle's current location?

```
    print(turtle.position())    
```

2.c. How do you set the turtle's speed to maximum speed?

```
    turtle.speed(10)
```

2.d. How would you change the turtle's color to xanadu?

```
    turtle.color(115, 134, 120)
```

2.e. How would you fill a shape with the color xanadu?

```
    turtle.fillcolor(115, 134, 120)
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    Making a copy of the project file to the local machine.
```

- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    Repositories can exist on both local machines and in Github, and is a file that Git uses to keep track of changes.
```

- What is a **commit**? Why does it need a commit message?

```
    A way to save progress, and a message can indicate what kind of change was made.
```

- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    Pushing your code refers to the action when you submit your changes from your local machine to Github.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Main Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    So that merge conflicts are kept minimal, and your work will not overwrite someone else's work.
```

4.b. How many branches are in the repository? Click the link to look at the branches. Do you see yours? Do you see any
others?

```
    53 branches as of 9/12 9:39PM.
```


4.c. Compare your branch and the main branch by clicking on each. Are they different?

```
    I don't see my branch on github since I haven't pushed it yet. But the files are different as I added some to 
    "Answers," text, code, and the number of commits are different. A lot of differences.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     main branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    My files that I had in my branch were no there, and there was only a README.md file.
```

4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations here, describe how branching
is useful:

```
    My file is back. By using the main branch as a locker that stores code that is already working, and a branch as a 
    experiemental space, it keeps my project going, while I can make adjustments and developments to the project.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will answer them for everyone! Paste the link to your question in Slack here:

```
    1. What is the difference between deleting a branch and deleting the files that were created on that branch?
    2. Can you undo a commit after pushing it to GitHub, and if so, what happens to the commit history?
    3. If I create a branch from another branch instead of from main, what happens when I eventually merge it into main?
```

---
