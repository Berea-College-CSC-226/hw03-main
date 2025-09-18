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
    R: 128, G: 0, B:128
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    R: 165, G: 42, B:42
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    R: 115, G: 134, B:120
```

_Return to the Google Doc to continue this assignment._

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
turtle.fd(distance)

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
    print(turtle.position())
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
turtle.speed()
```

2.d. How would you change the turtle's color to xanadu? 

```
    turtle.color(xanadu)
```

2.e. How would you fill a shape with the color xanadu?

```
    turtle.color("black", "#738678")
    turtle.begin_fill()
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    Making a full copy of git repository.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    project folder
```


- What is a **commit**? Why does it need a commit message?

```
    Commit is like a snapshot and it needs a commit message for explaning the change you did.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
To push your code means to send the changes you made on your local computer (your local repository) to a remote repository, such as GitHub. You are pushing *from* your local machine *to* the remote server so that others can access the updated code.```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
So you get the newest changes other people made before adding yours. This prevents conflicts.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    There is the master branch and my branch. I can see mine, and maybe some others from classmates.
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    Yes. My branch has my changes. The master branch doesn’t have them yet.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    My file disappears or looks different because it’s not in the master branch. The project shows only what’s in that branch.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    Yes, my file comes back. Branching is useful because I can work on my changes without messing up the main project.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will answer them for everyone! Paste the link to your question in Slack here:

```
    https://bereacs.slack.com/archives/C3QACGH8R/p1758164632431489
```

---