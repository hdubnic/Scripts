import arcpy

# Set workspace
arcpy.env.workspace = 'V:/ENV859_PS4/Data'

# Allow us to overwrite output
arcpy.env.overwriteOutput = True

# Get describe object
inFC = arcpy.GetParameterAsText(0)
desc = arcpy.da.Describe(inFC)

# Indicate the dataset's catalogPath property 
print("CatalogPath: " + desc["catalogPath"])

# Report XMin, XMax, YMin, and YMax properties of the dataset's extent object
extent = desc["extent"] # Assigning a string variable to the extent key in desc library
arcpy.AddMessage(((" XMin: {0}\n XMax: {1}\n YMin: {2}\n YMax: {3}".format(extent.XMin, extent.XMax, extent.YMin, extent.YMax))))  # Accessing values associated with extent key

# Check datasetType of our dataset
dataset_type = desc["dataType"] # "dataType" in brackets because it is a key in a dictionary

if dataset_type == "RasterDataset":
    # Assigning string variables to dictionary key and attributes of interest
    f = desc["format"]
    rows = arcpy.GetRasterProperties_management(inFC, "ROWCOUNT") # Searched for this function via Google
    columns = arcpy.GetRasterProperties_management(inFC, "COLUMNCOUNT")

    arcpy.AddWarning("Format: {}".format(f))
    arcpy.AddWarning("# of rows: {}".format(rows))
    arcpy.AddWarning("# of columns: {}".format(columns))

if dataset_type == "ShapeFile":
    s = desc["shapeType"]
    arcpy.AddWarning("Shape Type: {}".format(s)) 

if dataset_type not in ["RasterDataset","ShapeFile"]:
    arcpy.AddError("Dataset Type: {}".format(dataset_type)) 

# Note: each time I encoutnered an error, I pasted it into ChatGPT to troubleshoot the issue. I did not copy and paste solutions into my code. Rather, I cross-referenced ChatGPT, the class github page, and ESRI webpages to come to a solution. 