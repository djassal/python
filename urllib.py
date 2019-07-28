import urllib.request as req
import os
link = "http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample.csv.zip"
filename = link.split("/")[-1]
req.urlretrieve(link,filename)
print( filename,"is downloaded in",os.getcwd())