import configparser



def readLocator(section, key):
    reader = configparser.ConfigParser()
    reader.read("C:/Users/valmiki/PycharmProjects/PythonSelenium/pythonSeleniumProjectDec222022/ConfigurationData/config.cfg")
    return reader.get(section,key)

myPhone=readLocator("Registration","country")
print(myPhone) #input[name='phone']

rg=readLocator("Registration","firstName")
print(rg)

