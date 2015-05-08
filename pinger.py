#!/usr/bin/env python

'''
This scripts pings the lab networks
'''

import os, sys, re, subprocess


class Pinger:
    def __init__(self):
        self.blah = "blah"

    def pingIt(self, subnet, ipaddr):
        cmdPing = "ping -c 1 -W 1 " + str(subnet) + "." + str(ipaddr)

        result = subprocess.Popen(cmdPing,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  shell=True)
        out, error = result.communicate()

        result = out.split("\n")
        if re.search("bytes from",result[1]):
            print result[1]
            return True
        else:
            noPing = subnet + "." + (str(ipaddr))
            return noPing

if __name__ == "__main__":
    print " Please launch using main_ping.py"

    # localRun = Pinger()
    # localRun.pingIt("172.18.10", "200")
