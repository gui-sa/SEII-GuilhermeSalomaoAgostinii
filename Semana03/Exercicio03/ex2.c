#include <stdio.h>
#include <stdlib.h>

int main (){

    int return_value; 
    return_value = system("ls -l /"); //calls the Shell to run ls -l command. It returns the exit status


    return return_value;
}