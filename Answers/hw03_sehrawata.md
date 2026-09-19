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
    R:110, G:0, B:255
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    R:135, G:80, B:3
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    R:135, G:130, B:110
```

_Return to the Google Doc to continue this assignment._

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the
`forward()` method. What alternate command can be used to move the turtle forward, besides the `turtle.forward()`
command you are used to using?

```
    turtle.fd() can also be used to move the turtle forward
```

2.b. Which command from the turtle library can be used to print the turtle's current location?

```
    turtle.position() or turtle.pos() prints the turtle's current location
```

2.c. How do you set the turtle's speed to maximum speed?

```
    turtle.speed(0)
```

2.d. How would you change the turtle's color to xanadu?

```
    turtle.color("#738678")
```

2.e. How would you fill a shape with the color xanadu?

```
    turtle.fillcolor("#738678")
    turtle.begin_fill()
    #code for the shape goes here
    turtle.end_fill()
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    Making a copy of the repository from GitHub onto your local computer so you can work on the code.
```

- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    It's the project folder that contains the code and its version history. It can exist both on the local machine and on GitHub
```

- What is a **commit**? Why does it need a commit message?

```
    It's kind of a saved checkpoint of the changes we made, 
    the commit message explains what changed so a group of developers can understand the history of the project later 
```

- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    Pushing means sending your committed changes from the local repository on the computer to the remote repository on github
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Main Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    It is important to pull before you push so you have the latest changes from the repository and avoid conflicts with other people's work.
```

4.b. How many branches are in the repository? Click the link to look at the branches. Do you see yours? Do you see any
others?

```
    There are in total 54 branches. Yes I can see my branch, and other people's branch too.
```


4.c. Compare your branch and the main branch by clicking on each. Are they different?

```
    Yes hw03_sehrawata is different than main by 1 commit.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     main branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    After I checked out the main branch, my file was no longer there because the file was only added to my branch and not to main.
```

4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations here, describe how branching
is useful:

```
    Yes, my file came back when I switched back to my branch. 
    Branching is useful because it lets different people work on their own changes without affecting the main branch or other people's work.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will answer them for everyone! Paste the link to your question in Slack here:

```
    https://bereacs.slack.com/archives/C3QACGH8R/p1789854492649579
```

---
