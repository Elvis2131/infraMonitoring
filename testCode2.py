import appLogs as log

def sendNotification():
    log.saveLog(fileInvoke=__file__, funcInvoke=sendNotification.__name__, msg="We are working")

sendNotification()