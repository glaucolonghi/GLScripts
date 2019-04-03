#import sys
#sys.path.append('C:\Users\glaucolonghi\Documents\maya\scripts\GLScripts')
#import transferAttributesMultiple as tam
#reload(tam);
#tam.menuWindow()

import sys
import maya.cmds as mc

Values = dict(TransferPosition = 0, VertexPositionB = None, TransferUVs = 0, TransferUVB = None)


def printCommand(*args):

    print Values

def TransferVP(*args):

    Values["TransferPosition"] = 1
    mc.button(Values["VertexPositionB"], edit=True, enable = False)
    print "TransferVertexPositionActive"

def TransferUV(*args):

    Values["TransferUVs"] = 1
    mc.button(Values["TransferUVB"], edit=True, enable = False)
    print "TransferUV Active"

def menuWindow():

 
    if mc.window("menuGL", query=True, exists=True):
        mc.deleteUI("menuGL", window=True)
    menu = mc.window("menuGL")
    mc.columnLayout()
#    mc.paneLayout(configuration="quad")
    Values["VertexPositionB"] = mc.button(label="VertexPosition", c=TransferVP, enable=True)
    Values["TransferUVB"] = mc.button(label="TransferUV", c=TransferUV, enable=True)
    mc.button(label="RESET", command=reset)        
    mc.button(label="TransferAttributes", command=tas)
    mc.button(label="DEBUG", command=printCommand)
    mc.showWindow(menu)
 
def reset(*args):

    Values["TransferPosition"] = 0
    Values["TransferUVs"] = 0

    mc.button(Values["VertexPositionB"], edit=True, enable= True)
    mc.button(Values["TransferUVB"], edit=True, enable= True)
 
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
        mc.transferAttributes(sel[0], sel[x], transferPositions=Values["TransferPosition"], transferNormals=0, transferUVs=Values["TransferUVs"], transferColors=0, sampleSpace=3, searchMethod=3, targetUvSet="map2", sourceUvSet="map1")
    # not necessary the use of else here
    else:
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
            mc.button(label="VERTEX POSITION WAS TRANSFERED", command=delCongrats)
            mc.showWindow(congratsMenu)


        if Values["TransferUVs"] == 1:
            print "Transfered UVS"
            sys.stdout.write('Your UVS were transferred.\n')
            mc.deleteUI("menuGL")

            if mc.window("congratsUVS", query=True, exists=True):
                mc.deleteUI("congratsUVS", window=True)

            def delCongrats(*args):
                mc.deleteUI("congratsUVS", window=True)

            congratsMenuUVS = mc.window("congratsUVS")
            mc.paneLayout()
            mc.button(label="UVS WERE TRANSFERED :)", command=delCongrats)
            mc.showWindow(congratsMenuUVS)

