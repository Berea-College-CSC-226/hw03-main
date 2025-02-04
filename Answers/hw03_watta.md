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
    R 155, G 0, B 166
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    R 135, G 68, B 0
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    R 115, G 134, B 120
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
    turtle.pos() or turtle.position()
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    turtle.speed("fastest")
```

2.d. How would you change the turtle's color to xanadu? 

```
    turtle.color(115, 134, 120)
```

2.e. How would you fill a shape with the color xanadu?

```
    turtle.color(115, 134, 120)
    turtle.begin_fill()
    turtle.end_fill()
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    Asking the computer to make your own personal copy 
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    The repository is a place where you can store code, your files, and different versions of the files. It exists on 
    my local machine as well as in Github
```


- What is a **commit**? Why does it need a commit message?

```
    A commit is a point where you want to save your progress. You need a message so you know at which point of the project 
    you are at.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    To push your code means to save your progress on Github servers, so I use the code for continued development. It's 
    being pushed to Github from my computer.
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    It's important because it prevents possible merge conflicts when you want to push your changes.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    There are 3 branches. I see mine, main, and the one I created. 
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    Master is the edits made by everyone and my branch is the edits made by only me.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    When I checkout the master branch, everything I've done is there too. 
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    It's useful because it allows different people to work on it without it affecting the main branch.
```

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will do our best to answer them. Paste the link to your question in Slack here:

```
    If I were to accidentally push the wrong changes how can I undo a git push?
```

---