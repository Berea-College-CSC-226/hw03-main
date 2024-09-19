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
 R (Red): 128  G (Green): 0    B (Blue): 128
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
  R (Red): 165    G (Green): 42      B (Blue): 42
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
  R (Red): 115    G (Green): 133     B (Blue): 122
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
    turtle.speed(0)
```

2.d. How would you change the turtle's color to xanadu? 

```
    We can use the turtle.color() method and then give the RGB values for Xanadu. 
```

2.e. How would you fill a shape with the color xanadu?

```
    We need to use the begin_fill() and end_fill() methods around the drawing commands.
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    Cloning a repo means creating a local copy of a remote repository on our computer.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    A repository is a storage location for project’s files, including code, documentation, and history of changes.
    It exists on the local machine and on the remote server like GitHub.
```


- What is a **commit**? Why does it need a commit message?

```
    A commit is a snapshot of changes in a repository. It records modifications to files and their history.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
   Pushing the code means uploading the local changes to a remote repository. The code is pushed from the local machine to a remote server.
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    It's important to pull before we push to make sure that the repository is updated with the remote repository. 
    This prevents from conflicts by integrating any changes made by others before we upload our own changes.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    Yes, there are branches that are made by other students and I see mine there too. 
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    I see my branch and the master branch which is not identical to my branch.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    Yes. I checked out the branch and this updates the working directory with the file's current version from the repository, which allows me to make changes and commit them later.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
   Branching is useful because it enables us to work on different features or fixes independently 
   without affecting the main codebase.
```

---

## SECTION 5
- A lot happened in this assignment, and often, you do things without fully 
  understanding them. Your last task is to formulate a question and ask it. 
  To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the instructor 
  will do our best to answer them. Paste the link to your question in Slack here:

```
    My question is that when we create multiple branches in one repo, then when we push and commit it, are all the
branches being pushed to the local or just the most recent one? If just one is pushed, what happens to the other ones?
Also, another question of mine is how to compress my codes in a more efficient form since more of the codes are very long
and it can take a lot of time, as it did for me.





```