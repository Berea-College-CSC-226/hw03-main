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
    R:193, G:84,B:255

```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    R: 107, G: 29, B: 29
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    R: 115, G:134, B: 120
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
    turtle.position()
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    turtle.speed(0)
```

2.d. How would you change the turtle's color to xanadu? 

```
    turtle.color("xanadu")
```

2.e. How would you fill a shape with the color xanadu?

```
    turtle.fillcolor("xanadu")
turtle.begin_fill()
# Draw the shape here
turtle.end_fill()
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
      Cloning a repo means copying a project from GitHub to your computer. This lets you work on it offline while staying connected to the original online version.

 
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    A repository (repo) is where a project’s files and history are stored. It can be on GitHub (online) or on your computer (offline) if you clone it.
```


- What is a **commit**? Why does it need a commit message?

```
    A commit saves changes you made to a project. The commit message explains what you changed so you (and others) can understand the updates later.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
   Pushing your code means sending your saved changes from your computer to GitHub. This keeps the online version updated with your latest work.
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
     Pulling before pushing makes sure you have the latest updates from the main repository.  
    If someone else made changes, pulling helps you avoid conflicts when you push your own changes.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
     The number of branches can be found by clicking on the "Branches" section of the repository. If I see my branch, it means my changes have been pushed successfully, and i also see others.
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
     Yes, they are different. My branch contains the new changes I made, while the master branch does not have them yet.  
    This shows that my work is separate from the main project until it is merged.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
      When I switch to the master branch, my new file (or changes) disappears because the master branch does not have them yet.  
    This confirms that each branch maintains its own version of the project.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    When I switch back to my branch, my file (or changes) reappears.  
    This proves that branching allows multiple versions of a project to exist at the same time without interfering with each other.  
    It is useful for working on features separately before merging them into the main project.
```

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will do our best to answer them. Paste the link to your question in Slack here:

```
     https://bereacs.slack.com/archives/C3QACGH8R/p1738730623065289
```

---