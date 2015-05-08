#!/usr/bin/env  python



#### copied from temp_monitor for reference only ###

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import shutil

class PlotData:

    def __init__(self):
        self.x = []
        self.y = []

    def plot(self):
        with open("/code/temp_monitor/newPlotData.txt","r") as f:

            for line in f:
                sepLine = line.split(",")
                temp1 = float(sepLine[1])
                # print temp1
                self.x.append(float(sepLine[0]))
                # self.y.append(float(sepLine[1].strip()))
                self.y.append(temp1)

        plt.plot(self.x,self.y)
        plt.title("Software Lab Temperature - Flipflap")
        plt.xlabel('Time')
        plt.ylabel('Temps')

        plt.savefig('/code/temp_monitor/temps.png')
        shutil.copy('/code/temp_monitor/temps.png',"/var/www/html/temps.png")
        self.writeIndexFile()

    def writeIndexFile(self):

        with open("/code/temp_monitor/index.html", "w") as index:

            index.write("<head>")
            index.write("<meta http-equiv='refresh' content='30'>")
            index.write("<head>")
            index.write("<a href='temps/Historical_Temps.html'>Historical Temps</a>")
            index.write("<p>")

            index.write("               Current temperature in the Software Lab")
            index.write("<br>")
            index.write("<img src='temps.png' alt='lab temp' height='420' width='840'>")
            index.write("<p>")

        self.filecopy()


    def filecopy(self):

        print "copying files, please be patient"
        shutil.copy('/code/temp_monitor/index.html', "/var/www/html/index.html")
        print "done"

if __name__ == "__main__":
    localRun = PlotData()
    localRun.plot()
    # localRun.writeIndexFile()
    # localRun.filecopy()