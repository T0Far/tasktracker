import json
import sys
from datetime import datetime

timestamp = str(datetime.now().day) + "/" + str(datetime.now().month) + "/" + str(datetime.now().year) + " " + str(datetime.now().hour) + ":" + str(datetime.now().minute)

def main():

    try:
        command = sys.argv[1]
    except:
        print("Usage: ./tasktrack.py (command)")
        return

    argcount = len(sys.argv)

    if command == "add":
        
        # checks for correct no of arguments
        if argcount != 3:
            print("Error\nCorrect Usage: ./tasktrack.py add (newtask)")
            return

        newtask = sys.argv[2]
        addtask(newtask)
        return

    elif command == "update":

        # checks for correct no of arguments and checks that task id is an int
        if argcount != 4 or not sys.argv[2].isdigit():
            print("Error\nCorrect Usage: ./tasktrack.py update (task id) (newtask)")
            return

        newtask = sys.argv[3]
        updateid = sys.argv[2]
        updatetask(updateid, newtask)
        return      

    elif command == "delete":

        # checks for correct no of arguments and checks that id is an int
        if argcount != 3 or not sys.argv[2].isdigit():
            print("Error\nCorrect Usage: ./tasktrack.py delete (task id)")
            return
        
        deleteid = sys.argv[2]
        deletetask(deleteid)
        return

    elif command == "mark-in-progress":

        # checks for correct no of arguments and checks that id is an int
        if argcount != 3 or not sys.argv[2].isdigit():
            print("Error\nCorrect Usage: ./tasktrack.py mark-in-progress (task id)")
            return

        inprogressid = sys.argv[2]
        markinprogress(inprogressid)
        return

    elif command == "mark-done":

        # checks for correct no of arguments and checks that id is an int
        if argcount != 3 or not sys.argv[2].isdigit():
            print("Error\nCorrect Usage: ./tasktrack.py mark-done (task id)")
            return

        doneid = sys.argv[2]
        markdone(doneid)
        return

    elif command == "list":

        # checks for correct no of arguments
        if argcount < 2 or argcount > 3:
            print("Error\nCorrect Usage: ./tasktrack.py list (done/todo/in-progress)")
            return
        
        listtype = "all"

        # if there is an argument after "list" in the cli, assigns listtype to that argument
        try:
            listtype = sys.argv[2]

            # checks that listtype is valid
            if listtype not in ["all", "todo", "in-progress", "done"]:
                print("Error\nCorrect Usage: ./tasktrack.py list (done/todo/in-progress)")
                return
        except:
            pass

        #listtype is "all" if there are no arguments after list
        listtasks(listtype)
        return

    print("Usage: ./tasktrack.py (command)")

def addtask(newtask):

    id = 0
    data = []

    # if there is already a json file, assigns the list of dictionaries in the json file to data. 
    try:
        with open("tasks.json") as tasks:
            data = json.load(tasks)

        # uses last id currently in the list to calculate the id for the new task, just + 1
        id = data[-1]["id"] + 1
    except:
        pass

    data.append({"id" : id, "task" : newtask, "status" : "todo", "createdat" : timestamp, "updatedat" : timestamp})
    with open("tasks.json", "w") as tasks:
        json.dump(data, tasks)


def updatetask(updateid, newtask):

    updateid = int(updateid)

    try:
        with open("tasks.json") as tasks:
            data = json.load(tasks)
        
        #used later to check if updateid is in range of ids stored in the json
        lastid = data[-1]["id"]
    except:
        print("task list is empty")
        return

    # checks that updateid exists in the json file
    if updateid < 0 or updateid > lastid:
        print("id does not exist")
        return
    
    # replaces old task with the new task
    data[updateid] = ({"id" : updateid, "task" : newtask, "status" : "todo", "createdat" : data[updateid]["createdat"], "updatedat" : timestamp})
    with open("tasks.json", "w") as tasks:
        json.dump(data, tasks)


def deletetask(deleteid):

    deleteid = int(deleteid)
    try:
        with open("tasks.json") as tasks:
            data = json.load(tasks)
        lastid = data[-1]["id"]
    except:
        print("no task to delete")
        return

    #checks that deleteid exists in the json
    if deleteid < 0 or deleteid > lastid:
        print("id does not exist")
        return

    data.pop(deleteid)
    # iterates over tasks after the deleted task. updates their id so that all ids consecutive again
    for i in range(deleteid, lastid, 1):
        data[i]["id"] = i

    with open("tasks.json", "w") as tasks:
        json.dump(data, tasks)


def markinprogress(inprogressid):

    inprogressid = int(inprogressid)

    try:
        with open("tasks.json") as tasks:
            data = json.load(tasks)
        lastid = data[-1]["id"]
    except:
        print("no task to mark")
        return

    if inprogressid < 0 or inprogressid > lastid:
        print("id does not exist")
        return
    
    # reassigns status and updatedat of the chosen updateid
    data[inprogressid]["status"] = "in-progress"
    data[inprogressid]["updatedat"] = timestamp

    with open("tasks.json", "w") as tasks:
        json.dump(data, tasks)


def markdone(doneid):

    doneid = int(doneid)

    try:
        with open("tasks.json") as tasks:
            data = json.load(tasks)
        lastid = data[-1]["id"]
    except:
        print("no task to mark")
        return

    if doneid < 0 or doneid > lastid:
        print("id does not exist")
        return
    
    # reassigns status and updatedat of the chosen updateid
    data[doneid]["status"] = "done"
    data[doneid]["updatedat"] = timestamp

    with open("tasks.json", "w") as tasks:
        json.dump(data, tasks)


def listtasks(listtype):

    try:
        with open("tasks.json") as tasks:
            data = json.load(tasks)
        if not data:
            raise
    except:
        print("no tasks")
        return

    listed = []

    # iterates over every task in data. if the status of the task == the chosen listtype, appends it to listed
    if listtype != "all":
        for i in data:
            if i["status"] != listtype:
                continue
            listed.append(i)
    else:
        # if listtype is all, listed reassigned to data
        listed = data

    if not listed:
        print("no tasks of this type")
        return

    # header of the table
    print(
            "   id  |                                                   tasks                                                  |  status         |      Created At       |     Updated At"    
    )

    for i in listed:
        # calculates amount of whitespace needed after the task
        whitespace1 = 100 - len(i["task"])
        spaces1 = ""
        for j in range(0, whitespace1):
            spaces1 += " "

        # calculates amount of whitespace needed after the status
        whitespace2 = 11 - len(i["status"])
        spaces2 = ""
        for j in range(0, whitespace2):
            spaces2 += " "

        print(
            "   {id}   |    {task}{space1}  |  {status}{space2}    |    {createdat}     |   {updatedat}".format(id = i["id"], task = i["task"], space1 = spaces1, status = i["status"], space2 = spaces2, createdat = i["createdat"], updatedat = i["updatedat"])
        )


main()