import arcpy

# Set workspace
arcpy.env.workspace = 'V:/ENV859_PS4/Data'

# Allow us to overwrite output
arcpy.env.overwriteOutput = True

# Assign string variable to dataset of interest (in this case, I chose raster)
inFC = 'counties.img' 

# Get describe object
desc = arcpy.da.Describe(inFC)

# Indicate the dataset's catalogPath property 
print("CatalogPath: " + desc["catalogPath"])

# Report XMin, XMax, YMin, and YMax properties of the dataset's extent object
 extent = desc["extent"] # Assigning a string variable to the extent key in desc library
 print(("Extent: XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(extent.XMin, extent.XMax, extent.YMin, extent.YMax)))  # Accessing values associated with extent key
    #arcpy.AddMessage()

# Check datasetType of our dataset
dataset_type = desc["dataType"] # "dataType" in brackets because it is a key in a dictionary

if dataset_type == "RasterDataset":
    # Assigning string variables to dictionary key and attributes of interest
    f = desc["format"]
    rows = arcpy.GetRasterProperties_management(inFC, "ROWCOUNT") # Searched for this function via Google
    columns = arcpy.GetRasterProperties_management(inFC, "COLUMNCOUNT")

    print("Format: {}".format(f)) #arcpy.AddWarning
    print("# of rows: {}".format(rows)) # arcpy.AddWarning
    print("# of columns: {}".format(columns)) # arcpy.AddWarning

if dataset_type == "FeatureClass":
    s = desc["shapeType"]
    print("Shape Type: {}".format(s)) # arcpy.AddWarning

if dataset_type not in ["RasterDataset","FeatureClass"]:
     print("Dataset Type: {}".format(dataset_type)) # arcpy.AddError

# Note: each time I encoutnered an error, I pasted it into ChatGPT to troubleshoot the issue. I did not copy and paste solutions into my code. Rather, I cross-referenced ChatGPT, the class github page, and ESRI webpages to come to a solution. 