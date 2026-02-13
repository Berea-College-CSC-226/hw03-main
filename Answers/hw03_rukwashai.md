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
   To create a good purple color we had :"rgb(128, 0, 128)"
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
    To create a good brown color we have :"rgb(165, 42, 42)"
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values?

```
    I couldn't find the value of this color on the website you provide, but I found it on 
    Google and it is :"RGB Values: 115, 134, 120"
```

_Return to the Google Doc to continue this assignment._

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    We can still code Alex=turtle.Turtle()
    Alex.forward() or we can do turtle.fd()

```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
    To print the position of the Turtle we can say : turtle.position()
or we can put turtle.pos() it will return Return the turtle’s current location (x,y) (as a Vec2D vector).
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    we can set the speed by coding: turtle.speed(x) If input is a number 
    greater than 10 or smaller than 0.5, speed is set to 0. 
    Speedstrings are mapped to speedvalue
```

2.d. How would you change the turtle's color to xanadu? 

```
   To change the turtle's color you can code : turtle.color(rgb(115, 134, 120)) I am not thag
   sure but I am going to give another alternative so we can still do turtle.color("xanadu")
   but as we don't have the that name in the system we can take it value 
   which is turtle.color("#738678")
```

2.e. How would you fill a shape with the color xanadu?

```
    to fill the shape you can do turtle.fillcolor("#738678") then when you want to fill you code
    turtle.begin_fill()

```

_Return to the Google Doc to continue this assignment._

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
    That means you create a local copy of the work, which can allow you to make change without changing the original
    work yet
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    repo is a space where you can put your code it's store in you file and on github it is 
    copy of your project stored on the interne
```


- What is a **commit**? Why does it need a commit message?

```
    It need a message which helps to remember what change you made on you project especially when you're working in a team
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
    so push mean you send it to github so that it can reflect there, you push it from your local storage to the online 
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    what I have learned so far, it is important to pull before we push for avoinding merge conflict
    especially when you are working in a team.
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    You maight see your branch your created and the one for you teamate if you are working under the same main
    
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    The difference is that your local branch may have update that master may not have until you pull reques
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch. Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
    As long as you did not commit the work, all you're change won't be reflected in main 
    in fact if you do push the information may be there but deleted 
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    Branching is useful to avoid deleting each other work, but alse keeping on track with the work 
    without losing what you have worked on.
```

_Return to the Google Doc to continue this assignment._

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will answer them for everyone! Paste the link to your question in Slack here:

```
    So I would like to know if I get this right let me summurize the process, we clone, we create a branch,
    we work in the branch, we pull, we push, and when we want to merge with main, we pull request ?
```

---