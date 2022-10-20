gcc -c src/mytime.c -I include/ -o obj/mytime.o
gcc ./apps/app.c ./obj/float_vector.o -I ./include -o ./bin/app 
gcc ./apps/app_com_mytime.c ./obj/float_vector.o ./obj/mytime.o -I ./include -o ./bin/app_com_mytime 