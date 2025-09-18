# Fully Functional Gitty Psychedelic Robotic Turtles

## Instructions

1. In the top right of Pycharm, change the display of this file to 
   `Editor and Preview` mode, so you can see the code (markdown) and the rendered output. 

![Screenshot of "Editor and Preview" mode](split_mode_markdown.png)

The next line should appear red in the `Preview` mode on the right:

**_<span style="color:red">
    VERY IMPORTANT: Make a copy of this file. DO NOT EDIT IT DIRECTLY!
</span>_**

2. Make a copy of this file by selecting the file and hitting CTRL+C. 
3. Paste your copy into the `Answers` folder.
4. Rename the file to `hw03_username.md` replacing `username` with your username.

_Return to the Google Doc to continue this assignment._

---

## SECTION 1

Replace each `Replace this text with your answer` with your answer to the question above it.

1.a. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color purple. 
     What are the R, G, and B values?

```
 Purple
(128, 0, 128)
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
Brown
(165, 42, 42)
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
Xanadu
(115, 134, 120)
```

_Return to the Google Doc to continue this assignment._

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
t.fd()
Both turtle.forward(distance) and turtle.fd(distance) do the same thing.

```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
t.pos()
(or t.position() — both return the (x, y) coordinates).
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
t.speed(0)
0 is the “fastest” setting.
```

2.d. How would you change the turtle's color to xanadu? 

```
t.color((115, 134, 120))
Make sure you set screen.colormode(255) first so 0–255 values work.
```

2.e. How would you fill a shape with the color xanadu?

```
t.fillcolor((115, 134, 120))
t.begin_fill()
# draw your shape here
t.end_fill()
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
Cloning a repo means making a full copy of the repository from GitHub (or another remote server) 
onto your own computer. This lets you work on the code locally.

```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
A repository is the project’s storage place that holds all the files and history. 
It mainly exists on GitHub (the remote version), but once you clone it, you also 
have a copy on your local machine.

```


- What is a **commit**? Why does it need a commit message?

```
A commit is like saving a snapshot of your work in Git. It records the changes you made at that point in time. 
A commit message is needed so you (and others) can understand what changes were made and why.

```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
Pushing your code means sending your saved changes (commits) from your local computer to the remote repository on GitHub. 
It keeps the GitHub version up to date with the work you’ve done locally.

```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
To make sure my local branch has the newest commits from the remote. Pulling first prevents
errors and reduces merge conflicts.

```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
I see 2 branches: master (main) and my hw03_alemuy branch.

```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
Yes. My branch has my latest commit(s) for this assignment, while master doesn’t have those changes yet.

```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    Replace this text with your answer
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    Replace this text with your answer
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will answer them for everyone! Paste the link to your question in Slack here:

```
    Replace this text with your answer
```

---