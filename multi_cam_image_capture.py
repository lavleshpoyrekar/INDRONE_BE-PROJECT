from openpyxl import Workbook  
import time
import os 
from datetime import datetime
dir='/home/pi/indrone/test5/finalc1' 
wb = Workbook()  
sheet = wb.active 
n =0
sheet[f'A{n+1}'] = "Start time"
sheet[f'B{n+1}'] = "End time"
sheet[f'c{n+1}'] = "Total time required"
  

def function1():
          global n
          n += 1
          now = datetime.now().strftime('%H:%M:%S.%f')[:-3]
          
          sheet[f'A{n+1}'] = now
          # Execute i2cset command
          i2cset_cmd = 'i2cset -y 10 0x24 0x24 0x02'
          os.system(i2cset_cmd)

          # Execute libcamera-still command
          libcamera_cmd = f'libcamera-still --immediate --width 1920 --height 1080 -e png -o {dir}/f{n}.png --mode 3264:2448 --nopreview'
          os.system(libcamera_cmd)

          now = datetime.now().strftime('%H:%M:%S.%f')[:-3]
          sheet[f'B{n+1}'] = now

def function2():
          global n
          n += 1
          now = datetime.now().strftime('%H:%M:%S.%f')[:-3]
          sheet[f'A{n+1}'] = now
          i2cset_cmd = 'i2cset -y 10 0x24 0x24 0x12'
          os.system(i2cset_cmd)

          # Execute libcamera-still command
          libcamera_cmd = f'libcamera-still --immediate --width 1920 --height 1080 -e png  -o {dir}/ff{n}.png  --mode 3264:2448 --nopreview'
          os.system(libcamera_cmd)

          now = datetime.now().strftime('%H:%M:%S.%f')[:-3]
          sheet[f'B{n+1}'] = now


def function3():
          global n
          n += 1
          now = datetime.now().strftime('%H:%M:%S.%f')[:-3]
          sheet[f'A{n+1}'] = now
          i2cset_cmd = 'i2cset -y 10 0x24 0x24 0x22'
          os.system(i2cset_cmd)

          # Execute libcamera-still command
          libcamera_cmd = f'libcamera-still --immediate --width 1920 --height 1080 -e png  -o {dir}/ff{n}.png  --mode 3264:2448 --nopreview'
          os.system(libcamera_cmd)

          now = datetime.now().strftime('%H:%M:%S.%f')[:-3]
          sheet[f'B{n+1}'] = now
        
def function4():
          global n
          n += 1
          now = datetime.now().strftime('%H:%M:%S.%f')[:-3]
          sheet[f'A{n+1}'] = now
          i2cset_cmd = 'i2cset -y 10 0x24 0x24 0x32'
          os.system(i2cset_cmd)

          # Execute libcamera-still command
          libcamera_cmd = f'libcamera-still --immediate --width 1920 --height 1080 -e png  -o {dir}/ff{n}.png  --mode 3264:2448 --nopreview'
          os.system(libcamera_cmd)

          now = datetime.now().strftime('%H:%M:%S.%f')[:-3]
          sheet[f'B{n+1}'] = now

for i in range(5):
    function1()
    function2()
    function3()
    function4()
  

  
  
wb.save("sample_file205.xlsx")  
