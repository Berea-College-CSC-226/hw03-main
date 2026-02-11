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
    128, 0 , 128
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    165, 42, 42
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    115, 134, 120
```

_Return to the Google Doc to continue this assignment._

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    turtle.fd() also works as an alternative to the forward() command
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
    turtle.pos() can be used to print the turtle's current location
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    turtle.speed(10)
```

2.d. How would you change the turtle's color to xanadu? 

```
    We would first have to set the colormode to RGB by writing
    wn.colormode(255)
    And then for the turtle we want to change the color of
    we will write
    besher.color(115, 134, 120) (for my teamwork 03)
    
```

2.e. How would you fill a shape with the color xanadu?

```
    besher.fillcolor(115, 134, 120)
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
Cloning a repository means making a copy of the entire GitHub 
repository on my local computer so I can work on the code locally.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
A repository is a collection of files, code, and version history for a project. 
It exists on GitHub (online), and when cloned, it also exists on my local computer.
```


- What is a **commit**? Why does it need a commit message?

```
A commit is saving changes to a code. It needs a commit message
so that for anyone reviewing the code, they can know what changes you
saved before opening to see the code. 
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
Pushing your code means uploading my local saves to the remote respository from my 
local computer.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
It is important to pull before pushing so I get the most recent changes from the remote repository
and avoid conflicts with other people's work. 
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
There are multiple branches in the repository, including the main branch and my own branch.
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    Yes, they are different. My branch contains my changes, while the main branch does not. 
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    When I switch to the master branch, my file disappears or reverts 
    because it does not exist in the master branch.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    Yes, my file comes back when I switch back to my branch. Branching is useful because it
     allows me to work on changes independently without affecting the main codebase.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will answer them for everyone! Paste the link to your question in Slack here:

```
    I don't have a question right now related to the assignment. But I will be sure
    to post in the Slack channel in case I have questions in the future. I want
    to play around with the code a bit more. 
```

---