from logger import setup_logger
from spreadsheetProcessor import processSheet
from os import listdir
from os.path import isfile, join
from shutil import move
from re import search

#setup working directory and desired file format
workingDir = 'F:\\Users\\Mike\\OneDrive\\Documents\\GitHub\\Python\\Weekend2Project\\'
fileFormat = 'expedia_report_monthly_[A-Za-z]+_[0-9]{4}.xlsx'

#set up the loggers
mainLogger = setup_logger('mainLogger', workingDir + 'project.log','%(asctime)s %(levelname)-8s %(message)s')
fileListLogger = setup_logger('fileListlogger', workingDir + 'file.lst', '%(message)s')

#get the files that need to be worked on and pull the record of files that have already been processed
excelFiles = [f for f in listdir(workingDir) if isfile(join(workingDir,f)) and search("\.xlsx$", f)]
processedFiles = []
with open(workingDir + 'file.lst') as pf:
    processedFiles = pf.read()

#process each file
for file in excelFiles:
    if search(fileFormat, file):
        mainLogger.info("Checking for {} in file.lst".format(file))
        if file in processedFiles:
            mainLogger.info('{} already processed. Sending to the Error folder'.format(file))
            move(workingDir + file, workingDir + "Error\\" + file)
            mainLogger.info("------------------------------")
            continue
        mainLogger.info('{} not found in file.lst. Processing now.'.format(file))
        result = processSheet(file, mainLogger)
        mainLogger.info('Sending {} to {} folder'.format(file, result))
        move(workingDir + file, workingDir + result + "\\" + file)
    else:
        mainLogger.info('The file name {} is not formatted correctly. Be sure to use the format "expedia_report_monthly_[month]_[year].xlsx"'.format(file))
        mainLogger.info('Sending {} to the Error folder'.format(file))
        move(workingDir + file, workingDir + 'Error\\' + file)
    mainLogger.info("------------------------------")
    fileListLogger.info(file)

