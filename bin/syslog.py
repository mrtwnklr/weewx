"""Using logging instead of syslog for easier docker logging."""

import syslog as syslog_original
import logging

LOG_ALERT   = logging.INFO
LOG_AUTH    = logging.INFO
LOG_CONS    = logging.INFO
LOG_CRIT    = logging.CRITICAL
LOG_CRON    = logging.INFO
LOG_DAEMON  = logging.INFO
LOG_DEBUG   = logging.DEBUG
LOG_EMERG   = logging.CRITICAL
LOG_ERR     = logging.ERROR
LOG_INFO    = logging.INFO
LOG_KERN    = logging.INFO
LOG_LOCAL0  = logging.INFO
LOG_LOCAL1  = logging.INFO
LOG_LOCAL2  = logging.INFO
LOG_LOCAL3  = logging.INFO
LOG_LOCAL4  = logging.INFO
LOG_LOCAL5  = logging.INFO
LOG_LOCAL6  = logging.INFO
LOG_LOCAL7  = logging.INFO
LOG_LPR     = logging.INFO
LOG_MAIL    = logging.INFO
LOG_NDELAY  = logging.INFO
LOG_NEWS    = logging.INFO
LOG_NOTICE  = logging.INFO
LOG_NOWAIT  = logging.INFO
LOG_PERROR  = logging.ERROR
LOG_PID     = logging.INFO
LOG_SYSLOG  = logging.INFO
LOG_USER    = logging.INFO
LOG_UUCP    = logging.INFO
LOG_WARNING = logging.WARNING

def syslog(level, message):
    logging.log(level, message)
    return

def openlog(label, levels):
    logging.basicConfig(level=logging.INFO)
    syslog(LOG_INFO, "openlog() with %s and %s" % (label, levels))
    return

def LOG_UPTO(level):
    return level

def setlogmask(level):
    logging.basicConfig(level=level)
    syslog(LOG_INFO, "setlogmask() with %s" % level)
    return
