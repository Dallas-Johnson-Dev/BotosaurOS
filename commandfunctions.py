import random

from command import command


def reformatArrayFromString(string):
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


'''
Everything below this comment is bot commands!
Function syntax:
async def function (bot, channel, params)
Specify the bot as an input variable so we have something to call back to if (or when) messages are sent
Specify the channel, to be honest this is just making my life easier when sending a message.
TODO: Possibly implement string returns to remove the need for adding the bot and channel in the message
'''


# We won't modify how showhelp works for now.
def showHelp(params):
    helpString = 'Please run ~help fun | general | sprint to see a list of related commands.\n'
    helpString = helpString + "Use ~help \"command name\" to get a brief description of what it does."
    return helpString


def iGetIt(params):
    return 'https://giphy.com/gifs/zkzKGK9FG9RYI'


# arg[0] is how many die, arg[1] is the size of the dice
def rolldice(params):
    parameters = stringtoarray(params)
    if len(parameters) < 2:
        return 'Please use two integers, one for number of dice and one for size of the die'
    if int(parameters[0]) > 100:
        return 'Are you trying to crash someone out? Please use something less than or equal to 100 die.'
    try:
        rollmsg = ""
        for x in range(0, int(parameters[0])):
            rollmsg = rollmsg + str(random.randint(1, int(parameters[1]))) + ' '
        return rollmsg
    except ValueError:
        return 'Please use integer values as inputs!'


def choose(params):
    if len(params) < 1:
        return "I can't suggest anything if you won't tell me what you'd like to do!"
    choicelist = params.split(',')
    choice = choicelist[random.randint(0, len(choicelist) - 1)]
    sentences = ["Does {0} sound fun?".format(choice),
                 "How about {0}?".format(choice),
                 "I think you should {0}.".format(choice),
                 "What about {0}?".format(choice),
                 "Might I suggest {0}?".format(choice)]
    return sentences[random.randint(0, len(sentences) - 1)]


def pizza(params):
    return "https://giphy.com/gifs/pizza-post-vision-superchief-l0HlPLowNerqVkAsU"


def wednesday(params):
    return "https://www.youtube.com/watch?v=du-TY1GUFGk&ab_channel=JimmyHere"


def writingtime(params):
    return "https://giphy.com/gifs/XIqCQx02E1U9W"


def tableflip(params):
    return "https://giphy.com/gifs/ineedthisforreactions-table-flip-tableflip-uKT0MWezNGewE"


def forshame(params):
    return "https://m.popkey.co/f6d204/LWYby_s-200x150.gif"


def salty(params):
    return "https://giphy.com/gifs/sweat-seinfield-salty-discharge-C7XaPdXaaKQNy"


def wtf(params):
    fuckery = ["http://giphy.com/gifs/vh1-uTF44XsHNxa2Q",
               "http://giphy.com/gifs/originals-wtf-3o6oztIyMbZT0nLdU4",
               "http://giphy.com/gifs/optical-illusions-asap-science-aZ3LDBs1ExsE8",
               "https://media1.giphy.com/media/26tPmrPE9dzaC5Ixq/200.gif",
               "https://media0.giphy.com/media/10NOvYHKZJeal2/200.gif",
               "https://media3.giphy.com/media/3o6gDREoETcSrm9Wog/200.gif",
               "https://media1.giphy.com/media/9R9pGcCFn3ZKM/200.gif"]
    return fuckery[random.randint(0, len(fuckery))]


def lewd(params):
    return "http://giphy.com/gifs/face-lenny-Hot2b4Wn3aHwk"


'''
TODO: Advice command
Can take a username as an optional command, else it'll just output something.
Should probably read from a text file because holy shit will this be a huge array.
'''

# command categories are general, fun, sprint
showhelpcmd = command().setcategory("general").setfunction(showHelp).setdescription(
    "Usage: ~help command | all\nDisplays information related to a specific command or all commands if desired.")
igetitcmd = command().setcategory("fun").setfunction(iGetIt).setdescription(
    "Usage: ~igetit\nSends a gif of JonTron saying \"I get it\".")
pizzacmd = command().setcategory("fun").setfunction(pizza).setdescription("Usage: ~pizza\nSends a gif of a pizza DJ.")
wednesdaycmd = command().setcategory("fun").setfunction(wednesday).setdescription(
    "Usage: ~wednesday\nIt\'s wednesday my dudes!")
tableflipcmd = command().setcategory("fun").setfunction(tableflip).setdescription(
    "Usage: ~tableflip\nFor when you really need to flip that table.")
choosecmd = command().setcategory("general").setfunction(choose).setdescription(
    "Usage: ~choose <comma separated values>\nChooses an element from the list provided and suggests it to you.")
rolldicecmd = command().setcategory("general").setfunction(rolldice).setdescription(
    "Usage: ~rolldice count max\nRolls a number of dice of a specific count with the max being its highest value.")
writingtimecmd = command().setcategory("fun").setfunction(writingtime).setdescription(
    "Usage: ~writingtime\nHave you written your words today?")
shamecmd = command().setcategory("fun").setfunction(forshame).setdescription("Usage: ~shame\nShame be upon thee!")
saltycmd = command().setcategory("fun").setfunction(salty).setdescription(
    "Usage: ~salty\nThe sodium levels in this room are rising!")
wtfcmd = command().setcategory("fun").setfunction(wtf).setdescription("Usage: ~wtf\nWhat the fuck?")
lewdcmd = command().setcategory("fun").setfunction(lewd).setdescription("Usage: ~lewd\nSomeone said something dirty ;D")

cmdtable = {
    "~showhelp": showhelpcmd,
    "~help": showhelpcmd,
    "~igetit": igetitcmd,
    "~pizza": pizzacmd,
    "~wednesday": wednesdaycmd,
    "~tableflip": tableflipcmd,
    "~choose": choosecmd,
    "~rolldice": rolldicecmd,
    "~writingtime": writingtimecmd,
    "~shame": shamecmd,
    "~salty": saltycmd,
    "~wtf": wtfcmd,
    "~lewd": lewdcmd
}
