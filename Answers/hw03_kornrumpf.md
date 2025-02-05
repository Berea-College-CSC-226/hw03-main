# Fully Functional Gitty Psychedelic Robotic Turtles

"""## Instructions

**_<span style="color:red">
    VERY IMPORTANT: Make a copy of this file. DO NOT EDIT IT DIRECTLY!
</span>_**

#1. Make a copy of this file by selecting the file and hitting CTRL+C. 
#2. Paste your copy into the `Answers` folder.
#3. Name the file `hw03_username.md` replacing `username` with your username.
#4. Replace each `Replace this text with your answer` with your answer to the question above it.
===================== COMPLETE ==============================================================
""" 
## SECTION 1

1.a. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color purple. 
     What are the R, G, and B values?

```
    The color purple is created using values: [R,G,B] == [205,0,255] 
```

1.b. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color brown. 
     What are the R, G, and B values? 

```
     The color brown is created using values: [R,G,B] == [142,80,9] 
```

1.c. Using the [RGB Color Wheel tool](https://colorspire.com/rgb-color-wheel/), create the color xanadu. 
     What are the R, G, and B values? 

```
    The RGB is 115, 134, 120. This is also represented as a hexidecimal value of
     #738678
     
```

---

### SECTION 2

2.a. Explore the turtle library documentation and find the description for the 
     `forward()` method. What alternate command can be used to move the turtle forward, 
     besides the `turtle.forward()` command you are used to using?

```
    turtle.fd() can also be used to move the turtle forward.
```

2.b. What command from the turtle library can be used to print the turtle's current 
   location?
   
```
    The .position() method - returns the turtle's current location.
```

2.c. How do you set the turtle's speed to maximum speed?
   
```
    Because the .speed() method only accepts parameters within the range of [0,10] my
    first thought was that an input of 10 would produce the MAX speed, but 0 is described
    as the "fastest".
```

2.d. How would you change the turtle's color to xanadu? 

```
    wn.bgcolor("#738678")
    
    Attempted to pass hexidecimal input to the method, but failed
    bad color argument: wn.bgcolor(#738678). Also attempted to pass string input, but
    this also failed. wn.bgcolor("xanadux"). I also attempted to follow the documentation
    about this and used wn.bgcolor("#738678"), but this too failed. For some reason,
    wn.bgcolor("red") also failed!? Assuming there was a cache related error, I restarted the application
    and my system, only to realize the problem was related to the position of the method.
    It needed to be IN-FRONT-OF the exitonclick() eventHandler!
```

2.e. How would you fill a shape with the color xanadu?

```
    This question is a bit unclear. Do you mean - modify the shape of the turtle object 
    and then fill the color as xanadu, or do you mean - draw a shape using the turtles 
    movements and then fill that completed shape as the color xanadu?
    
   CITATION PROMPT TO CHATGPT:
    
   INPUT:

   2.e. How would you fill a shape with the color xanadu?

    This question is a bit unclear. Do you mean - modify the shape of the turtle object 
    and then fill the color as xanadu, or do you mean - draw a shape using the turtles 
    movements and then fill that completed shape as the color xanadu?  
    
    OUTPUT: (Summary)
    ChatGPT did provide a loop, but when I tried to incorporate into my code, it failed. 
    Though once I re-incorporated the code into a new Python file, it did do precisely
    what I needed to - draw and fill a pentagon with the color xanadu. The working code is
    below.
    
import turtle

t = turtle.Turtle()

# Set fill color to xanadu
t.fillcolor("#738678")  # Hex code for xanadu

# Draw and fill a shape
t.begin_fill()
for _ in range(5):  # Draw a pentagon
    t.forward(100)
    t.left(72)
t.end_fill()

turtle.done()

    
    
```

---

## SECTION 3

3.a. What does **cloning** the repo mean?

```
   Cloning the repository in the first step a student is taking in order to get all the files associated with a project.
   To do it, simply select [Clone Repository] on the home screen of PyCharm and insert a URL. 
   Once that is completed using Git Versioning control, the files in the repository will be installed into a Trusted
     Folder onto the localhost. C:\Users\<localhost>\PycharmProjects. This folder is added to an exclusion list for
     Microsoft Defender. Within PyCharm there is then a quick dependency check as well. 
   
```


- What is the **repository**? Where does it exist (on your local machine or in Github)?

```
    Margaret Rouse with Techopedia defines a (software) repository as a central place to keep resources that users can 
    pull when needed. These offer remote access to code modules and packages. Once the cloning process is complete
    the files in that repository will be on the local machine, though they do also remain stored in GitHub.
```


- What is a **commit**? Why does it need a commit message?

```
    A commit is used for: tagging changes, and revisions to a document. These are similar to break points 
    where programmers can create a type of restore point. For instance, if I have a project, and I have 
    completed a "section" then I can commit 'A'. I will then do further work, and commit 'B'. If something goes wrong, 
    or I want to retrace my steps, I can roll back to the previous commit 'A'. These should be quality commit messages
    for richer context.
```


- What does it mean to **push** your code? Where is your code being pushed _to_ and _from_?

```
To Push causes PyCharm to write the python files to GitHubs Servers, from the localhost.
```

---

## SECTION 4

## Pull Master Into Your Local

4.a. Why do you think it is important to pull before you push?

```
    Cloning appears to be the inital pull request from GitHub. Further pull requests should be done in the
    context of pair programming. For example: if two people are working on a GitHub repository that they have
    both cloned. Then person 1 make a change, commits and pushes the code back to GitHub. Person 2 will then need
    to perform a pull of the code, before pushing any changes they make. Another reason to 
    perform a pull request is to check if other people on your team made changes.
    
    Pull requests are also used as a way to request that your code in incoporated into the master branch.
    
```

4.b. How many branches are in the repository?
     Click the link to look at the branches. Do you see yours? Do you see any others? 

```
    There are some distinct categories of branches, local and remote.
    In Local:
          hw_03_kornrumpf
          main
          
    In Remote:
          main
          fix_a03_stubs
          Spring-2024
          
I am unclear about the remote branches.
```


4.c. Compare your branch and the master branch by clicking on each. Are they different?

```
    I don't see much difference between my branch and the master branch. 
    The Project files window remains unchanged between branches, and the only
    difference is that I lose access to my workspace, which included the .md file
    i'm currently working in.
```


4.d. Go back to PyCharm, and go back to the Branches interface from before. Checkout the 
     master branch.
     Describe what happens to your file in the Project pane of PyCharm. Is it still 
     there? Did it change?

```
   Within this project I see a 'main' branch. When I check it out, I no longer
   see my hw03_kornrumpf.md file, or another of the other files I've created.
```


4.e. Now go back to your branch in PyCharm. Is your file back? Based on your observations
     here, describe how branching is useful:

```
    Switching back to my branch, I am able to see the files I had open. PyCharm
    goes onto to describe that what's happening is that a workspace is restored.
    This includes: specific run configurations, open files, and breakpoints.
```

---

## SECTION 5

A lot happened in this assignment, and often, you do things without fully understanding them. Your last task is to 
formulate a question and ask it. To do this, put your question into the [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and the TAs and the 
instructor will do our best to answer them. Paste the link to your question in Slack here:

```
There seems to be an error in the documentation of the library.
REF: https://docs.python.org/3.13/library/turtle.html , 
"Methods, of course, have the additional first argument self which is omitted here."
SUMMARY: What is the disntiction between an argument and a parameter?
THREAD LINK: https://bereacs.slack.com/archives/C3QACGH8R/p1738416378066409

Hi,
I was reading documentation about the Turtle module, and this distinction struck me, as another layer of separation between functions and modules.
"In the following documentation the argument list for functions is given. Methods, of course, have the additional first argument self which is omitted here."
I am a bit confused by the wording on these sentences:
The argument list for functions is given (but the documentation doesn't give a clear list of argument for each "function").
Methods, of course, have the additional first argument self which is omitted here.
The index that follows starts with the header Turtle Method and then prints out [METHOD??? // FUNCTIONS ?? # I'm leaning towards methods based on the header, and the prompt in section 2,  questions 2.a.] such as:
     forward()
     backward() (edited) 
     
I think I have some more clarity on this. It seems that that particular blurb in the documentation is not exactly correct. As I looked further into the .forward() method, the methods PARAMETERS were described.
I also recalled there to be a strong distinction between local scope AND global scope; input parameters; arguments.

@heggens Could I get copy of the cyclical-type whiteboard illustration you had created in class?

Further clarifying, within the documentation on the .speed() method, there was another contextual remark about arguments and parameters.
Though, I think the way it is described may have been more confusing!
turtle.Speed()
Parameters: speed = an integer between 0...10
Set the turtles speeds using an integer. (This is where I have some confusion):
     "if no argument is given, return current speed).


```

---