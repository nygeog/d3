import pandas as pd 
import shutil

print 'copy data'

srcCSV = '/Users/danielmsheehan/Dropbox/GIS/Data/Monitoring/JawboneUp/20132014mw.csv'
desCSV = '/Users/danielmsheehan/GitHub/d3/jawbone_weather_graph/data/20132014mw.csv'
midCSV = '/Users/danielmsheehan/GitHub/d3/jawbone_weather_graph/data/20132014mw_working.csv'
midJSN = '/Users/danielmsheehan/GitHub/d3/jawbone_weather_graph/data/20132014mw_working.json'

shutil.copy2(srcCSV, desCSV)

df = pd.read_csv(desCSV)

print 'clean up'
df = df[['DATE','m_active_time','m_distance','tempmean','tempmax','tempmin','precip','snow']] #'date',

print 'export to csv and json'
df.to_csv(midCSV, index=False)
df.to_json(midJSN)
