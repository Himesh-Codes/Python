#!/usr/bin/env python3
"""
Chat analysis demo using string objects
"""

from datetime import datetime

class Chat(str):
    demoMessage: str

    def __init__(self, **kwargs):
        self._endUser = kwargs['EndUser'] if 'EndUser' in kwargs else None
        self._endUserMsg = kwargs['EndUserMessage'] if 'EndUserMessage' in kwargs else None
        self._currentUserMsg = kwargs['CurrentUserMessage'] if 'CurrentUserMessage' in kwargs else None
        # since STRINGS in py is object we can directly use them as objects,
        # and multiline strings using tripple qoutes
        self.demoMessage = """
                            Hello there! 
                            Its....
                            {} now..""".format(datetime.now())

    def printDemoMessage(self) -> str:
        print(self.demoMessage)

    def getCaseFoldedMessages(self) -> dict:
        self._currentUserMsg = self._currentUserMsg.casefold() if self._currentUserMsg else None
        self._endUserMsg = self._endUserMsg.casefold() if self._endUserMsg else None
        return {'endUser': self._endUserMsg, 'current': self._currentUserMsg}

    #concatenate string with '+'
    def getEndUserDetails(self) -> str:
        #check value is empty/null
        if not self._endUser or not self._currentUserMsg:
            return None
        else:
            return self._endUser + self._currentUserMsg

"""
    String formatting
"""
class ChatFormat(Chat):
    currentChat: list
    filterWords = ['shit', 'idiot']
     
    def __init__(self, **kwargs):
        super(ChatFormat, self).__init__(**kwargs)
        self.currentChat = []
        
    def endUserMessageTrack(self) -> list:
        #named keys arguments format for string
        self.currentChat.append('The message send by {name} is {chat}'.format(name = self._endUser, chat = self._endUserMsg))

        #positional argument formatting
        self.currentChat.insert(0, 'The message send by {0} is {1}'.format(self._endUser, self._endUserMsg))
        
        #give justified spacing, add space in right, add symbol in left
        self.currentChat.append('The network health is {0:<5} {1:>+4}'.format(2000, 100))
        
        #add comma in big numbers, and replace with dot
        self.currentChat.append('The total message char send is {:,}'.format(723 * 667 * 100).replace(',', '.'))
        
        #decimal point add by 'f' and count '3'
        self.currentChat.append('The ping is {:.3f}'.format(723 * 667 * 100))
        #convert hexadecimal with 'x', octa 'o', binary 'b'
        self.currentChat.append('The ping is {:b}'.format(723 * 667 * 100))

        return self.currentChat
    
    #split and join of strings
    def filterAbuseMessage(self, message: str):
        for word in self.filterWords:
           splitMessage = message.split(word) 
           splitMessage = '****'.join(splitMessage)
        # splitMessage = [message for message in splitMessage if message.lower() not in self.filterWords]
        return splitMessage
        
        

personOnechat = Chat()
personOnechat.printDemoMessage()
print(personOnechat.getCaseFoldedMessages())
print(personOnechat.getEndUserDetails())

personChatStudy = ChatFormat()
print(personChatStudy.endUserMessageTrack())
print(personChatStudy.filterAbuseMessage(""" 
                                    I am not going to talk with you idiot .
                                    Get off!!!
                                    """))