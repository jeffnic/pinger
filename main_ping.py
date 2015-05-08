#!/usr/bin/env python

'''
This is the main entry point for the lab ping script.
It pings and logs address availability
'''

from pinger import Pinger
import datetime, os, sys


class MainClass:
    def __init__(self):
        self.blah = "blah"
        self.ping = Pinger()
        self.network = ["10.35.0", "10.35.180", "10.35.155", "10.36.0", "10.36.1", "10.255.0", "10.255.1", "10.255.2", "10.255.3", "172.18.1", "172.18.3", "172.18.10"]
        # self.network = ["10.35.180"]   # testing network
        self.today = datetime.datetime.now()
        self.dayNow = self.today.strftime('%Y-%m-%d')
        self.parentDir = os.path.dirname(os.path.realpath(__file__))
        self.logDir_main = os.path.join(self.parentDir,"logs")
        self.logDir_responses = os.path.join(self.parentDir,"logs","ping_responses")
        self.htmlOutDir = os.path.join("/" + "var","www","html","pings" + "/")


    def pingNetwork(self):

        self.setupEnv()
        # pause = raw_input("ctrl-C to stop, enter to continue")

        for network in self.network:
            networkFile = (os.path.join(self.logDir_responses,network  + "-" + self.dayNow + "-" + "responses.txt"))
            with open(networkFile, "a+" ) as outfile:
                with open(os.path.join(self.logDir_main,network),"a+") as netFileOut:
                    netSummary = []
                    count = 0
                    for _ in range(1,254):    #testing
                        result = self.ping.pingIt(network,_)
                        if result == True:
                            count +=1
                            outfile.write(str(network) + "." + str(_) + "," + "True" + "\n")
                        else:
                            netSummary.append(result)
                            # for item in netSummary:
                            outfile.write(result + "," + "False" + "\n")
                    print "Pings from network %s.x: %s" % (network, count)
                    netFileOut.write(str(count) + "," + self.dayNow + "\n")
            self.makeWebPage(networkFile, network)


    def setupEnv(self):
        if not os.path.exists(self.logDir_main):
            print "Creating log directory"
            os.mkdir(self.logDir_main)

        if not os.path.exists(self.logDir_responses):
            print "Creating responses directory"
            os.mkdir(self.logDir_responses)



    def makeWebPage(self,networkFile,network):
        with open(networkFile, "r") as inFile:
            with open(os.path.join(self.htmlOutDir + network +  ".html"), "w") as outFile:
                outFile.write("<!DOCTYPE html>")
                outFile.write("<html>")
                outFile.write("<head>")
                outFile.write(" <link rel=stylesheet href=style.css>")
                outFile.write("</head>")
                outFile.write("<body>")
                outFile.write("<h2>" + "Pings from " + network + " on   " + self.dayNow + "</h2>")
                outFile.write("<table border=1>" + "\n")

                for line in inFile:
                    splitLine = line.split(",")
                    pingResponse = splitLine[1].strip()
                    if pingResponse == "True":
                        responseColor = "#00FF00"
                    else:
                        responseColor = "#FF0000"
                    outFile.write("<tr>"+ "<td bgcolor=" + responseColor + ">"+"{:>15}".format(splitLine[0]) +"</td>"  + "<td>"+"{:>25}".format(splitLine[1]) + "</td>" + " " + "<td>" + "{:>40}".format("placeholder2" + "</td></tr>" + "\n"))

                outFile.write("</table>")
                outFile.write("</body>")
                outFile.write("</html>")


if __name__ == "__main__":
    localRun = MainClass()
    localRun.pingNetwork()

'''
2-do:
track available addresses for 10.35.180.x, create web page with conditional formatting... red for used, green for available


Nathan idea: have python color cells in excel spreadsheet
'''
