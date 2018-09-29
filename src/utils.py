import os

def dataPathFromName(datasetName):
    root = rootDir()

    if datasetName == "mnist":
        return os.path.join(root, 'data', 'mnist')
    
    print("Dataset '" + datasetName + "' not defined. Exiting.")
    exit()

def rootDir():
	return os.path.dirname(os.path.dirname(__file__))
