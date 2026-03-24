

db = {
    "admin":"test1234",
    "test":"test"
}

def auth(username, password):
    for i in db:
        print(i)
        if username == i and password == db[i]:
                print("Succesfully!!!!")
        print("incorrect username or password :(")  

if __name__ == "__main__":
    auth("test1","test")              