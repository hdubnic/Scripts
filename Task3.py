import arcpy
import sys

# Set workspace
arcpy.env.workspace = 'V:/ENV859_PS4/Data'

# Allow us to overwrite output
arcpy.env.overwriteOutput = True

# Check product
if arcpy.CheckProduct("ArcInfo") == "Available":
    print("Available!")
else: 
    print("Not available...")
    sys.exit()

# Make a list of all feature classes starting with "BMR"
# I used ChatGPT to troubleshoot incorrect code. "is there another python function I can use?"
# I originally tried to use ListFeatureClasses by itself - ChatGPT suggested creating an empty list and a seperate for loop.

# Creating list of all feature classes
all_fc = arcpy.ListFeatureClasses()

# Creating an empty list for feature classes starting with "BMR"
BMR_fc = []

# Looping through all feature classes and appending to the empty list if starting with "BMR"
for fc in all_fc:
    if fc.startswith("BMR"):
        BMR_fc.append(fc)

# Seeing if the for loop worked
print(BMR_fc)

# Loop through 5 "BMR" feature classes to create folders and split data by county features
for fc in BMR_fc: 
    folder = arcpy.CreateFolder_management("V:/ENV859_PS4/Scratch/", "{}_counties".format(fc))
    arcpy.analysis.Split(fc, "TriCounties.shp", "CO_NAME", folder)




    

