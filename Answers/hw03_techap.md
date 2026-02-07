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
    R = 179, G = 0, B = 255
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    R = 153, G = 97, B = 0
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    R = 102, G = 153, B = 153
    rgb(102, 153, 153)
```

_Return to the Google Doc to continue this assignment._

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    turtle.fd(distance)
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
    turtle.position() or turtle.pos()
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    turtle.speed(0)
```

2.d. How would you change the turtle's color to xanadu? 

```
    Using the rgb values for xanadu: 
    wn.colormode(255)
    turtle.color(102, 153, 153)
```

2.e. How would you fill a shape with the color xanadu?

```
   Using the rgb values for xanadu: 
   wn.colormode(255)
   turtle.begin_fill(102, 153, 153)
   turtle.end_fill() 
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    Creating a copy of the main repo in your IDE to make changes to the code locally.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    A repository is the official source code of any program, and it is usually hosted on GitHub.
```


- What is a **commit**? Why does it need a commit message?

```
    A commit refers to the changes made to a program after cloning it. A commit message is important because it tells
    other programmers working on the code the exact changes you made.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    Pushing a code means sending the updated version of the source code from your local machine to GitHub.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    Pulling before pushing ensures that you have the latest updates, especially if your are working with a partner on 
    the same repo.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    Replace this text with your answer
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    Replace this text with your answer
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