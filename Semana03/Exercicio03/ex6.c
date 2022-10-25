#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>
#include <signal.h>

int spawn(char *program, char** arg_list){
    pid_t child_pid;

    child_pid = fork();
    if (child_pid != 0 ){
        return child_pid;
    }else{
        execvp(program, arg_list);
        fprintf(stderr, "an error ocurred in execvp\n"); //se der erro, dai ele retorna para esse programa e printa esse texto
        abort(); //Mata esse processo filho
    }
}


int main (){
    int child_status;

    char *arg_list [] = {
        "ls",
        "-l",
        "/",
        NULL
    };

    spawn("ls", arg_list);
 
    wait(&child_status);
    if (WIFEXITED (child_status)){
        printf("The child process exited normally, with exit code %d\n", WEXITSTATUS(child_status));
    }else{
        printf("The child process exited abnormally\n");
    }

    return 0;
}