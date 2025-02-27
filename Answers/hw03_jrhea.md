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
   R:160 G:32 B:240
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    R:150 G:75 B:0
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    R:115 G:134 B:120
```

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    t.backward() with a negative value
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
   t.stamp
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    t.speed(10)
```

2.d. How would you change the turtle's color to xanadu? 

```
    t.pencolor((115, 134, 120))
```

2.e. How would you fill a shape with the color xanadu?

```
    t.fillcolor((115, 134, 120))
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    you are making a copy of the repository from Github, on your computer or laptop
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    the repository is a file or group of files stored somewhere, in our case Github. 
```


- What is a **commit**? Why does it need a commit message?

```
    a commit is like a save that, well, saves your code. it needs a message because other people who are working in 
    the same repository and the owner of the repository can see what you've done before merging
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    a push is taking your code and moving it from your local repository and putting it a section of the main repository.
    from your computer to Github
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    to make sure your local repository is updated and anything you push is not going to conflict
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    my branch and main
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    yes, my branch has all my code, i have to submit a pr to merge my branch into main
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    it transferred all of my code to the main branch and put me in the main branch
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    yes, when you need to change priority on what code takes priority
```

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will do our best to answer them. Paste the link to your question in Slack here:

```
   is turtles useful anywhere outside of class?
```

---