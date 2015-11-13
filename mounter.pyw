#!/usr/bin/env python2.7
#########################################################
#               Techknow Mounter 0.0.1.1                #
#    Mounts Webdav Volumes for the Techknow Classes     #
#         By John Hass <john@techknow.io>               #
#             License GPLv2 no Warrantys!               #
# https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt #
#########################################################
import Tkinter as tk
import os
import platform
from Tkinter import *
import tkMessageBox
if platform.system() == "Windows":
    import _winreg

import sys



def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()

    if platform.system == "Windows":
        width=253
        height=75
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def login(event=None):
    username = root.usernametxt.get().strip()
    password = root.passwordtxt.get().strip()
    if username == "" or password == "":
        tkMessageBox.showinfo("Error", "Username or Password Blank")
    #username and password aren't blank
    url = "https://" + username +":"+password+"@cloud.techknow.io"
    if platform.system() == "Darwin":
        print "/usr/bin/osascript -e 'mount volume "+url+"'"
        os.system("diskutil unmount /Volumes/webdav")
        output = os.system("/usr/bin/osascript -e 'mount volume \""+url+"\"'")
        if output != 0:
            tkMessageBox.showinfo("Error", "Username or Password Invalid")
            root.passwordtxt.delete(0, END)
        else:
            os.system("open /Volumes/webdav")
            tkMessageBox.showinfo("Volume Connected", "Your volume is now connected!")
            sys.exit(0)
    if platform.system() == "Windows":
        print "net use z: /delete"
        os.system("net use z: /delete")
        output = os.system("net use z: https://cloud.techknow.io /user:" + username + " " +password)
        if os.path.exists('z:') == False:
            tkMessageBox.showinfo("Error", "Username or Password Invalid")
            root.passwordtxt.delete(0, END)
        else:
            tkMessageBox.showinfo("Drive Connected", "Your Z Drive is now connected!")
            os.system('explorer /select,"z:\"')
            sys.exit(0)
#def isUserAdmin():
#
#    if os.name == 'nt':
#        import ctypes
#        # WARNING: requires Windows XP SP2 or higher!
#        try:
#            return ctypes.windll.shell32.IsUserAnAdmin()
#        except:
#            traceback.print_exc()
#            print "Admin check failed, assuming not an admin."
#            return False
#    elif os.name == 'posix':
#        # Check for root on Posix
#        return os.getuid() == 0
#    else:
#        raise RuntimeError, "Unsupported operating system for this module: %s" % (os.name,)
#
#
#def runAsAdmin(cmdLine=None, wait=True):
#
#    if os.name != 'nt':
#        raise RuntimeError, "This function is only implemented on Windows."
#
#    import win32api, win32con, win32event, win32process
#    from win32com.shell.shell import ShellExecuteEx
#    from win32com.shell import shellcon
#
#    python_exe = sys.executable
#
#    if cmdLine is None:
#        cmdLine = [python_exe] + sys.argv
#    elif type(cmdLine) not in (types.TupleType,types.ListType):
#        raise ValueError, "cmdLine is not a sequence."
#    cmd = '"%s"' % (cmdLine[0],)
#    # XXX TODO: isn't there a function or something we can call to massage command line params?
#    params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
#    cmdDir = ''
#    showCmd = win32con.SW_SHOWNORMAL
#    #showCmd = win32con.SW_HIDE
#    lpVerb = 'runas'  # causes UAC elevation prompt.
#
#    # print "Running", cmd, params
#
#    # ShellExecute() doesn't seem to allow us to fetch the PID or handle
#    # of the process, so we can't get anything useful from it. Therefore
#    # the more complex ShellExecuteEx() must be used.
#
#    # procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)
#
#    procInfo = ShellExecuteEx(nShow=showCmd,
#                              fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
#                              lpVerb=lpVerb,
#                              lpFile=cmd,
#                              lpParameters=params)
#
#    if wait:
#        procHandle = procInfo['hProcess']
#        obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
#        rc = win32process.GetExitCodeProcess(procHandle)
#        #print "Process handle %s returned code %s" % (procHandle, rc)
#    else:
#        rc = None
#
#    return rc

def buildGUI():
    photo = """ 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 """
    photo = PhotoImage(data=photo)
    root.title("Techknow Webdav Connector")
    root.logolbl = tk.Label(root, image=photo, anchor=CENTER)

    root.logolbl.grid(row=0,column=3,rowspan=3,columnspan=1, sticky="e")
    root.usernamelbl = tk.Label(root, text="Username")
    root.usernamelbl.grid(row=0)
    root.usernametxt = tk.Entry(root)
    root.usernametxt.grid(row=0,column=1,sticky="nsew",columnspan=2)
    root.usernametxt.focus()
    root.passwordlbl = tk.Label(root, text="Password")
    root.passwordlbl.grid(row=1)
    root.passwordtxt = tk.Entry(root,show="*")
    root.passwordtxt.grid(row=1,column=1,sticky="nsew")

    root.loginButton = tk.Button(root, text='Login Now',command=login)
    root.loginButton.grid(row=2,column=1,sticky="nsew")

    root.bind('<Return>', login)
    center(root)
    root.lift()
    root.mainloop()

print platform.system()
print os.path.exists('z:')
root = tk.Tk()
if platform.system() == "Windows":
    root.attributes("-toolwindow", 1)

if platform.system() == "Darwin":
    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    buildGUI()
if platform.system() == "Windows":
    buildGUI()
    #no longer need to runas in Python Keeping the code because it's cool!
    #rc = 0
    #if not isUserAdmin():
    #    print "You're not an admin.", os.getpid(), "params: ", sys.argv
    #    auth = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,"SYSTEM\\CurrentControlSet\\Services\\WebClient\\Parameters")
    #    value, type = _winreg.QueryValueEx(auth, "BasicAuthLevel")
    #    _winreg.CloseKey(auth)
    #    if value == 2:
    #        buildGUI()
    #    else:
    #        rc = runAsAdmin()
    #else:
    #    print "You are an admin!", os.getpid(), "params: ", sys.argv
    #    rc = 0
    #    auth = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,"SYSTEM\\CurrentControlSet\\Services\\WebClient\\Parameters")
    #    value, type = _winreg.QueryValueEx(auth, "BasicAuthLevel")
    #    _winreg.CloseKey(auth)
    #    if value != 2:
    #        auth = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,"SYSTEM\\CurrentControlSet\\Services\\WebClient\\Parameters",0,_winreg.KEY_ALL_ACCESS)
    #        _winreg.SetValueEx(auth, "BasicAuthLevel",0, _winreg.REG_DWORD, 0x00000002)
    #        _winreg.CloseKey(auth)
    #        tkMessageBox.showinfo("Restart", "You must restart your computer for changes to take affect")
    #        print "Changed the Value!"
    #    else:
    #        buildGUI()
