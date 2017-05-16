class HubInformation(object):

    def __init__(self):
        print 'HubInformation Init'

    def getserial(self):
        cpuserial = "0000000000000000"
        try:
            f = open('/proc/cpuinfo', 'r')
            for line in f:
                if line[0:6] == 'Serial':
                    cpuserial = line[10:26]
            f.close()
        except:
            cpuserial = "ERROR000000000"

        return cpuserial

    def getrevision(self):
        myrevision = "0000"
        try:
            f = open('/proc/cpuinfo', 'r')
            for line in f:
                if line[0:8] == 'Revision':
                    length = len(line)
                    myrevision = line[11:length - 1]
            f.close()
        except:
            myrevision = "0000"

        return myrevision