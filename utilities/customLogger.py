import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Users\\Luis\\Desktop\\Selenium-Hybrid-Framework\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        loggeer=logging.getLogger()
        loggeer.setLevel(logging.INFO)
        return loggeer
