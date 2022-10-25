#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include <string.h>

sig_atomic_t child_exit_status;

void clean_up_child_process(int signal_number){
    int status;

    wait(&status);
    child_exit_status = status;
}



int main(){
    struct sigaction sigch1d_action;
    memset (&sigch1d_action, 0 , sizeof(sigch1d_action));
    sigch1d_action.sa_handler = &clean_up_child_process;
    sigaction(SIGCHLD, &sigch1d_action, NULL);
    
    

    return 0;
}