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
    R: 173 G: 7 B: 159
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    R: 70 G: 7 B: 7
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    R: 115 G: 134 B: 120
    This color is not named xanadu in the website we're sent to, but when I looked it up I found that this is the same
    color, just named differently.
```

_Return to the Google Doc to continue this assignment._

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    I could use 'turtle.fd()' instead.
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
    turtle.pos() or turtle.position()
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    turtle.speed(0). Numbers greater than 10 or smaller than 0.5 when used as an input also set speed to 0.
```

2.d. How would you change the turtle's color to xanadu? 

```
    First enter the command "screen.colormode(255)" then enter "turtle.color(115,134,120)".
```

2.e. How would you fill a shape with the color xanadu?

```
    First enter the command "screen.colormode(255)", then enter "turtle.fillcolor(115,134,120)". Next, enter
    "turtle.begin_fill()", draw the shape, then enter "turtle.end_fill()".
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    Cloning the repo makes a copy of the code on the local computer.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    The repository is the area where GitHub keeps the current code and all the older versions of it. It exists in
    GitHub, though we can clone it. 
```


- What is a **commit**? Why does it need a commit message?

```
    A commit is where the coder makes a note that they completed an important part of the program, saving the work
    they've done so far. A commit message is necessary to know what was accomplished since the last commit.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    Pushing your code sends it from your computer to GitHub and tells GitHub to update the original code with your
    changes.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    If you don't pull beforehand, you may accidentally create a merge conflict. If someone changed the code between your
    last pull and this push, then whether or not you changed that section, it's different from what's on GitHub.
    However, even if it doesn't create a merge conflict, the changes may cause your code to no longer work, and as such
    you would want to fix it to work with the new code.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    There are seven branches at the moment that I am answering this question. Main, my branch, santosb2's branch, 
    two of ciccariellop's branches, Kirkpatrickm's branch, and "fix_a03_stubs".
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    They are different, mine has two more items in the "Answers" folder.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    My file was gone.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    My file is now back. Branching allows you to create new files and code that you aren't sure you want to use and 
    easily keep a copy of your work without those testing files so you don't accidentally mix them up.
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