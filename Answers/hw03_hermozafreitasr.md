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
    (214, 127, 248)
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    (130, 64, 16)
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    (43, 129, 103)
```

_Return to the Google Doc to continue this assignment._

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    there's an abbreviation for the function forward that is just .fd(distance). Although, that's not a new method,
    which is why I'd think of setting the exact coordinates as a another way to move the turtle (because the turtle 
    also draws when it teleports); we can do this using goto(coordinates) or setposition(x, y)
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
    turtle.position() will return a tuple with the x and y coordinates; 
    we can print(turtle.position()) and get its location

```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    using turtle.speed("fastest")
```

2.d. How would you change the turtle's color to xanadu? 

```
    turtle.pencolor(43, 129, 103)
```

2.e. How would you fill a shape with the color xanadu?

```
    first we need to stablish: turtle.colormode(255)
    then we can use turtle.fillcolor(43, 129, 103)
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    It is making a copy of a project locally in your computer
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    The repository is like a container that stores all the files of a project, it exists in Github
```


- What is a **commit**? Why does it need a commit message?

```
    a commit is a way of saving the changes you've made. It needs a message
    because you're modifying a project and we need to identify the kind of changes or 
    additions to the original code so that later in the future it is easier to understand
    and to debug.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    Pushing the code is like updating your changes into the remote version of the repository.
    It goes from your local clone to the original repository in github
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    So that you work with the updated projects and don't make changes where changes have already been made
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    I only see 3 other branches and I don't see mine because I haven't pushed yet
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    Yes they're different
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    It dissapeared for a while since it doesn't exist in the main branch
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    branching is useful in terms of upgrades or maintainance. If you already have some code that works 
    properly you'll want to keep it as it is, so that previous functionality doesn't dissapear.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will answer them for everyone! Paste the link to your question in Slack here:

```
    https://bereacs.slack.com/archives/C3QACGH8R/p1758162654002539
```

---