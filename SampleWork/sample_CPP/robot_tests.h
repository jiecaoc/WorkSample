/*
  robot_test.h by H & J.C.
*/

#ifndef _ROBOT_TEST_H_
#define _ROBOT_TEST_H_
#include "cxxtest/TestSuite.h"
#include "Position.h"
#include "Robot.h" 
#include "Object.h"
#include "const.h"
#include "Goal.h"
#include "Obstacle.h"
#include "Vector.h"
#include "MovableObj.h"
#include <cmath>
#include <iostream>
using namespace std;
/* for robot test  */
const int windowX = 500;
const int windowY = 300;
 
// Test class Position
class PositionTests : public CxxTest::TestSuite
{
public:
    void Test_class_Position(void){
        Position test1(windowX / 2.0f, windowY / 2.0f);
        TS_ASSERT_EQUALS(test1.getPositionX(), windowX/2.0f);
        TS_TRACE("TEST test +getPositionX() SUCCESS");
        TS_ASSERT_EQUALS(test1.getPositionY(), windowY/2.0f);
        TS_TRACE("TEST test +getPositionY() SUCCESS");
    }
};



// Test class Object
class ObjectTests : public CxxTest::TestSuite
{
public:
    void Test_setColor(void){
        Object object_test_1;
        Color test_color;
        TS_ASSERT_THROWS_NOTHING(
            object_test_1.setColor(test_color.red, test_color.green, test_color.blue));
        TS_ASSERT_EQUALS(object_test_1.color.red, test_color.red);
        TS_ASSERT_EQUALS(object_test_1.color.green, test_color.green);
        TS_ASSERT_EQUALS(object_test_1.color.blue, test_color.blue);
        TS_TRACE("TEST test +setColor() initialize value SUCCESS");
        
        TS_ASSERT_THROWS_NOTHING(test_color.setColor(0.0f, 0.0f, 0.1f));
        TS_ASSERT_THROWS_NOTHING(
            object_test_1.setColor(test_color.red, test_color.green, test_color.blue));
        TS_ASSERT_EQUALS(object_test_1.color.red, test_color.red);
        TS_ASSERT_EQUALS(object_test_1.color.green, test_color.green);
        TS_ASSERT_EQUALS(object_test_1.color.blue, test_color.blue);
        TS_TRACE("TEST 001 test +setColor() change color SUCCESS");
        TS_ASSERT_THROWS_NOTHING(object_test_1.color.setColor(-1.0f, -1.0f, -1.0f));
        TS_ASSERT_EQUALS(object_test_1.color.red, -1.0f);
        TS_ASSERT_EQUALS(object_test_1.color.green, -1.0f);
        TS_ASSERT_EQUALS(object_test_1.color.blue, -1.0f);
        TS_TRACE("TEST 002 test +setColor() change color SUCCESS");

    }

    // test setPosition(), getPosition()
    void Test_position_test(void){
        Object object_test_i2;
        TS_ASSERT_THROWS_NOTHING(object_test_i2.draw());
        Position test1;
        TS_ASSERT_THROWS_NOTHING(test1.setPosition(70.0f,70.0f));
        object_test_i2.setPosition(test1.x, test1.y);
        TS_ASSERT_EQUALS(object_test_i2.position.x, test1.x);
        TS_ASSERT_EQUALS(object_test_i2.position.y, test1.y);
        TS_ASSERT_THROWS_NOTHING(object_test_i2.setPosition(80.0f,80.0f));
        TS_ASSERT_DIFFERS(object_test_i2.position.x, test1.x);
        TS_ASSERT_DIFFERS(object_test_i2.position.y, test1.y);
        TS_TRACE("\tTEST 001 test_position SUCCESS");
    }


    // test getSize(), setSize()
    void Test_object_size_test(void){
        Object object_test_i2_1;
        TS_ASSERT_EQUALS(object_test_i2_1.size, object_test_i2_1.getSize());
        TS_ASSERT_THROWS_NOTHING(object_test_i2_1.setSize(0.0f));
        TS_ASSERT_EQUALS(object_test_i2_1.size, 0.0f);
        TS_ASSERT_EQUALS(object_test_i2_1.getSize(), 0.0f);
        TS_TRACE("\tTEST test_size SUCCESS");
    }

    // test getColor(), setColor()
    void Test_object_color_test(void){

        Color test2;
        TS_ASSERT_EQUALS(test2.red, 0.9f);
        TS_ASSERT_EQUALS(test2.green, 0.0f);
        TS_ASSERT_EQUALS(test2.blue, 0.0f);
        TS_ASSERT_THROWS_NOTHING(test2.setColor(0.5f,0.3f,0.0f));
        TS_TRACE("\tTEST 001 change_color SUCCESS");
    
        Object object_test_i2_2;
        TS_ASSERT_THROWS_NOTHING(test2.setColor(0.5f,0.3f,0.0f));

        TS_ASSERT_EQUALS(object_test_i2_2.color.red, 0.5f);
        TS_ASSERT_EQUALS(object_test_i2_2.color.green, 0.3f);
        TS_ASSERT_EQUALS(object_test_i2_2.color.blue, 0.0f);
        TS_ASSERT_EQUALS(object_test_i2_2.color.red, test2.red);
        TS_ASSERT_EQUALS(object_test_i2_2.color.green, test2.green);
        TS_ASSERT_EQUALS(object_test_i2_2.color.blue, test2.blue);
        TS_TRACE("\tTEST 002 change_color SUCCESS");

        Color cl = object_test_i2_2.getColor();
        TS_ASSERT_EQUALS(object_test_i2_2.color.red, cl.red);
        TS_ASSERT_EQUALS(object_test_i2_2.color.green, cl.green);
        TS_ASSERT_EQUALS(object_test_i2_2.color.blue, cl.blue);
       
        TS_TRACE("\tTEST test_color SUCCESS");
        
    }
};


/*
  As we want to test the private members of
  class Robot, we have to declare class RobotTest
  as its friend class.
*/


class RobotTests : public CxxTest::TestSuite
{
public:
    void Test_getDegree(void){
        Robot robot_test_1(windowX, windowY);
        TS_ASSERT_DELTA(robot_test_1.getDegree(0.0, 1.0), PI/2.0, 0.001);
        TS_ASSERT_DELTA(robot_test_1.getDegree(0.0, -1.0), PI * 3 / 2.0, 0.001);
        TS_ASSERT_DELTA(robot_test_1.getDegree(1.0, 0.0), 0.0, 0.001);
        TS_TRACE("TEST test getDegree() SUCCESS");
    }

    void Test_refreshRobot(void){
        /*
          There is nothing to test, because
          this function will call timer.getElapsedTime(),
          so the result is unpredictable
        */
        TS_TRACE("TEST test refreshRobot() SUCCESS");
    }

    void Test_stepSpeed(void){
        Robot robot_test_1(windowX, windowY);
        float &speed = robot_test_1.speed;


        //negative value testing
        TS_ASSERT_THROWS_NOTHING(speed = 0.0);
        TS_ASSERT_THROWS_NOTHING(robot_test_1.stepSpeed(-1));
        TS_ASSERT_DELTA(speed, 0.0, 0.00001);
    
        TS_ASSERT_THROWS_NOTHING(robot_test_1.stepSpeed(+1));
        TS_ASSERT_DELTA(speed, unitSpeed, 0.00001);
        TS_TRACE("TEST test stepSpeed() SUCCESS");
    }

    void Test_stepDirection(void){
        Robot robot_test_1(windowX, windowY);
        float &dir = robot_test_1.degree;

  
        TS_ASSERT_THROWS_NOTHING(dir = 0.0);
        TS_ASSERT_THROWS_NOTHING(robot_test_1.stepDirection(-1));
        TS_ASSERT_DELTA(dir, 2 * PI - unitDegree, 0.00001);

        TS_ASSERT_THROWS_NOTHING(dir = 2 * PI);
        TS_ASSERT_THROWS_NOTHING(robot_test_1.stepDirection(+1));
        TS_ASSERT_DELTA(dir, unitDegree, 0.00001);

        TS_ASSERT_THROWS_NOTHING(dir = 0.0);
        TS_ASSERT_THROWS_NOTHING(robot_test_1.stepDirection(1));
        TS_ASSERT_DELTA(dir, unitDegree, 0.00001);
    
        TS_TRACE("TEST test stepDirection() SUCCESS");
    }

    void Test_getDirection(){
        Robot robot;
        TS_ASSERT_EQUALS(robot.getDirection(), robot.degree);
        TS_TRACE("TEST test getDirection() SUCCESS");
    }

    void Test_invCollisionDir(){
        Position node(50.0f, 50.0f);
        Robot robot(40.0f, 50.0f);
        robot.invCollisionDir(node);
        TS_ASSERT_DELTA(robot.getDirection(), PI, 0.0001f);

        robot.degree = 0.0f;
        node.setPosition(40.0f, 70.0f);
        robot.invCollisionDir(node);
        TS_ASSERT_DELTA(robot.getDirection(), 0.0f, 0.0001f);

        robot.degree = PI / 4;
        robot.setPosition(0.0f, 0.0f);
        node.setPosition(10.0f, 0.0f);
        robot.invCollisionDir(node);
        TS_ASSERT_DELTA(robot.getDirection(), PI * 3 / 4, 0.0001f);
        
    }
    
        
    

  
    /*
      We do not test +draw()
      mainly due to the fact that their effect could
      be obsevered from the graphical screen
    */  

};



/* Test class Obstacle,
   class Obstacle inherit from class Object,
   most of its methods have been tested in ObjectTests
*/
class ObstacleTests : public CxxTest::TestSuite
{
public:
    void Test_obstacle_test(void){
        Obstacle test1;
        TS_ASSERT_THROWS_NOTHING(test1.draw());
        TS_TRACE("TEST   test_Obstacle_class SUCCESS");

    }
};



/* Test class Goal
   Most of class Goal's methods inherit from class Object,
   those methods has been tested in Object
*/

class GoalTests : public CxxTest::TestSuite
{
public:
    void Test_goal_class(void) {
        Object tmp;
        Goal test1;
        TS_ASSERT_THROWS_NOTHING(test1.draw());
        TS_TRACE("TEST   test_goal_class SUCCESS");
    }

};


// Test class Timer
class TimerTest : public CxxTest::TestSuite
{
public:
    void Test_timer(void) {
        Timer test1;
    
        TS_ASSERT_THROWS_NOTHING(test1.getElapsedTime());
        TS_ASSERT_THROWS_NOTHING(test1.initialize());
        TS_ASSERT_THROWS_NOTHING(test1.elapsedTime);
        TS_TRACE("TEST   test_timer SUCCESS");

    }

};


//Test VectorClass
class VectorClassTest : public CxxTest::TestSuite
{
public : 
    void test_getLength()
    {
        VectorClass vec1(1,1);
        VectorClass vec2;
        cout << vec1.getLength() << endl;
        cout << vec2.getLength() << endl;
        VectorClass vec = vec1 - vec2;
        cout << vec.getX() << " " << vec.getY() << endl;
    }
    
};






#endif
