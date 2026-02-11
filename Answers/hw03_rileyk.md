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
    Replace this text with your answer
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    128, 0, 128
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    115, 134, 120
```

_Return to the Google Doc to continue this assignment._

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    'turtle.fd()'
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
    'turtle.pos()'
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    'turtle.speed(0)'
```

2.d. How would you change the turtle's color to xanadu? 

```
    'turtle.color(115, 134, 120, /)'
```

2.e. How would you fill a shape with the color xanadu?

```
    'turtle.fillcolor((115, 134, 120))'
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    It means that it clones all of the code from the repo in the github server
    to your device locally so you can have your own version and upload edits
    as needed.
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    The repository is on the github servers, but if you clone it, it is put on
    your local machine.
```


- What is a **commit**? Why does it need a commit message?

```
    A commit is a marker of a milestone in your code. Every time you commmit
    it saves that version of the code so if you need to go back to that version
    for whatever reason you can.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    When you 'push' it pushes the commit you made from your local machine to
    the repo on github's server.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    Because if you don't then it will cause a merge conflict due to your local
    version of main being out of sync with the main in the github server.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    There are 24 branches; I do see mmine as well many others from previous classses
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    Yes they are different because I have edited things and added some files in my branch but
    main stays the same as when I first cloned the repo
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    Yes, my files are no longer there and it is just showing the original state of the repo
    because all of my changes were on a branch and had no affect on the main
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    Branching is useful because you can make your own branch of the repo which includes
    all of the same files that main has but you can edit them now without it affecting main.
    But now if you make some changes that you thing should be included in the main branch you
    must create a pull request for it to be included.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will answer them for everyone! Paste the link to your question in Slack here:

```
    Do huge tech companies like Google, Facebook, etc. really use Github and Git? Or do they use similar
    programs that maybe they programmed themselves to work better for their needs specifically?
```

---