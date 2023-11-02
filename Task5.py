import arcpy 

# Set workspace
arcpy.env.workspace = 'V:/ENV859_PS4/Data'

# Allow us to overwrite output
arcpy.env.overwriteOutput = True

# User input
feature_class = "TriCounties.shp"   # arcpy.GetParameterAsText(0)
fc_field_name = "CO_NAME"   # arcpy.GetParameterAsText(1)

# Create a point object
x = 621000
y = 254000
point = arcpy.Point(x, y)

# Create a search cursor
rows = arcpy.da.SearchCursor(feature_class, [fc_field_name, "Shape@"])

# This chunk of code was pulled from ChatGPT, I queried: "At value =, I want to determine the value of fc_field_name" and "How do I know what index each value is at?"
for row in rows:
    recShape = row[1] 
    if point.within(recShape):  
        value = row[0]
        arcpy.AddMessage("Field Value: {}".format(value)) 


