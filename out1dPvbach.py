import sys
sys.path.append('/Users/keisuke/work/postOF/code')
import out1dPostProcess


if __name__ == '__main__':
    readPath='/Volumes/G-DRIVE USB-C/calculationResultFromSC/Lu/u25x10000/xxx.foam'
    pvbatchmfrPost = out1dPostProcess.PvbatchMFRPostProcess(readPath)

    ##### get 1dCsvFile #####
    extractPoint1 = [0.0, 0.0, 0.0]
    extractPoint2 = [0.1, 0.0, 0.0]
    pvbatchmfrPost.pvbatch1dCsv(extractPoint1, extractPoint2)
    
    extractPoint1 = [0.0, 0.00025, 0.0]
    extractPoint2 = [0.1, 0.00025, 0.0]
    pvbatchmfrPost.pvbatch1dCsv(extractPoint1, extractPoint2)
    
    extractPoint1 = [0.0, 0.00075, 0.0]
    extractPoint2 = [0.1, 0.00075, 0.0]
    pvbatchmfrPost.pvbatch1dCsv(extractPoint1, extractPoint2)


