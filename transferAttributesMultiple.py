#import sys
#sys.path.append('C:\Users\glaucolonghi\Documents\maya\scripts\GLScripts')
#import transferAttributesMultiple as tam
#reload(tam);
#tam.menuWindow()

import sys
import maya.cmds as mc

Values = dict(valueA = 1, valueB = 1, option1 = False, option2 = False, TransferPosition = 0)


def printCommand(*args):

    print Values

def changeTo1A(*args):


    Values["valueA"] = 15
    Values["TransferPosition"] = 1
    visibility = mc.button(Values["option1"], query=True, enable=True)
 
    if visibility:
        visibility = not visibility
 
    mc.button(Values["option1"], edit=True, enable= visibility)
 
    print "value A has changed to 15"
 
 
def changeTo1B(*args):

    Values["valueB"] = 20
 
    visibility = mc.button(Values["option2"], query=True, enable=True)
 
    if visibility:
        visibility = not visibility
 
    mc.button(Values["option2"], edit=True, enable= visibility)
 
    print "value B has changed to 20"
 
 
def menuWindow():

 
    if mc.window("menuGL", query=True, exists=True):
        mc.deleteUI("menuGL", window=True)
    menu = mc.window("menuGL")
    mc.columnLayout()
#    mc.paneLayout(configuration="quad")
    Values["option1"] = mc.button(label="Option01", c=changeTo1A, enable=True)
    Values["option2"] = mc.button(label="Option02", c=changeTo1B, enable=True)
    mc.button(label="Print", command=printCommand)
    mc.button(label="RESET", command=reset)        
    mc.button(label="TransferAttributes", command=tas)
    mc.showWindow(menu)
 
 
def reset(*args):

    Values["valueA"] = 0
    Values["valueB"] = 0  

    mc.button(Values["option1"], edit=True, enable= True)
    mc.button(Values["option2"], edit=True, enable= True)
 
    print "values and buttons have been reset"

def tas(*args):

    #//Transfer Attributes to multiple objects
#select master object first

    # sel is = all selected

    sel = mc.ls(sl = True)

    # len returns the list values of an object - sel in this case

    if len(sel) <= 1:
        sys.exit('Please select at least 2 different polygonal objects.\n')

    # selectionMask 12 to make sure you select polygons

    selType = mc.filterExpand(selectionMask = 12)
    if selType == None:
        sys.exit("You did not select an polygonal object.\n")

    #for loop - x in range - starting on 1 because we are saving 0 as master, then running our sel list

    for x in range(1, len(sel)):
        mc.select(sel[0])
        mc.select(sel[x], add = True)
        mc.transferAttributes(sel[0], sel[x], transferPositions=Values["TransferPosition"], transferNormals=0, transferUVs=0, transferColors=0, sampleSpace=3, searchMethod=3, targetUvSet="map2", sourceUvSet="map1")
    # not necessary the use of else here
        if Values["TransferPosition"] == 1:
            print "deu certo"
            sys.stdout.write('Your Verts were transferred.\n')
            mc.deleteUI("menuGL")

            if mc.window("congrats", query=True, exists=True):
                mc.deleteUI("congrats", window=True)

            def delCongrats(*args):
                mc.deleteUI("congrats", window=True)

            congratsMenu = mc.window("congrats")
            mc.paneLayout()
            mc.button(label="DEU CERTO", command=delCongrats)
            mc.showWindow(congratsMenu)


        if Values["TransferPosition"] == 0:
            print "deu caca"

