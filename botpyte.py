import socket

class BotIRC(object):
    def __init__(self, server, channel, botnick):
        self.server = server
        self.channel = channel
        self.botnick = botnick
        self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ircsock.connect((self.server, 6667))
        self.ircsock.send('USER ' + self.botnick + ' ' + self.botnick + ' ' + self.botnick + ' ' + ':I am not a robot.\n')
        self.ircsock.send('NICK ' + self.botnick + '\n')
        
        self.ircsock.setblocking(0)
        while True:
            try:
                ircmsg = self.ircsock.recv(512)
                print ircmsg
                if ircmsg.find('PING :') != -1:
                    self.ping()
                    break
                elif not ircmsg:
                    break
            except:
                break
        self.ircsock.setblocking(1)
        self.joinchan()
        
    def ping(self):
        self.ircsock.send('PONG :pingis\n')
    def sendmsg(self, msg):
        self.ircsock.send('PRIVMSG ' + self.channel + ' :' + msg + '\n')
    def joinchan(self):
        self.ircsock.send('JOIN ' + self.channel + '\n')
    def quit(self):
        self.ircsock.send('QUIT\n\r :Power Off')
    def run(self):
        pass

if __name__ == '__main__':
    class MyBotIRC(BotIRC):
        def __init__(self, server, channel, botnick):
            BotIRC.__init__(self, server, channel, botnick)
        def run(self):
            while True:
                ircmsg = self.ircsock.recv(512)
                ircmsg = ircmsg.strip('\n\r')
                if ircmsg.find('PING :') != -1:
                        self.ping()
                if ircmsg:
                    print ircmsg
    MightMorgan = MyBotIRC(server ='irc.freenode.net', channel = '#test', botnick = 'Morgan12345')
    MightMorgan.run()
        
