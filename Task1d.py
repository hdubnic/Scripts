import arcpy

# Set workspace
arcpy.env.workspace = 'V:/ENV859_PS4/Data'

# Allow us to overwrite output
arcpy.env.overwriteOutput = True

# Set local variables
in_features = "streams.shp"
out_feature_class = "V:/ENV859_PS4/Scratch/buff_1000m.shp"
buffDist = sys.argv[2] 

# Execute buffer
arcpy.Buffer_analysis(in_features, out_feature_class, buffDist, "", "", "ALL")

# display any messages, warnings, or errors to interactive console
print(arcpy.GetMessages())