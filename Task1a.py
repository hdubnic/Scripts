import arcpy

# Set workspace
arcpy.env.workspace = 'V:/ENV859_PS4'

# Set local variables
in_features = "V:/ENV859_PS4/Data/streams.shp"
out_feature_class = 'V:/ENV859_PS4/Scratch'
buffDist = "1000 meters"

# Execute buffer
arcpy.Buffer_analysis(in_features, out_feature_class, buffDist, "", "", "PLANAR", "ALL")

# display any messages, warnings, or errors to interactive console
print(arcpy.GetMessages())