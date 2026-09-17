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
   128,0,128
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    165,42,42
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
   115,134,120
```

_Return to the Google Doc to continue this assignment._

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the
`forward()` method. What alternate command can be used to move the turtle forward, besides the `turtle.forward()`
command you are used to using?

```
    tutrle.fd()
```

2.b. Which command from the turtle library can be used to print the turtle's current location?

```
    turtle.pos() or turtle.postition()
```

2.c. How do you set the turtle's speed to maximum speed?

```
turtle.speed()
```

2.d. How would you change the turtle's color to xanadu?

```
    You can use the hex code for xanadu by turtle.color("#738678")
```

2.e. How would you fill a shape with the color xanadu?

```
    turtle.fillcolor("#738678")
    turtle.begin_fill()
    turtle.end_fill()
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
Cloning means creating a complete local copy of a remote Git repository onto your own computer.```

- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
A repository is a storage space that holds your project's files and the entire history of changes made to those files. the remote repository is on GitHub, and your local repository is on your machine after you clone it.```

- What is a **commit**? Why does it need a commit message?

```
A commit is a saved copy of your code at any time. It requires a commit message to explain what changes were made which helps eveyone understand the project's history.
- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
Pushing means uploading your local commits to the remote repository. Your code is being pushed from your local machine to GitHub.```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Main Into Your Local

4.a. Why do you think it is important to pull before you push?

```
It ensures your local repository is completely up to date with any changes other people might have made. If you push without pulling first, you might overwrite someone else's work or cause difficult merge conflicts.```

4.b. How many branches are in the repository? Click the link to look at the branches. Do you see yours? Do you see any
others?

```
There is alot, like 50+```


4.c. Compare your branch and the main branch by clicking on each. Are they different?

```
    They are different.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     main branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    It is not there. 
```

4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations here, describe how branching
is useful:

```
Branching allows you to safely experiment/ build new features/ dp assignments in an seprate workspace. You can make changes without breaking or altering the original code in the main branch, and easily switch back and forth between different versions.```

_Return to the Google Doc to continue this assignment._

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will answer them for everyone! Paste the link to your question in Slack here:

```
Is there an easier way to figure out the exact (x, y) coordinates for turtle shapes?```

---
