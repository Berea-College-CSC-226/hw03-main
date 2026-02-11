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
    a. #800080
    b. rgb (128, 0, 128) ~ 128 red, 0 green, 128 blue
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    a. #A52A2A 
    b. rgb (165, 42, 42) ~ 165 red, 42 green, 42 blue
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    not found
```

_Return to the Google Doc to continue this assignment._

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
    turtle.pos()
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    turtle.speed(0)
```

2.d. How would you change the turtle's color to xanadu? 

```
    turtle.color(#738678)  - using xandu hex color from ColorHexa
```

2.e. How would you fill a shape with the color xanadu?

```
    turtle.fillcolor(#738678)
    turtle.begin_fill
    turtle.end_fill()
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    Making a copy of the project, but now it is considered your own personal 
    copy you may utilize to make any changes. It is important to not touch the main.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    Similar to a Google Doc, a repository stores all coding history so that 
    all files and history are stored safely. Additionally, they exist on both Github
    and the computer to which it was cloned on. 
```


- What is a **commit**? Why does it need a commit message?

```
    A commit is making sure that your code was saved. Similar (if not the exact same concept) 
    of hitting CTRL + S or Command S when saving the changes of a document. 
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    Pushing means you're 'pushing' the changes you made on your copy to the github repository.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    We should always pull before push because this makes sure that our code is up to date with 
    the changes we have most recently made and these changes help us ensure there are no merge conflicts
    with other students who may have access to the same repository.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    Generally speaking, a repository can have as many branches. As for this HW03, there is the main 
    branch WHICH NO ONE SHOULD TOUCH and there are also other students' branches which can be seen on 
    Github. (I think)
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    Absolutely. The master branch is the original and my branch is a copy with my own changes.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    Yes. As mentioned before, it's important to note that the MAIN branch are completely different from
    mine. This is because the changes I make only exist on my file. Anything beyond that are not my own.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    Yes, my file is back! Branches helps swes work on differnt features without interfereing with eachother's work.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will answer them for everyone! Paste the link to your question in Slack here:

```
    Do all of the web developers for Berea College use branches? Is there any specific website that only one person created? 
```

---