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
    R: 128
G: 0
B: 128
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
 R: 165
G: 42
B: 42
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
  turtle.color(115, 134, 120)
```

2.e. How would you fill a shape with the color xanadu?

```
turtle.begin_fill()
turtle.color(115, 134, 120)
#shape 
turtle.end_fill()
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    creating a local copy of a repository from GitHub
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
     storage location for project files and version history. It exists both on GitHub  and on local machine 
     after cloning.
```


- What is a **commit**? Why does it need a commit message?

```
   a snapshot of changes in the repository. A commit message explains what changes were made
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
   uploading your local commits to the remote repository
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    Pulling before pushing ensures your local repo is up to date with the remote version, preventing conflicts.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    The number of branches depends on the repository. If my branch exists, I should see it along with any others.


```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    If changes were made in my branch but not in the master branch, they will be different. Otherwise, they will be the same.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    Checking out the master branch updates the project to match that branch. If my changes were only in my branch, they might disappear.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    Switching back to my branch restores my changes. Branching is useful for working on features separately without affecting the main project.
```

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will do our best to answer them. Paste the link to your question in Slack here:

```
   what are the best strategies for preventing and resolving conflicts when merging branches in Git?
```

---