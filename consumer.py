#!/usr/bin/python

import subprocess
import re
import sys
import time
import datetime
import gspread

# ===========================================================================
# Google Account Details
# ===========================================================================

# Account details for google docs
email       = 'runeorion@gmail.com'
password    = 'orionpentagon73'
spreadsheet = 'odroid'

# ===========================================================================
# Example Code
# ===========================================================================


# Login with your Google account
try:
  gc = gspread.login(email, password)
except:
  print "Unable to log in.  Check your email address/password"
  sys.exit()

# Open a worksheet from your spreadsheet using the filename
try:
  worksheet = gc.open(spreadsheet).sheet1
  # Alternatively, open a spreadsheet using the spreadsheet's key
#   worksheet = gc.open_by_key('0AuDEvmLA4ezadFlwMTRHSlVoMExNRVpDNlFlZlZHU1E')
except:
  print "Unable to open the spreadsheet.  Check your filename: %s" % spreadsheet
  sys.exit()

# Continuously append data
while(True):
  # Run the DHT program to get the humidity and temperature readings!

  output = subprocess.check_output(["tshark", "-i", "mon0", "subtype", "probereq", "and", "not", "wlan", "host", "c8:3a:35:c8:e5:fb", "-T", "fields", "-e", "wlan.sa", "-c", "10"]);
  print output
#  from subprocess import call
#  output =  call(["tshark", "-i", "mon0", "subtype", "probereq", "-T", "fields", "-e", "frame.time", "-e", "wlan.sa", "-e", "radiotap.dbm_antsignal", "-c", "10"]); 
#  print output
#  matches = re.search("(?<=:)\w+", output)
 # if (not matches):
 #	time.sleep(3)
 #	continue
#  	temp = float(matches.group(1))
     #  temp = float(output) 
  # search for humidity printout
 # matches = re.search("\s+([0-9]+)", output)
 # if (not matches):
  #	time.sleep(3)
  #	continue
 #	humidity = float(matches.group(1))

#  print "Mac Address: %.1f C" % temp
#  print "Signal Strength:    %.1f %%" % humidity
 
  # Append the data in the spreadsheet, including a timestamp
  try:
#    cell_list = worksheet.range('A1:A10')
#    for cell in cell_list:
#	cell.value = [datetime.datetime.now(), temp]
#    worksheet.update_cells(cell_list)
#   values = [datetime.datetime.now(), temp]
#    worksheet.update_cell(1, 2, 3,output)
    alternative = worksheet.row_count + 1
    print alternative
    values = [datetime.datetime.now(), output, '=SPLIT(SUBSTITUTE(B%s,CHAR(10), "@"),"       -@")' % alternative]
    worksheet.append_row(values)
  except:
    print "Unable to append data.  Check your connection?"
    subprocess.call(["sudo", "python", "consumer.py"])

  # Wait 30 seconds before continuing
  print "Wrote a row to %s" % spreadsheet
  time.sleep(1)
