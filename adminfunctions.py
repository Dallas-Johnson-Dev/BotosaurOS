from command import AdminCommand
import discord

#When defining admin functions, pass in the client first, then the params afterward.

class admincoroutinereturn:
    rettype = ""
    member = None
    message = ""

    def __init__(self, calltype="", servmember=None, optionalmessage=""):
        self.rettype = calltype
        self.member = servmember
        self.message = optionalmessage

def searchForUser(client, username, server):
    serverlist = client.servers
    memberlist = []
    for x in serverlist:
        if x.name != server:
            continue
        memberlist = x.members
        for y in memberlist:
            #print(y.name)
            if username == y.name:
                return y
    return None

def reformatarrayfromstring(string):
    stripchars = '[]\''
    formattedstring = string
    for char in stripchars:
        formattedstring = formattedstring.replace(char, '')
    formattedstring = formattedstring.replace(',,', '_')
    formattedstring = formattedstring.replace(',', '')
    formattedstring = formattedstring.replace('_', ',')
    formattedstring = formattedstring.split(',')
    return formattedstring


def stringtoarray(string, delim=' '):
    return string.split(delim)

def test(client, params):
    print(params)
    print(type(params))
    return "Command successfully executed! Parameters were: {0}".format(params)

def getuserinfo(client, params): #This takes the username first, then the server name after that.
    retstring = ""
    arguments = params.split(' ')
    servermember = searchForUser(client, arguments[0], arguments[1])
    if servermember is not None:
        retstring = "Info for {0}:\n".format(params)
        retstring = "{0} mute: {1}\n id: {2}\n status: {3}\n server: {4}\n".format(retstring, servermember.mute, servermember.id, servermember.status, servermember.server)
        return retstring
    return "Member not found!"

def mute(client, params):
    arguments = params.split(' ')
    if not len(arguments) == 2:
        return "Please speficy a server to mute the user on!"
    servermember = searchForUser(client, arguments[0], arguments[1])
    if servermember is not None:
        adminreturn = admincoroutinereturn
        adminreturn.rettype = "mute"
        adminreturn.member = servermember
        adminreturn.message = "{0} has been muted!".format(params)
        return adminreturn



cmdtest = AdminCommand(['admin', 'Administration', 'Bot Commander', 'moderator']).setcategory("admin").setfunction(test).setdescription("Replies with a message if the command was successfully executed.")
cmdmute = AdminCommand(['admin', 'Administration', 'moderator', 'Bot Commander']).setcategory("admin").setfunction(test).setdescription("Mutes a user on the server.")
cmdgetuserinfo = AdminCommand(['admin', 'Administration', 'moderator', 'Bot Commander']).setcategory("admin").setfunction(getuserinfo).setdescription("Looks up a user on the given servers.")

cmdtable = {
    "!test": cmdtest,
    "!mute": cmdmute,
    "!getuserinfo": cmdgetuserinfo
}