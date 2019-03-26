#!/usr/local/CyberCP/bin/python2
import sys
sys.path.append('/usr/local/CyberCP')
import plogical.CyberCPLogFileWriter as logging
from plogical.mailUtilities import mailUtilities
from serverStatus.serverStatusUtil import ServerStatusUtil
from plogical.processUtilities import ProcessUtilities
import time


class DockerInstall:

    @staticmethod
    def submitInstallDocker():
        try:

            mailUtilities.checkHome()

            statusFile = open(ServerStatusUtil.lswsInstallStatusPath, 'w')

            logging.CyberCPLogFileWriter.statusWriter(ServerStatusUtil.lswsInstallStatusPath,
                                                      "Starting Docker Installation..\n", 1)

            command = "sudo adduser docker"
            ServerStatusUtil.executioner(command, statusFile)

            command = 'sudo groupadd docker'
            ServerStatusUtil.executioner(command, statusFile)

            command = 'sudo usermod -aG docker docker'
            ServerStatusUtil.executioner(command, statusFile)

            command = 'sudo usermod -aG docker cyberpanel'
            ServerStatusUtil.executioner(command, statusFile)

            if ProcessUtilities.decideDistro() == ProcessUtilities.centos:
                command = 'sudo yum install -y docker'
            else:
                command = 'sudo DEBIAN_FRONTEND=noninteractive apt-get install -y docker.io'

            if not ServerStatusUtil.executioner(command, statusFile):
                logging.CyberCPLogFileWriter.statusWriter(ServerStatusUtil.lswsInstallStatusPath,
                                                          "Failed to install Docker. [404]\n", 1)
                return 0

            command = 'sudo systemctl enable docker'
            ServerStatusUtil.executioner(command, statusFile)

            command = 'sudo systemctl start docker'
            ServerStatusUtil.executioner(command, statusFile)

            logging.CyberCPLogFileWriter.statusWriter(ServerStatusUtil.lswsInstallStatusPath,
                                                      "Docker successfully installed.[200]\n", 1)

            time.sleep(2)

            command = 'sudo systemctl restart gunicorn.socket'
            ProcessUtilities.executioner(command)

        except BaseException, msg:
            logging.CyberCPLogFileWriter.statusWriter(ServerStatusUtil.lswsInstallStatusPath, str(msg) + ' [404].', 1)

DockerInstall.submitInstallDocker()