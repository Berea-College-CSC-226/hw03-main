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
    R = 128, G = 0, B = 128
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    R = 165, G = 42, B = 42
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    There's no such color as "xanadu" among the colors on the given website. Initially I thought
    that there was a typo in the name of the color, but I looked it up, and this color actually
    exists. Here are its RGB values: 
    
    R = 115, G = 134, B = 120
    
    This time I used the website below to answer this question: 
    https://www.figma.com/colors/xanadu/  
```

_Return to the Google Doc to continue this assignment._

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    Turns out that we can use the turtle.fd() function instead of turtle.forward(), and 
    both methods do the same thing!
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
    To find the turtle's current location, we can use turtle.position() or turtle.pos().
    It will return two values: the x and y coordinates. If you want to print these two values, 
    you can do this: print(turtle.position()) or print(turtle.pos()).
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    To set the turtle's spped to maximum speed, we use turtle.speed(0)
```

2.d. How would you change the turtle's color to xanadu? 

```
    To change turtle's color to xanadu, we have to make two steps. First of all,
    we have to set the screen colormode to 255 (so we can use RGB values to set the 
    turtle's color): 
    
    screen.colormode(255)
    
    Then we use the following method: 
    
    turtle.color(115, 134, 120)
    
    I forgot the method above, so to answer the question, I looked up in the 
    Python documentation: https://docs.python.org/3/library/turtle.html#turtle.color
```

2.e. How would you fill a shape with the color xanadu?

```
    First, we set the fill color: 
    
    turtle.fillcolor(115, 134, 120) 
    
    Then we begin filling the shape we are about to draw: 
    
    turtle.begin_fill()
    
    Then we outline the shape, and use another method at the end: 
    
    turtle.fillcolor(115, 134, 120)
    
    Once again, I conculted the Python documentation to answer the question: 
    https://docs.python.org/3/library/turtle.html#turtle.color
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    Cloning the repo means creating its copy on your own local drive. 
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    A repo is a project Git tracks the files and folders of. It might exist both on our local drive 
    and GitHub.  
```


- What is a **commit**? Why does it need a commit message?

```
    A commit is capturing (all or some of) the changes you have made to the files in the repo. Just like,
    you take photos to capture memorable moments, developers commit changes to be able to go back to those 
    changes for various reasons. 
    
    We need to write commit messages so that we and other developers can understand what changes have been
    made to the project at a certain commit.  
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    Pushing code means uploading it from your local drive into the cloud (usually GitHub, but it might any 
    online service that hosts git repos). 
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    Pulling before pushing is a safety feature that prevents us from merge conflicts (it decreases 
    the chance of getting a conflict of this kind). 
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    There are 38 branches in the repo at the moment I'm writing the answer, and the 
    number is always increasing as more and more people push their branches up into the GitHub
    server. And as I said earlier, there are not only my branches, but also branches of other 
    CSC 226 students.
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    These branches are different since the main branch is supposed to be emptier. That's because this branch 
    should be a starting point for every student that does homework 03. Nonetheless, I saw some students 
    adding their files into the main branch.  
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    All of the file that I previously created on my branch (hw03_kurasova.md, kfc.png, flowers.png, 
    hw03_kurasova.py) disappear when I checkout to the main branch. 
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    All of my created files reappear once I checkout to my branch. 
    
    Branching is what I would call "the best of both worlds" because it allows us to work together
    and also void code conflicts/rewriting. 
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will answer them for everyone! Paste the link to your question in Slack here:

```
    Hello. I'm a little confused about homework 3. I read in the group chat that there should be 2 branches (besides the main/master branch)
    and some merge conflicts occurring while doing this assignment. However, I have only created one branch, where I have put
    all of my files and the answers to all the questions. Also, I didn't get any merge conflict and already made a pull request.
    Is it OK that I did the homework the way I did?
    
    https://bereacs.slack.com/archives/C3QACGH8R/p1770737691525429
```

---