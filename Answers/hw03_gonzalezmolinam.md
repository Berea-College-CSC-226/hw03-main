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
   rgb(108, 37, 179) 
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    rgb(97, 45, 24)
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    rgb(83, 90, 73)
```

_Return to the Google Doc to continue this assignment._

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    The alternate method taht can be used to move a turtle forward is "turtle.fd" both with the parameter (distance) which can be an integer or a float.
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
 It can be "turtle.position()" or "turtle.pos()", both variations print the turtle's current location (x, y) (as a Vec2D vector) 
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
With "turtle.speed()", and the parameters from the parenthesis is an integer in the range from 0..10. if input is a number bigger than 10 or smaller than 0.5, speed is set to 0. Speedstrings are mapped so I thik the maximum speed is "0"
```

2.d. How would you change the turtle's color to xanadu? 

```
  I would put 
import turtle

t = turtle.Turtle()

turtle.colormode(255) #I had to look for this because I was always recibing an error "bad color sequence" everytime I ran the code: https://www.youtube.com/watch?v=4XwKjzxk4M8&t=110s
t.shape("circle")
t.color(115, 134, 120)
turtle.done()

```

2.e. How would you fill a shape with the color xanadu?

```
import turtle
turtle.colormode(255)
t = turtle.Turtle()


t.shape("circle")
t.fillcolor((115, 134, 120))
turtle.done()   
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    It means to create a clonned version from the original code to avoid messing up the original one with new changes.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
  A repository is the project folder that Git tracks. It exists in two places: in my computer and on github locally and remote 
```


- What is a **commit**? Why does it need a commit message?

```
    A commit is to save progress, for example if i'm coding with some else and we didn't agree on something we can commit the code, save it and then we can come back and revert changes if needed. A commit message is a tag that indicates the changes that were made since the last commit.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
   Pushing your code means sending your work from your computer to GitHub. You push from your computer to the online copy of your project on GitHub so it stays saved and updated.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    Because pulling first keeps you from overwriting someone else’s work
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    I think there is only one, I don't know where the link is exacly and i only see mine.
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    Yes, they're different because the main does not have my changes. 


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
 They disapeared, all my files were gone when I clicked on checkout in the master branch, they came back when I checked out my branch again. 
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
 Yes, my file is back and branching is useful because of two main things to avoid messing up the original code, crashing it and work with different approaches also it is useful if you're working with a team.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will answer them for everyone! Paste the link to your question in Slack here:

```
    https://bereacs.slack.com/archives/C3QACGH8R/p1770784666460479   
```

---