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
   RGB(128, 0, 128)
  #800080

```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    RGB(165, 42, 42)
    #A52A2A

```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    RGB(115, 134, 120)
    #738678

```

_Return to the Google Doc to continue this assignment._

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
    turtle.position()
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    turtle.speed(0) or turtle.speed("fastest")

```

2.d. How would you change the turtle's color to xanadu? 

```
    turtle.colormode(255)
turtle.color(115, 134, 120)   # Xanadu

```

2.e. How would you fill a shape with the color xanadu?

```
   import turtle

turtle.colormode(255)             # enable RGB values (0–255)
turtle.fillcolor(115, 134, 120)   # set fill color to Xanadu (RGB)
turtle.begin_fill()               # start filling

# draw a square
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.end_fill()                 # end filling

turtle.done()

```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    Cloning is the process of downloading that entire repository, including all files, commit history, and branches, so you can work on it locally.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    That’s the remote repository which is the shared copy of the project stored online so others can access, collaborate, and contribute and it is store and fully hosted on Git except user clone a copy to their computer.
```


- What is a **commit**? Why does it need a commit message?

```
    Commit creates a history for the file and it is mostly needed a message so it can be easliy identy from the main branch. 
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    Pushing means to send to git, the work you have done. It gives git the abality to show other to see and access, it's like save online after working on a project. 
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    You need to pull so you can have the updated version of the code so that when you work you will only need to be updating your branch as needed. 
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    for now 14, Yes i saw mine.
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    Yes, they are.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    Upon update, yes it did change as i created i work on my branch. 
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