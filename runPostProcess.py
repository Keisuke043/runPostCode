import sys
sys.path.append('/Users/keisuke/work/postOF/code')
import postProcessMFR
import subprocess

def runGraphPostProcess():
    readPath1 = './csv1d_y0.0'
    readPath2 = './csv1d_y0.00075'
    
    #graph1d = postProcessMFR.Graph1d(readPath1, readPath2)
    graph1d = postProcessMFR.Graph1d(readPath1)
    
    # set readFileNum
    startNum = 30
    endNum = 100
    deltaNum = 1
    deltaT = 1/100
    graph1d.multiplePara = ['CO', 'CH2O']
    graph1d.multipleValue = [2, 10]
    graph1d.setReadCsv(startNum, endNum, deltaNum, deltaT)
    
    # set parameter
    graph1d.xlim = [3.5, 7.5]
    # select y_species or y_HRR or y_T or y_U or y_p
    graph1d.ax1Para = graph1d.y_species
    graph1d.y1speciesList = ['nC7H16', 'CO2', 'CO', 'CH2O']
    graph1d.y1colorList = ['r', 'b', 'g', 'c']
    graph1d.y1specieslim = [0, 0.2]
    graph1d.ax2Para = graph1d.y_HRR
    # graph1d.y2lim = [0, 1]
    graph1d.ax3Para = graph1d.y_T
    graph1d.y3lim = [300, 2400]

    # draw 3 yaxis graph
    savePath = './graph3yaxis2Lines'
    imageFormat = 'png' # pdf or png or jpeg or ...
    graph1d.timeShow = 'off' # 'on' or 'off'
    graph1d.legend = 'off'
    # graph1d.drawGraphs3yaxis(savePath, imageFormat)

    # set parameter
    graph1d.xlim = [3.5, 7.5]
    # select y_species or y_HRR or y_T or y_U or y_p
    graph1d.ax1Para = graph1d.y_species
    graph1d.y1speciesList = ['nC7H16', 'CO2', 'CO', 'CH2O']
    graph1d.y1colorList = ['r', 'b', 'g', 'c']
    graph1d.y1specieslim = [0, 0.2]
    graph1d.ax2Para = graph1d.y_T
    graph1d.y2lim = [300, 2400]

    # draw 2 yaxis graph
    savePath = './graph2yaxis2Lines'
    imageFormat = 'png' # pdf or png or jpeg or ...
    graph1d.timeShow = 'off' # 'on' or 'off'
    graph1d.legend = 'off'
    graph1d.drawGraphs2yaxis(savePath, imageFormat)

def runFFmpegPng():
    readDir = './graph2yaxis2Lines/Species_T_png'
    saveDir = './graph2yaxis2Lines'

    readFileName = 'graph%05d.png'
    saveFileName = 'graph'
    readPath = readDir +'/'+ readFileName
    savePath = saveDir +'/'+ saveFileName
    startNum = 0
    # framerate = 20
    framerateList = [10, 20, 30, 60]
    for framerate in framerateList:
        cmd = "ffmpeg -start_number {0} -r {1} -i {2} -pix_fmt yuv420p {3}{1}.mp4".format(startNum, framerate, readPath, savePath)
        subprocess.call(cmd.split())

    # readDirPath = './graph2yaxis2Lines/Species_T_png'
    # ffmpeg = postProcessMFR.FFmpeg(readDirPath)
    # ffmpeg.imageToMov('graph%05d.png', 'graph.mp4')

def runFFmpegQdot():
    readPath = './Qdot'
    ffmpeg = postProcessMFR.FFmpeg(readPath)
    ffmpeg.pngTrim()
    readDir = 'Qdot_trim'
    saveDir = './'
    readFileName = 'Qdot.%04d.png'
    saveFileName = 'Qdot'
    readPath = readDir +'/'+ readFileName
    savePath = saveDir +'/'+ saveFileName
    startNum = 0
    # framerate = 20
    framerateList = [10, 20, 30, 60]
    for framerate in framerateList:
        cmd = "ffmpeg -start_number {0} -r {1} -i {2} -pix_fmt yuv420p {3}{1}.mp4".format(startNum, framerate, readPath, savePath)
        subprocess.call(cmd.split())

def runPeak():
    readPath = './csv1d_y0.0'
    pp = postProcessMFR.PostPeak(readPath)
    startNum = 30
    endNum = 100
    deltaT=1/100
    fuelName='nC7H16'
    pp.setParameter(startNum, endNum, deltaT, fuelName)
    pp.  xlim = [3.5, 7.5]
    pp.peakNum = 2
    pp.showTwFunc = 'off'
    pp.showContour = 'off'
    savePath = './peak1d_y0.0_out'
    pp.detectPeakValue(savePath)
    # pp.detectMaxValue(savePath)

def getPropagetionSpeed():
    readPath = './csv1d_y0.0'
    ps = postProcessMFR.PropagationSpeed(readPath)
    startNum = 30
    endNum = 100
    deltaT=1/100
    fuelName='nC7H16'
    ps.setParameter(startNum, endNum, deltaT, fuelName)
    ps.maxLoc, ps.maxValue = ps.detectMaximumPeak(ps.dfList)
    ps.xlim = [3.5, 7.5]
    ps.saveDir = './peak1d_y0.0_out'
    ps.ylim = [-160, 100]
    ps.calcPropagatingSpeed()

if __name__ == '__main__':
    # runGraphPostProcess()
    # runFFmpegPng()
    # runFFmpegQdot()
    # runPeak()
    getPropagetionSpeed()


