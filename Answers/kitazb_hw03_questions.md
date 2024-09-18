# Fully Functional Gitty Psychedelic Robotic Turtles

## Instructions

**_<span style="color:red">
    VERY IMPORTANT: Make a copy of this file. DO NOT EDIT IT DIRECTLY!
</span>_**

Please replace each `Replace this text with your answer` 
with your answer to the question above.

## SECTION 1: 

1.a. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color purple. 
     What are the R, G, and B values?

```
    R: 99
    G: 0
    B: 148
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    R: 148
    G: 89
    B: 0

```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    R: 115 
    G: 134 
    B: 120
```

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    turtle.fd(100) (from the turtle documentation). It moves the turtle by 100 units (or whatever we pass as an argument to it.)
    It takes only one argument: the number of units to move forward. 
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
    turtle.pos()
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    turtle.speed('fastest')
```

2.d. How would you change the turtle's color to xanadu? 

```
    First, we neet to set the color mode to 255:
    turtle.colormode(255)
    turtle.color(115, 134, 120)
```

2.e. How would you fill a shape with the color xanadu?

```
    First, we neet to set the color mode to 255:
    turtle.colormode(255)
    
    Then we need to set the fill color and set the starting point for filling process:
    
    turtle.fillcolor(115, 134, 120)
    turtle.begin_fill()
    
    Then we need to draw a shape (say, a square):
        turtle.forward(100)   # Bottom of the ship
    turtle.left(90)
    turtle.forward(100)   # Left side
    turtle.left(90)
    turtle.forward(100)   # Right side
    turtle.left(90)
    turtle.forward(100)

    Finally, we need to fill it out:
    turtle.end_fill()

```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    It means making my own copy of on my local machine form the remote repository on GitHub servers
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    A repository (repo) is a a place where we can store source codes. It can be on my machine locally and on Github remotely.
```


- What is a **commit**? Why does it need a commit message?

```
    A commit is when I save the latest update of my code to the branch.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    To push a source code is to upload my local version of code base from the branch to the remote version (on Github).
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    To make sure that I have the updated code from my partner(s) so we avoid conflict when possible.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    Remotely, I see 108 brancheas. I did not see my branch, but I saw A LOT of other's branches 
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    Yes, they are different. I see that there is a seperate copy of questions.md with my user name on it that I created, and pushed 
    to my branch, while it doesn't exist in the master one.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    It went away. 
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    It is back :) 
    It is useful in a way that everyone works on their own version to avoid mess when developing a project.
    It is also helpful if I want to go back to older versions.
```

---

## SECTION 5
- A lot happened in this assignment, and often, you do things without fully 
  understanding them. Your last task is to formulate a question and ask it. 
  To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the instructor 
  will do our best to answer them. Paste the link to your question in Slack here:

```
    Posted:
    
Hi all,

My question is about the following:

When I need to start working, I need to pull the master branch to ensure anything my teammate did is updated on my local branch, and then I can push. This is clear to me so far.

However, what if we are working on the project simultaneously? I can make pull the code from master, but it will change while I am working on the project, and by the time I push, conflict may happen. How do we avoid/resolve this?
```
