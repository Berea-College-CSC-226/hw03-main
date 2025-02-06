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
    Red=179, Green=0, Blue=255
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    Red+100, Green=30, Blue=0
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    Red=87, Green=112, Blue=92
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
    turtle.pos()
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    turtle.speed(10)
```

2.d. How would you change the turtle's color to xanadu? 

```
    turtle.colormode(255) #enables RGB color mode
    turtle.color((87,112,92)) #sets pen and fill color
    turtle.pencolor((87,112,92)) #sets only the pen color
```

2.e. How would you fill a shape with the color xanadu?

```
    turtle.colormode(255) #turns on RGB
    turtle.fillcolor((87,112,92)) #sets fill color
    turtle.begin_fill() #starts fill
    turtle.end_fill() #ends fill
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    Cloning the repro is when you pull the most recent copy of data from a repository.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    A centralized data storage location. Github.
```


- What is a **commit**? Why does it need a commit message?

```
    A commit is a save of the updated data to your local repository, not uploaded to the central repository until pushed. It saves a new version, and it needs a meaningful message because previous commits can be reverted too if need be. Thats message tells you what was going on at that point in your work.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    To send your updated data to the centralized/remote repository.
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
   To avoid redundancy in merge requests. You want to start with the most updated version.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    5. Yes, I see mine and other students branches.
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    yes, the master does not have my file I added
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    It disapears.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    Yes. Its very useful for collaborating. Manu workers can work on parts of code without messing up the main code.
```

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will do our best to answer them. Paste the link to your question in Slack here:

```
    https://bereacs.slack.com/archives/C3QACGH8R/p1738540995613029
```

---