This is the readme.txt file for iteration 4.

Creators:
	Jiecao Chen, jieca001@umn.edu

User ID: user128

Special Instructions for the TA (if any):

--------------How to operate this program-----------------
* Make sure your system has openGL lib!!
* run "make all", then gorobot and convert2readable will be produced
* you can write commands in "cmd" file (or any text file you like), 
  a sample may look like this:
  in file "cmd":
      moveBackward(10)
      stepSpeed(10)
      for 0 to 200 do
        moveForward(5)
	stepdirection(0.05)
      endfor
      moveForward(10)
* run the command "./gorobot < cmd", a graphical screen will appear,
  then press F2, commands in file "cmd" will be executed. 
  also you can press F1 to execute commands in "cmd" line by line
* there is another way to use this program : control the robot will keyboard 
  and output the corresponding commands.
  To do this, run the command in terminal "./gorobot -k > cmd"
  Then the same graphical screen will show up, you can now control the robot using
       F1 : move forward
       left : change direction of robot counter-clockwise 
       right: change direction of robot clockwise
       up : increase the speed (but there is limitation)
       down : decrease the speed
  After you finish and close the graphical screen, you can run "less cmd" to check the 
  commands that are printed, but they are too complex, so you can run 
  "./convert2readable cmd" to make code in file "cmd" more readable, run "less cmd"
  to check it.
  
  now, you can run "./gorobot < cmd" to repeat the movement that you just controlled through keyboard

---------------------------Enjoy it ^_^--------------------------------


------------------------------------------------------------------------------------

GENERAL OVERVIEW OF DESIGN :
A Interpreter class has been created to interpret string into Command class format.
And all those Commands will be pushed in to a deque structure.  Every time when the class World updateScreen, the top command in the command deque will be fetched and executed.
Every inputed command will be interpreted into several atomical commands, including:
      * moveForward() : float
      * stepDiretion(float signal) : float
      * stepSpeed(float delta) : void

Other design could be found in previous readme.txt, also, the most direct way to learn the design of the system is to read UML_Iteration4.png



REQUIREMENTS: 
All requirements I have promised in my Letter_of_intent.pdf have been met.

