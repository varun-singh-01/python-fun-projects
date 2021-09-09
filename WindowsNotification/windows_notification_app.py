#  @author Varun Singh
#  @email admin@talkhash.com
#  @create date 2021-08-21 16:02:29
#  @modify date 2021-08-21 16:02:29
#  @desc Generates a windows notification

import os
import sys
from win10toast import ToastNotifier

def notification():
    # Change Directory to the script location
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    
    # Create ToastNotifier object that will be used to create a notification
    toast = ToastNotifier()
    
    # Setting title, message and icon of the notification for display
    title = "Hey there! You have one notification"
    message = "Follow GetRealWithPython group on Facebook!"
    length = 5
    toast.show_toast(title, message, duration=length)

notification()
sys.exit(0)