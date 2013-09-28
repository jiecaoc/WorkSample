OBJS = main.o Timer.o ControllableRobt.o Color.o Position.o Obstacle.o Clock.o World.o Object.o Goal.o Vector.o MovableObj.o Interpreter.o RectObstacle.o
CC = g++
DEBUG = -g
CFLAGS = -Wall -c $(DEBUG)
LFLAGS = -Wall $(DEBUG)

all : gorobot convert2readable
convert2readable : convert2readable.cpp Command.h Command.cpp
	$(CC) convert2readable.cpp Command.h Command.cpp -o convert2readable 
gorobot : $(OBJS)
	$(CC) $(LFAGS) $(OBJS) -o gorobot -lglut -lGL -lGLU -pthread -lm
main.o : main.cpp Robot.h Obstacle.h Clock.h World.h const.h Goal.h Interpreter.h environment.txt
	$(CC) $(CFLAGS) main.cpp ControllableRobt.h Obstacle.h Clock.h World.h const.h Goal.h Interpreter.h 

World.o : World.h World.cpp ControllableRobt.h Goal.h Command.h RectObstacle.h MovableObj.h Position.h Vector.h
	$(CC) $(CFLAGS) World.h World.cpp  Goal.h Command.h RectObstacle.h MovableObj.h Position.h Vector.h

Interpreter.o : Interpreter.h Interpreter.cpp Command.h World.h
	$(CC) $(CFLAGS) Interpreter.h Interpreter.cpp Command.h World.h


Command.o : Command.h Command.cpp
	$(CC) $(CFLAGS) Command.h Command.cpp

RectObstacle.o : RectObstacle.h RectObstacle.cpp Obstacle.h Position.h
	$(CC) $(CFLAGS) RectObstacle.h RectObstacle.cpp Obstacle.h Position.h

Goal.o : Goal.h Goal.cpp MovableObj.h 
	$(CC) $(CFLAGS) Goal.h Goal.cpp MovableObj.h
Object.o : Object.h Object.cpp Position.h Color.h const.h
	$(CC) $(CFLAGS) Object.h Object.cpp Position.h Color.h const.h

Obstacle.o : Obstacle.h Obstacle.cpp Object.h
	$(CC) $(CFLAGS) Obstacle.h Object.h Obstacle.cpp

MovableObj.o : MovableObj.h MovableObj.cpp const.h Timer.h Color.h Position.h Object.h Vector.h 
	$(CC) $(CFLAGS) MovableObj.h Timer.h const.h Color.h MovableObj.cpp Object.h Vector.h


Clock.o : Clock.h Clock.cpp Timer.h Object.h const.h
	$(CC) $(CFLAGS) Clock.h Clock.cpp Timer.h Object.h const.h

Timer.o : Timer.h Timer.cpp
	$(CC) $(CFLAGS) Timer.h Timer.cpp

Color.o : Color.h Color.cpp
	$(CC) $(CFLAGS) Color.h Color.cpp

Robot.o : Robot.h Robot.cpp MovableObj.h
	$(CC) $(CFLAGS) Robot.h MovableObj.h Robot.cpp

ControllableRobt.o : ControllableRobt.h ControllableRobt.cpp MovableObj.h
	$(CC) $(CFLAGS) ControllableRobt.h ControllableRobt.cpp MovableObj.h

Position.o : Position.h Position.cpp
	$(CC) $(CFLAGS) Position.h Position.cpp

Vector.o : Vector.h Vector.cpp
	$(CC) $(CFLAGS) Vector.h Vector.cpp

# #=======================tests ===================

# tests : testrobot
# 	./testrobot

# CXXDIR=../bin/cxxtest
# # This rule will create an executable program to run the tests by linking the test-related object files together:
# testrobot: test.o Robot.o Timer.o Color.o Position.o Object.o Obstacle.o Goal.o Vector.o MovableObj.o
# 	g++ -I$(CXXDIR) -o testrobot test.o Color.o Object.o Position.o Robot.o Timer.o Obstacle.o Goal.o Vector.o MovableObj.o -lglut -lGL -lGLU -pthread -lm



# # This rule compiles .cpp files into .o files
# test.o : test.cpp Robot.h Position.h Object.h Vector.h
# 	g++ -I $(CXXDIR) -c Robot.h Position.h Object.h Vector.h test.cpp

# # This rule calls the perl scripts distributed with the cxxtest framework to auto-generate .cpp file(s) to run the tests that you have defined.
# test.cpp: robot_tests.h
# 	perl $(CXXDIR)/cxxtestgen.pl --error-printer -o test.cpp robot_tests.h





#========================clean and tar ==================

clean :
	rm -f *.o
	rm -f testrobot
	rm -f convert2readable
	rm -f gorobot
	rm -f test.cpp
	rm -f *~
	rm -f *.gch

tar :
	tar cfv robot.tar *.h *.cpp *.txt *.pdf
