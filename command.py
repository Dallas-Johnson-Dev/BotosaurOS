class command:
    function = None
    executor = None
    executorlog = []
    description = ""
    output = ""
    category = ""

    def __init__(self):
        executorlog = []

    def logexecution(self, user, time):
        self.executorlog.append(logentry().setname(user).settime(time))

    def execute(self, parameters, user, time=""):
        self.logexecution(user, time)
        self.setexecutor(user)
        self.output = output().setcontent(self.function(parameters))
        return self.output

    def getfunction(self):
        return self.function

    def getpermissions(self):
        return self.permissions

    def getexecutor(self):
        return self.executor

    def getexecutorlog(self):
        return self.executorlog

    def getdescription(self):
        return self.description

    def getoutput(self):
        return self.output

    def getcategory(self):
        return self.category

    def setfunction(self, func):
        self.function = func
        return self

    def setpermissions(self, perms):
        self.permissions = perms
        return self

    def setexecutor(self, ex):
        self.executor = ex
        return self

    def setexecutorlog(self, exlog):
        self.executorlog = exlog
        return self

    def setdescription(self, desc):
        self.description = desc
        return self

    def setcategory(self, cat):
        self.category = cat
        return self


class admincommand(command):
    permissions = ["Dragonsire21#1223"]

    def execute(self, parameters, user, time=""):
        if user not in self.permissions():
            return output().setcontent("You do not have permission to do that!")
        self.execute(parameters, user, time)


class logentry:
    name = ""
    time = ""

    def __init__(self, name="", timestamp=""):
        self.name = name
        self.time = timestamp

    def getname(self):
        return self.name

    def gettime(self):
        return self.time

    def setname(self, name):
        self.name = name
        return self

    def settime(self, time):
        self.time = time
        return self


class output:
    isPM = False
    content = ""

    def __init__(self, pm=False, content=""):
        self.isPM = pm
        self.content = content

    def getPM(self):
        return self.isPM

    def getcontent(self):
        return self.content

    def setPM(self, pm):
        if type(pm) is not bool:
            raise TypeError
        else:
            self.isPM = pm
            return self

    def setcontent(self, content):
        self.content = content
        return self


class commandrunner:
    commandtable = {}

    def __init__(self, commands={}):
        self.commandtable = commands

    def executeFunction(self, message):
        command = message.content.split(' ')[0].lower()
        arguments = message.content
        arguments = arguments[len(command) + 1:len(arguments)]
        if not command in self.commandtable:
            return output().setcontent("I did not understand that command!")
        if command == "~help" or command == "~showhelp":
            arguments = arguments.split(' ')
            if not arguments[0]:
                return self.commandtable[command].execute(self.commandtable, message.author, message.timestamp)
            elif arguments[0][0] == '~':
                if not arguments[0] in self.commandtable:
                    return output().setcontent(
                        "This command doesn't exist! Please run ~help if you need more information.")
                return output().setcontent(self.commandtable[arguments[0]].getdescription())
            else:
                if arguments[0] != "fun" and arguments[0] != "general" and arguments[0] != "sprint":
                    return output().setcontent(
                        "This category does not exist! Please see ~help if you need more information.")
                return self.printhelpcategory(arguments[0])
        return self.commandtable[command].execute(arguments, message.author, message.timestamp)

    def getcommandtable(self):
        return self.commandtable

    def setcommandtable(self, commandtable):
        self.commandtable = commandtable
        return self

    def printhelpcategory(self, category):
        helpstring = "The following commands under {0} are:\n".format(category)
        for x in self.commandtable.keys():
            if self.commandtable[x].getcategory() == category:
                helpstring = helpstring + x + "\n"
        return output().setcontent(helpstring).setPM(True)
