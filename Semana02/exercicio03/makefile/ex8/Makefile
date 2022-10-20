BIN = ./bin
OBJ = ./obj
INCLUDE = ./include
SRC = ./src
APPS = ./apps

all: libed my_apps

libed: float_vector.o\
	 mytime.o

my_apps:
	gcc $(APPS)/app.c $(OBJ)/float_vector.o -I $(INCLUDE) -o $(BIN)/app
	gcc $(APPS)/app_com_mytime.c $(OBJ)/*.o -I $(INCLUDE) -o $(BIN)/app_com_mytime


%.o: $(SRC)/%.c $(INCLUDE)/%.h
	gcc -c $< -I $(INCLUDE) -o $(OBJ)/$@


run:
	./bin/app

clean:
	rm -rf ./bin/* ./obj/*