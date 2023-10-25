import arcpy

# Set workspace
arcpy.env.workspace = 'V:/ENV859_PS4/Data'

# Allow us to overwrite output
arcpy.env.overwriteOutput = True

# Create list of buffer distance values
buffDists = ["100", "200", "300", "400", "500"]

#ChatGPT referenced to debug code (pasted for loop, no question posed) - removed "meters" from buffDists list, and specified meters in buffer analysis tool
#Iterate through buffDists
for i in buffDists:

    # Set local variables
    in_features = "streams.shp"
    out_feature_class = "V:/ENV859_PS4/Scratch/buff_{}m.shp".format(i)

    # Execute buffer
    arcpy.Buffer_analysis(in_features, out_feature_class, "{} Meters".format(i), "", "", "ALL")

    # display any messages, warnings, or errors to interactive console
    print(arcpy.GetMessages())