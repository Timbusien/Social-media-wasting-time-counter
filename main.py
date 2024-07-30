import pygetwindow
import psutil
import time


while True:
    windows = pygetwindow.getAllTitles()
    for window in windows:
        if 'Браузер' in window and 'YouTube' in window: #'Браузер' in window or 'YouTube' or 'Instagram' in window
            procs = psutil.process_iter(['pid', 'name'])
            for proc in procs:
                if proc.info['name'] == 'browser.exe':
                    proc.kill()
    time.sleep(1)

# import pygetwindow
# import psutil
# import time
#
# while True:
#
#     windows = pygetwindow.getAllTitles()
#
#     for window in windows:
#         if 'Браузер' in window and 'YouTube' in window:
#             procs = psutil.process_iter(['pid', 'name'])
#             for proc in procs:
#                 if proc.info['name'] == 'browser.exe':
#                     proc.kill()
#
#     time.sleep(1)
