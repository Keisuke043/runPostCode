# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
xxxfoam = OpenFOAMReader(FileName='/Volumes/G-DRIVE USB-C/calculationResultFromSC/Lu/u25x10000/xxx.foam')
xxxfoam.MeshRegions = ['internalMesh']
xxxfoam.CellArrays = ['C2H2', 'C2H3', 'C2H3CHO', 'C2H3CO', 'C2H4', 'C2H5', 'C2H5CHO', 'C2H5CO', 'C2H5COCH2', 'C2H5O', 'C2H6', 'C3H2', 'C3H3', 'C3H4-a', 'C3H5-a', 'C3H5O', 'C3H6', 'C4H6', 'C4H7', 'C4H7O', 'C4H8-1', 'C4H8OOH1-3', 'C4H8OOH1-3O2', 'C5H10-1', 'C5H9', 'C7H14-2', 'C7H14-3', 'C7H14O1-3', 'C7H14O2-4', 'C7H14OOH1-3', 'C7H14OOH1-3O2', 'C7H14OOH2-3', 'C7H14OOH2-4', 'C7H14OOH2-4O2', 'C7H14OOH3-2', 'C7H14OOH3-4', 'C7H14OOH3-5', 'C7H14OOH3-5O2', 'C7H14OOH4-2', 'C7H14OOH4-2O2', 'C7H14OOH4-3', 'C7H15-1', 'C7H15-2', 'C7H15-3', 'C7H15-4', 'C7H15O2-1', 'C7H15O2-2', 'C7H15O2-3', 'C7H15O2-4', 'CH2(s)', 'CH2CHO', 'CH2CO', 'CH2O', 'CH3', 'CH3CHO', 'CH3CO', 'CH3COCH2', 'CH3O', 'CH3O2', 'CH3O2H', 'CH4', 'CO', 'CO2', 'H', 'H2', 'H2O', 'H2O2', 'HCCO', 'HCO', 'HO2', 'N2', 'O', 'O2', 'OH', 'Qdot', 'T', 'U', 'nC3H7', 'nC3H7CHO', 'nC3H7CO', 'nC3H7COCH2', 'nC4H9CHO', 'nC4H9CO', 'nC4ket13', 'nC7H16', 'nC7ket13', 'nC7ket24', 'nC7ket35', 'nC7ket42', 'p', 'pC4H9', 'pC4H9O2']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on xxxfoam
xxxfoam.CellArrays = ['O2', 'Qdot']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2262, 2196]

# show data in view
xxxfoamDisplay = Show(xxxfoam, renderView1)

# trace defaults for the display properties.
xxxfoamDisplay.Representation = 'Surface'
xxxfoamDisplay.ColorArrayName = [None, '']
xxxfoamDisplay.OSPRayScaleArray = 'O2'
xxxfoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
xxxfoamDisplay.SelectOrientationVectors = 'None'
xxxfoamDisplay.ScaleFactor = 0.010000000149011612
xxxfoamDisplay.SelectScaleArray = 'None'
xxxfoamDisplay.GlyphType = 'Arrow'
xxxfoamDisplay.GlyphTableIndexArray = 'None'
xxxfoamDisplay.GaussianRadius = 0.0005000000074505806
xxxfoamDisplay.SetScaleArray = ['POINTS', 'O2']
xxxfoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
xxxfoamDisplay.OpacityArray = ['POINTS', 'O2']
xxxfoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
xxxfoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
xxxfoamDisplay.SelectionCellLabelFontFile = ''
xxxfoamDisplay.SelectionPointLabelFontFile = ''
xxxfoamDisplay.PolarAxes = 'PolarAxesRepresentation'
xxxfoamDisplay.ScalarOpacityUnitDistance = 0.0010000501164298173

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
xxxfoamDisplay.DataAxesGrid.XTitleFontFile = ''
xxxfoamDisplay.DataAxesGrid.YTitleFontFile = ''
xxxfoamDisplay.DataAxesGrid.ZTitleFontFile = ''
xxxfoamDisplay.DataAxesGrid.XLabelFontFile = ''
xxxfoamDisplay.DataAxesGrid.YLabelFontFile = ''
xxxfoamDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
xxxfoamDisplay.PolarAxes.PolarAxisTitleFontFile = ''
xxxfoamDisplay.PolarAxes.PolarAxisLabelFontFile = ''
xxxfoamDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
xxxfoamDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0

# set scalar coloring
ColorBy(xxxfoamDisplay, ('POINTS', 'Qdot'))

# rescale color and/or opacity maps used to include current data range
xxxfoamDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
xxxfoamDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Qdot'
qdotLUT = GetColorTransferFunction('Qdot')
qdotLUT.RGBPoints = [0.0, 0.278431372549, 0.278431372549, 0.858823529412, 1630328640.5119998, 0.0, 0.0, 0.360784313725, 3249256381.4399996, 0.0, 1.0, 1.0, 4890985921.536, 0.0, 0.501960784314, 0.0, 6509913662.464, 1.0, 1.0, 0.0, 8140242302.976, 1.0, 0.380392156863, 0.0, 9770570943.487999, 0.419607843137, 0.0, 0.0, 11400899584.0, 0.878431372549, 0.301960784314, 0.301960784314]
qdotLUT.ColorSpace = 'RGB'
qdotLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Qdot'
qdotPWF = GetOpacityTransferFunction('Qdot')
qdotPWF.Points = [0.0, 0.0, 0.5, 0.0, 11400899584.0, 1.0, 0.5, 0.0]
qdotPWF.ScalarRangeInitialized = 1

# rescale color and/or opacity maps used to exactly fit the current data range
xxxfoamDisplay.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
qdotLUT.RescaleTransferFunction(0.0, 10000000000.0)

# Rescale transfer function
qdotPWF.RescaleTransferFunction(0.0, 10000000000.0)

# Rescale transfer function
qdotLUT.RescaleTransferFunction(1.0, 10000000000.0)

# Rescale transfer function
qdotPWF.RescaleTransferFunction(1.0, 10000000000.0)

# convert to log space
qdotLUT.MapControlPointsToLogSpace()

# Properties modified on qdotLUT
qdotLUT.UseLogScale = 1

# get color legend/bar for qdotLUT in view renderView1
qdotLUTColorBar = GetScalarBar(qdotLUT, renderView1)
qdotLUTColorBar.Title = 'Qdot'
qdotLUTColorBar.ComponentTitle = ''
qdotLUTColorBar.TitleFontFile = ''
qdotLUTColorBar.LabelFontFile = ''

# change scalar bar placement
qdotLUTColorBar.WindowLocation = 'AnyLocation'
qdotLUTColorBar.Position = [0.8686599223946785, 0.020491803278688547]
qdotLUTColorBar.ScalarBarLength = 0.3299999999999999

# hide color bar/color legend
xxxfoamDisplay.SetScalarBarVisibility(renderView1, False)

# Properties modified on renderView1
renderView1.Background = [1.0, 1.0, 1.0]

# create a new 'Reflect'
reflect1 = Reflect(Input=xxxfoam)

# Properties modified on reflect1
reflect1.Plane = 'Y Min'

# show data in view
reflect1Display = Show(reflect1, renderView1)

# trace defaults for the display properties.
reflect1Display.Representation = 'Surface'
reflect1Display.ColorArrayName = ['POINTS', 'Qdot']
reflect1Display.LookupTable = qdotLUT
reflect1Display.OSPRayScaleArray = 'O2'
reflect1Display.OSPRayScaleFunction = 'PiecewiseFunction'
reflect1Display.SelectOrientationVectors = 'None'
reflect1Display.ScaleFactor = 0.010000000149011612
reflect1Display.SelectScaleArray = 'None'
reflect1Display.GlyphType = 'Arrow'
reflect1Display.GlyphTableIndexArray = 'None'
reflect1Display.GaussianRadius = 0.0005000000074505806
reflect1Display.SetScaleArray = ['POINTS', 'O2']
reflect1Display.ScaleTransferFunction = 'PiecewiseFunction'
reflect1Display.OpacityArray = ['POINTS', 'O2']
reflect1Display.OpacityTransferFunction = 'PiecewiseFunction'
reflect1Display.DataAxesGrid = 'GridAxesRepresentation'
reflect1Display.SelectionCellLabelFontFile = ''
reflect1Display.SelectionPointLabelFontFile = ''
reflect1Display.PolarAxes = 'PolarAxesRepresentation'
reflect1Display.ScalarOpacityFunction = qdotPWF
reflect1Display.ScalarOpacityUnitDistance = 0.0007938592620418341

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
reflect1Display.DataAxesGrid.XTitleFontFile = ''
reflect1Display.DataAxesGrid.YTitleFontFile = ''
reflect1Display.DataAxesGrid.ZTitleFontFile = ''
reflect1Display.DataAxesGrid.XLabelFontFile = ''
reflect1Display.DataAxesGrid.YLabelFontFile = ''
reflect1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
reflect1Display.PolarAxes.PolarAxisTitleFontFile = ''
reflect1Display.PolarAxes.PolarAxisLabelFontFile = ''
reflect1Display.PolarAxes.LastRadialAxisTextFontFile = ''
reflect1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(xxxfoam, renderView1)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# hide color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, False)

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

#change interaction mode for render view
renderView1.InteractionMode = '3D'

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.05000000074505806, 0.0, 0.013398785584581652]
renderView1.CameraFocalPoint = [0.05000000074505806, 0.0, 0.0]
renderView1.CameraParallelScale = 0.0023685956495695924

# save animation
SaveAnimation('/Users/keisuke/work/postOF/Lu/x10000r100/Qdot/Qdot.png', renderView1, ImageResolution=[2212, 160],
    FrameWindow=[0, 102])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.05000000074505806, 0.0, 0.013398785584581652]
renderView1.CameraFocalPoint = [0.05000000074505806, 0.0, 0.0]
renderView1.CameraParallelScale = 0.0023685956495695924

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).