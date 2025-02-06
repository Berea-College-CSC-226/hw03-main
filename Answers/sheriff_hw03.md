
-# Fully Functional Gitty Psychedelic Robotic Turtles

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
   R=152
   G=14
   B=168
   
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    R=110
    G=60
    B=11
   
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    R=114
   G=134
   B=120
   
   source: https://artincontext.org/xanadu-color/
```

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
   You can use fd() or backward(negative number)
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
    print(turtle.pos())
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    using the functon turtle.speed() and passing the value to 0.
```

2.d. How would you change the turtle's color to xanadu? 

```
   turtle.colormode(255)  to enable RGB mode
   turtle.pencolor(115, 134, 120)  to set pen color to Xanadu
```

2.e. How would you fill a shape with the color xanadu?

```
    turtle.colormode(255)  to enable RGB mode
   turtle.fillcolor(115, 134, 120)  to fill color to Xanadu
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    Cloning a repository means making a copy of a remote Git repository from GitHub onto your local machine. This 
    allows you to work on the project locally while keeping it linked to the remote repository for version control.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    A repository (repo) is a storage location for a software project, containing all the files, folders, and version
    history. And it exists on both the local machine and in GitHub.

```


- What is a **commit**? Why does it need a commit message?

```
    A commit is a saving order of changes made to a project. A commit message is important because it describes what
    changes were made and helps track the project's version history.  

```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    Pushing means uploading your local changes (commits) to the repository on GitHub. A code is pushed from the
    local computer to GitHub.
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    to get all the changes made on the project on your computer before pushing your own.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    I see 28 branches. I do see mine and others' branches.
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
   I see my file and all the committs I have done on my branch but not on the main branch.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
   My file was not in the project pane of pycharm. 
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    I see my file now after I switched back to my branch. Branching is useful because it allows developers to work on
    different features or fixes independently without affecting the main project. This ensures that experimental or 
    unfinished changes do not disrupt the main working code.
```

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will do our best to answer them. Paste the link to your question in Slack here:

```
    https://bereacs.slack.com/archives/C3QACGH8R/p1738803115529629
    
```

---