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
The RGB values for the color purple I created are R: 128, G: 0, B: 128.
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
The RGB values for the color brown I created are R: 165, G: 42, B: 42.
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
The RGB values for the color xanadu I created are R: 115, G: 134, B: 120.
```

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
Besides `turtle.forward()`, the `turtle.fd()` command can also be used to move the turtle forward.
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
The `turtle.position()` or `turtle.pos()` command can be used to print the turtle's current location.
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
To set the turtle's speed to maximum, I can use `turtle.speed('fastest')` or `turtle.speed(0)`.
```

2.d. How would you change the turtle's color to xanadu? 

```
 I would change the turtle's color to xanadu by using the command `turtle.color((115, 134, 120))` after setting `screen.colormode(255)`.
```

2.e. How would you fill a shape with the color xanadu?

```
To fill a shape with the color xanadu, I would first use `turtle.fillcolor((115, 134, 120))` to set the fill color, then start the fill with `turtle.begin_fill()`, draw the shape, and complete with `turtle.end_fill()`.
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
Cloning the repo means making a copy of the entire repository from GitHub onto my local machine so that I have all the files and their history available locally.

```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
The repository is a storage space where all the files related to a project are kept along with their version history. It exists both on GitHub (remote repository) and on my local machine once I clone it.
```


- What is a **commit**? Why does it need a commit message?

```
A commit is a record of changes made to the repository's files. The commit message is necessary because it provides a description of the changes for future reference, making it easier to understand the purpose of the changes when reviewing the project history.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
To push code means to send my local repository changes to the remote repository on GitHub. This updates the remote with my latest changes.
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
It's important to pull before you push to ensure that I have the latest changes from the remote repository. This helps prevent merge conflicts and keeps the project up-to-date with all team members' contributions.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
 There are several branches in the repository. I see my branch named `clarkk2` and other branches from my classmates.
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
 Yes, they are different. My branch has the latest changes I've made, which haven't been merged into the master branch yet.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
When I checkout the master branch, my file reflects the state of the files in the master branch, which may not include the latest changes I made in my branch.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
 Yes, my file is back with all my recent changes. Branching is useful because it allows me to work on my updates independently without affecting the master branch until I'm ready to merge my changes.
```

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will do our best to answer them. Paste the link to your question in Slack here:

```

```

---