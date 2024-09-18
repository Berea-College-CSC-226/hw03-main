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
R:255 G:0 B:239
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    R:142 G:85 B:0
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    R:71 G:226 B:167
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
    turtle.position() / turtle.pos()
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    turtle.speed("fastest")
```

2.d. How would you change the turtle's color to xanadu? 

```
    screen.colormode(255)
    turtle.color(71,226,167)
```

2.e. How would you fill a shape with the color xanadu?

```
    screen.colormode(255)
    turtle.fillcolor(71,226,167)
    turtle.begin_fill()
    #draw shape
    turtle.end_fill()
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
Making a copy of it on your machine
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
The repository is where all the code and related files reside. It originally exists in Github, but
can also be copied onto your local machine
```


- What is a **commit**? Why does it need a commit message?

```
A commit is a sort of "Save point" [https://www.geeksforgeeks.org/committing-in-git/]
And a commit message is needed to differentiate one save point from another and actually make commits useful
by allowing quick access to a previous version of a project
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
One way of looking at pushing code is as publishing or updating [https://github.com/git-guides/git-push]
The code is being pushed from your local machine to Github.
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
The only reason I can think of without looking it up is that it splits the resolving of 
merge conflicts into two parts instead of one big merge-conflict-resolving seshion.
The first part being when you pull: here you resolve merge conflicts from other contributors' 
contributions and seeing if anything they did will break what you just did, before your code
ever gets implemented.
The second part being when you push: here you resolve merge conflicts dervied from the feature you're 
actually integrating. 
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
Lots, over 30 in remote. I see mine there as well as my classmates' branches
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
Yes, my files are not in master yet because my pull request has not been approved yet
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
It is not there, since master doesn't have my changes merged into it yet.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
Yes, my file is back. Branching is useful since you can experiment as much as you want with no
risk of breaking code for everyone else besides yourself
```

---

## SECTION 5
- A lot happened in this assignment, and often, you do things without fully 
  understanding them. Your last task is to formulate a question and ask it. 
  To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the instructor 
  will do our best to answer them. Paste the link to your question in Slack here:

```
    https://bereacs.slack.com/archives/C3QACGH8R/p1726700540054349
```



