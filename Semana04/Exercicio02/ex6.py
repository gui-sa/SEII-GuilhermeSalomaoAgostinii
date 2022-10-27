class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod #Dont has access to class props.
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("run")



print(Math.add5(5))
print(Math.add10(5))
Math.pr()