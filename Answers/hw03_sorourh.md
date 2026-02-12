# Fully Functional Gitty Psychedelic Robotic Turtles

## Instructions

1. In the top right of Pycharm, change the display of this file to 
   `Editor and Preview` mode, so you can see the code (markdown) and the rendered output. 

![Screenshot of "Editor and Preview" mode](split_mode_markdown.png)

The next line should appear red in the `Preview` mode on the right:

**_<span style="color:red">
    VERY IMPORTANT: Make a copy of this file. DO NOT EDIT IT DIRECTLY!
</span>_**

2. Make a copy of this file by selecting the file and hitting CTRL+C. 
3. Paste your copy into the `Answers` folder.
4. Rename the file to `hw03_username.md` replacing `username` with your username.

_Return to the Google Doc to continue this assignment._

---

## SECTION 1

Replace each `Replace this text with your answer` with your answer to the question above it.

1.a. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color purple. 
     What are the R, G, and B values?

```
    rgb(130, 0, 129)
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    rgb(165, 42, 42)
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    rgb(115, 134, 120)
```

_Return to the Google Doc to continue this assignment._

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
    turtle.position()
 ```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    turtle.speed(0)
```

2.d. How would you change the turtle's color to xanadu? 

```
    wn = turtle.Screen()
    wn.colormode(255)
    turtle.color(115, 134, 120)
```

2.e. How would you fill a shape with the color xanadu?

```
    wn = turtle.Screen()
    wn.colormode(255)
    turtle.color(115, 134, 120)
    turtle.begin_fill()
    turtle.circle(50) # example shape
    turtle.end_fill()
    
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    Cloning a repo means creating a local copy of a remote repository on your personal computer.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    A repository is a location in which you store all of your project's files and history and it exists remotely on Github and locally on your personal machine
```


- What is a **commit**? Why does it need a commit message?

```
    A commit is a snapshot of the work done at a specific point, acting as a save point that records everything added and removed to your files from the last commit.
    Commit messages are important because they describe what are the changes and why they were made. Furthermore, it make sit easier to track bugs and errors. Moreover, it helps the person looking over your code know what exactly you did.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    Pushing your code means uploading the commits you have made in your local repository to remote repository, synchronizing the versions together.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    It is important to pull before you push as it is  good practice. It makes sure your repository is up to date with the latest changes from the remote repo. 
    Pushing before pulling can result in merge conflicts and overlapping code that can result in your code being modified or deleted, which is not desired.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    Since I pulled changes in main in my branch in this current state. I see 45 branches from current students and previous students who took the class. I see mine and see all of the branches.
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    Yes, they are different. The master branch contains all the accepted work from current and previous students that has been merged. 
    My branch contains my own files and changes that haven't been merged into master yet.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    My files disappeared as they are not part of the main branch yet.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    My files are back.
    Branching is useful because it allows multiple people to work on different things simultaneously, allowing experimentations and code review 
    and keeps the project organized.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will answer them for everyone! Paste the link to your question in Slack here:

```
I understand the basic Git workflow, but I'm confused about having two developers working on the same code. In the current teamwork, we have "chunks" we can code in together, but the number of lines will change due to the large number of lines per function. How does GitHub identify the different chunks? 
```

---