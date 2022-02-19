from logger import setup_logger
from spreadsheetProcessor import processSheet
from os import listdir
from os.path import isfile, join
from shutil import move


workingDir = 'F:\\Users\\Mike\\OneDrive\\Documents\\GitHub\\Python\\Weekend2Project\\'

mainLogger = setup_logger('mainLogger', workingDir + 'project.log','%(asctime)s %(levelname)-8s %(message)s')
fileListLogger = setup_logger('fileListlogger', workingDir + 'file.lst', '%(message)s')

excelFiles = [f for f in listdir(workingDir) if isfile(join(workingDir,f)) and f[-5:] == ".xlsx"]

processedFiles = []
with open(workingDir + 'file.lst') as pf:
    processedFiles = pf.read()

for file in excelFiles:
    mainLogger.info("Checking for {} in file.lst".format(file))
    if file in processedFiles:
        mainLogger.info('{} already processed. Moving to next file'.format(file))
        move(workingDir + file, workingDir + "Error\\" + file)
        continue
    mainLogger.info('{} not found in file.lst. Processing now.'.format(file))
    result = processSheet(file, mainLogger)
    mainLogger.info('Sending {} to {} folder'.format(file, result))
    move(workingDir + file, workingDir + result + "\\" + file)
    fileListLogger.info(file)
