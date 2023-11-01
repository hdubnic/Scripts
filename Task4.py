import arcpy

# Set workspace
arcpy.env.workspace = 'V:/ENV859_PS4/Data'

# Allow us to overwrite output
arcpy.env.overwriteOutput = True

inFC = 'counties.img'       #arcpy.GetParameterAsText(0)
outFC =       #arcpy.GetParameterAsText(1)

desc = arcpy.da.Describe(inFC)

# Indicate the catalog path property 

print("Feature Type:  " + desc.featureType)