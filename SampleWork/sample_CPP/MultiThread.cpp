#include "MultiThread.h"

#include <iostream>
using namespace std;

void* interactTerminal(void *para)
{
    string cmd;
    cin >> cmd;
    while (cmd.compare("exit") != 0)
    {
        interpreter.excuteCommand(cmd);
        cin >> cmd;
    }
    return ((void *)0);
}

void MultiThread::createThread()
{
    pthread_t ntid;
    int err = pthread_create(&ntid,NULL, interactTerminal,NULL);
    if(err != 0){
        printf("can't create thread: %s\n",strerror(err));
        //return 1;
    }
    
}
