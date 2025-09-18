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
    rgb(128, 0, 128)
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    rgb(165, 42, 42)
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    This is a returning a "Invalid hex color format" because "xanadu" isn't a color in their library
    but searching what hex color format "Xanadu" is it's able to give me "rgb(115, 134, 120)" for the a muted green (#738678) which
    what xanadu is.

```

_Return to the Google Doc to continue this assignment._

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    You could also input "fd()" instead.
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
    You can type in "turtle.pos() or turtle.position() to tell where the turtle's current state is.
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    turtle.speed(0) 
    “fast”: 10
    “normal”: 6
    “slow”: 3
    “slowest”: 1
```

2.d. How would you change the turtle's color to xanadu? 

```
    turtle.color(#738678)
```

2.e. How would you fill a shape with the color xanadu?

```
    Depending on your shape, you could start on a turtle.begin_fill() and once you're done drawing
    your shape you can turtle.end_fill() which would fill in the shape it drew with the color you stated before hand.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    You're making a local copy of the project/files into your computer that allows you to make your own changes.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    A repository is a storage location that includes your files, work, and the software packages. When you're making a clone repository of a file, for example 
    the classroom git is located in the Remote Repository but when you clone it onto your computer, it would be in the local repository. So they're both located in Github, just ogranized differently. 
```


- What is a **commit**? Why does it need a commit message?

```
    Commit is a button that helps you save the changes you've made in your code. Leaving a commit message let's you know what changes you made for that specific commit
    which makes it easier to go back and refine/find which specific code change/version you're looking for.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    Once you've finish making your changes and commiting your new updated code, you would need to push these new updates to the main branch that holds your whole code (Github)
    which then allows whoever is a collaborator see these new changes and can pull these new changes into their computer or branch. 
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    I think it's important to pull because there could be new changes and your file isn't up to date which could
    cause conflicts. If you push without pulling you're not making sure your files are the same.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    I believe I only see my files (hw03_manabatl3_galaxy.py , hw03_manabatl3.md) unless I go on the 
    Github website and see my other classmates branches.
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    Yes, they are different. My branch only has my edits and files.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    It changes because the main doesn't hold my files but my branch does. 
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    Yes it is because it's my branch that I created and inputed the files/work. Which again shows 
    how branching works and organizes people's work within their own branhc.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will answer them for everyone! Paste the link to your question in Slack here:

```
    Is there a way to indicate if we did our pull requests right, and if so, 
    how could we fix them if there was an issue? 
```

---