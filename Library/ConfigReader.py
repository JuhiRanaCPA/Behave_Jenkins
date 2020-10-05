import configparser

def read_configData(section,key):
    cfg = configparser.ConfigParser()
    cfg.read(filenames="C:/workspace/BEHAVE/Behave_Tutorial/mypython/ConfigurationFiles/Config.cfg")
    return cfg.get(section, key)

