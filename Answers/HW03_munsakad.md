# Fully Functional Gitty Psychedelic Robotic Turtles
#
# Name: Dingani Munsaka
#Title: Fully Functional Gitty Psychedelic Robotic Turtles
#Google doc link: https://docs.google.com/document/d/1_QtOsvS1fWH7XksrLDKD0NqiDHW8SSyqDkNQlqv7ePw/edit?usp=sharing
#Acknoledgements: I used google to confirm some of the answers 
#
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
    R-222
    G-0
    B-255
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    R-101
    G-72
    B-14
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    R-112
    G-149
    B-144
```

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
    turtle.pos()/turtle.position()
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    turtle.speed(0)
```

2.d. How would you change the turtle's color to xanadu? 

```
    turtle.color(112,149,144)
```

2.e. How would you fill a shape with the color xanadu?

```
    turtle.fillcolor(112,149,144) in addition to begin_fill() and end_fill() on the shape that we want to fill 
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
   means creating a local copy of a remote Git repository 
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    A repository is where I store my code, including files, commit history, and branches. It can exist on my local machine or on GitHub (remote repository) after I clone or initialize it.
```


- What is a **commit**? Why does it need a commit message?

```
     Committing a file is like tagging changes, or revisions, in a document. A commit is typically an important point in development process where you want to save progress.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    To push my code means to upload my local commits to a remote repository, like GitHub servers. My code is being pushed from my local machine to the remote repository.
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
To update the changes made by others so as to avoid the merge conflict
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    There are four braches including mine
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    Its kinda the same except that mine has an extra python file and some answered questions, otherwise the layout is the same.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
  My file is no longer there, I can't see it.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    Yes but the question I had answered on section 4 has all disappeared so I had to redo them which sucks, in this case, branching helps saving coppies of our files such that when events like this happens, you will be having a backup plan rather than restarting the whole file. 
```

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will do our best to answer them. Paste the link to your question in Slack here:

```
    https://bereacs.slack.com/archives/C3QACGH8R/p1738473945425329
```

---