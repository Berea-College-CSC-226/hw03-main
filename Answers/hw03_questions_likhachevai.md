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
    R 222
    G 0
    B 255
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    R 151
    G 92 
    B 41

```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    R 111
    G 132
    B 103

```

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    The forward() method moves the turtle forward by a specified distance. An alternative command is the fd() method.
    turtle.forward(distance)
    turtle.fd(distance)
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
    turtle.position()
    turtle.pos()
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
     We set the turtle's speed to maximum using the speed() function with the argument 0.
     turtle.speed(0)
```

2.d. How would you change the turtle's color to xanadu? 

```
    We can use the function pencolor(colorstring) or color(colorstring). For xanady color it is #6F8467. Alos, we can set pencolor to the RGB color.
    pencolor("6F8467")
    
    turtle.colormode(255)
    color(111, 132, 103)
```

2.e. How would you fill a shape with the color xanadu?

```
    To fill a shape with xanadu we set turtle.colormode(255), use fillcolor(111, 132, 103), start with begin_fill(), draw the shape, and end with end_fill().
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
     Cloning a repo means copying it from the internet to the computer so the programmer can work on it. This is done with `git clone <repository_url>`, which downloads all the files and history.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    A repository is a storage for a project's files, managed by Git. It can be local on the computer or remote on platforms like GitHub.

```


- What is a **commit**? Why does it need a commit message?

```
    A commit is saving and tagging a version of the project so the programmer can go back to it if needed. It needs a commit message to explain what changed, helping to track progress easily.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    To push the code means to upload the latest changes from the local repository (on your computer) to a remote repository (like GitHub). This keeps the remote repo updated so it is possible to access the latest version of the project.
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    Replace this text with your answer
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
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    Replace this text with your answer
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    Replace this text with your answer
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