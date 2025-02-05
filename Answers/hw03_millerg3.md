# Fully Functional Gitty Psychedelic Robotic Turtles

## Instructions

**_<span style="color:red">
    VERY IMPORTANT: Make a copy of this file. DO NOT EDIT IT DIRECTLY!
</span>_**

1. Make a copy of this file by selecting the file and hitting CTRL+C. 
2. Paste your copy into the `Answers` folder.
3. Name the file `hw03_username.md` replacing `username` with your username.
4. Replace each `Replace this text with your answer` with your answer to the question above it.

## SECTION 1

1.a. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color purple. 
     What are the R, G, and B values?

```
Red 128, Green 0, Blue 255
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
Red 101, Green 68, Blue 11
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
Red 85, Green 137, Blue 45
```

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
pos() or position()
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
Set it to 0, means no animation takes place and it moves instantly.
```

2.d. How would you change the turtle's color to xanadu? 

```
wn.colormode(255) This makes it so the rgb values can be used up to the end of the range 0-255.
alex.color(85, 137, 45) alex being the turtles name, set the (r, g, b) values to the corresponding values for xanadu.
```

2.e. How would you fill a shape with the color xanadu?

```
import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
wn.colormode(255)
alex.begin_fill()
alex.fillcolor(85, 137, 45)
for i in range(4):
    alex.forward(100)
    alex.right(90)
alex.end_fill()

wn.exitonclick()
Set the colormode to 255 so any numbers in that range work, start the filling and set the color at first, then do the drawing, then end the fill!
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
It makes a copy of the repository.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
It contains the code is kept, changes saved, and any files in the projects. The repo exists in Github, but when cloned a copy is stored on your local computer or other machine.
```


- What is a **commit**? Why does it need a commit message?

```
It means to save the changes made to your code or files (on local machine), it needs a message so you can know what was changed and you can revert back to that if needed.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
While the commit saves changes on your computer, pushing it moves your changes from your local machine to the Github repository.
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
 To get the latest changes from others.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
12, I don't see mine since I haven't pushed it yet, but I see others.
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
They are different.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
It went away.
(placeholder change)

```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
I got it back, which is useful because I can make files that are only available on my branch and don't conflict with others.
```

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will do our best to answer them. Paste the link to your question in Slack here:

```
    Replace this text with your answer
```

---