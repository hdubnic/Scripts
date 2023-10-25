import arcpy

# Set workspace
arcpy.env.workspace = 'V:/ENV859_PS4/Data'

# Allow us to overwrite output
arcpy.env.overwriteOutput = True

# Set local variables
in_features = "streams.shp"
out_feature_class = sys.argv[1] # in JSON file - "args":["V:/ENV859_PS4/Scratch/StrmBuff1km.shp", "1000 meters"] 
buffDist = sys.argv[2] 

# Execute buffer
arcpy.Buffer_analysis(in_features, out_feature_class, buffDist, "", "", "ALL")

# display any messages, warnings, or errors to interactive console
print(arcpy.GetMessages())