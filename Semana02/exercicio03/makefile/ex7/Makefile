BIN = ./bin
OBJ = ./obj
INCLUDE = ./include
SRC = ./src
APPS = ./apps

all: libed my_apps

libed:
	gcc -c $(SRC)/float_vector.c -I $(INCLUDE) -o $(OBJ)/float_vector.o
	gcc -c $(SRC)/mytime.c -I $(INCLUDE) -o $(OBJ)/mytime.o

my_apps:
	gcc $(APPS)/app.c $(OBJ)/float_vector.o -I $(INCLUDE) -o $(BIN)/app
	gcc $(APPS)/app_com_mytime.c $(OBJ)/*.o -I $(INCLUDE) -o $(BIN)/app_com_mytime

run:
	./bin/app

clean:
	rm -rf ./bin/* ./obj/*