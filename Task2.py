import arcpy

# Set workspace
arcpy.env.workspace = 'V:/ENV859_PS4/Data'

# Allow us to overwrite output
arcpy.env.overwriteOutput = True

# Creates a string variable containing the path to the Roads.shp feature class
Roads = "V:\ENV859_PS4\Data\Roads.shp"

# Creates a string variable with the value “0;201;203” (i.e. a “multi-value string”) of the road type class values to be processed.
RoadValues = "0;201;203"

# Splitting RoadValues between semi-colons to create a list variable
ValueList = RoadValues.split(";")

# Loop through each road type value in ValueList
for i in ValueList:
    # Define output fc to write using ValueList item
    out_feature_class = "V:/ENV859_PS4/Scratch/roads_{}.shp".format(i)
    # Select analysis
    arcpy.analysis.Select(Roads, out_feature_class, f'"ROAD_TYPE" = {i}')

        
