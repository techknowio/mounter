#!/usr/bin/env python2.7
#########################################################
#               Techknow Mounter 0.0.1                  #
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
    url = "http://" + username +":"+password+"@192.168.99.13:80/webdav"
    if platform.system() == "Darwin":
        #osascript -e ' mount volume "http://192.168.99.13:80" '
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
        print "net use z: http://192.168.99.13:80/webdav /user:" + username + " " +password
        output = os.system("net use z: http://192.168.99.13:80/webdav /user:" + username + " " +password)
        if os.path.exists('z:') == False:
            tkMessageBox.showinfo("Error", "Username or Password Invalid")
            root.passwordtxt.delete(0, END)
        else:
            tkMessageBox.showinfo("Drive Connected", "Your Z Drive is now connected!")
            os.system('explorer /select,"z:\"')
            sys.exit(0)
def isUserAdmin():

    if os.name == 'nt':
        import ctypes
        # WARNING: requires Windows XP SP2 or higher!
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            print "Admin check failed, assuming not an admin."
            return False
    elif os.name == 'posix':
        # Check for root on Posix
        return os.getuid() == 0
    else:
        raise RuntimeError, "Unsupported operating system for this module: %s" % (os.name,)


def runAsAdmin(cmdLine=None, wait=True):

    if os.name != 'nt':
        raise RuntimeError, "This function is only implemented on Windows."

    import win32api, win32con, win32event, win32process
    from win32com.shell.shell import ShellExecuteEx
    from win32com.shell import shellcon

    python_exe = sys.executable

    if cmdLine is None:
        cmdLine = [python_exe] + sys.argv
    elif type(cmdLine) not in (types.TupleType,types.ListType):
        raise ValueError, "cmdLine is not a sequence."
    cmd = '"%s"' % (cmdLine[0],)
    # XXX TODO: isn't there a function or something we can call to massage command line params?
    params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
    cmdDir = ''
    showCmd = win32con.SW_SHOWNORMAL
    #showCmd = win32con.SW_HIDE
    lpVerb = 'runas'  # causes UAC elevation prompt.

    # print "Running", cmd, params

    # ShellExecute() doesn't seem to allow us to fetch the PID or handle
    # of the process, so we can't get anything useful from it. Therefore
    # the more complex ShellExecuteEx() must be used.

    # procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)

    procInfo = ShellExecuteEx(nShow=showCmd,
                              fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                              lpVerb=lpVerb,
                              lpFile=cmd,
                              lpParameters=params)

    if wait:
        procHandle = procInfo['hProcess']
        obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
        rc = win32process.GetExitCodeProcess(procHandle)
        #print "Process handle %s returned code %s" % (procHandle, rc)
    else:
        rc = None

    return rc

def buildGUI():
    photo = """ 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 """
    photo = PhotoImage(data=photo)
    root.title("Techknow Webdav Connector")
    root.logolbl = tk.Label(root,bg="black", image=photo, anchor=CENTER)

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
    rc = 0
    if not isUserAdmin():
        print "You're not an admin.", os.getpid(), "params: ", sys.argv
        auth = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,"SYSTEM\\CurrentControlSet\\Services\\WebClient\\Parameters")
        value, type = _winreg.QueryValueEx(auth, "BasicAuthLevel")
        _winreg.CloseKey(auth)
        if value == 2:
            buildGUI()
        else:
            rc = runAsAdmin()
    else:
        print "You are an admin!", os.getpid(), "params: ", sys.argv
        rc = 0
        auth = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,"SYSTEM\\CurrentControlSet\\Services\\WebClient\\Parameters")
        value, type = _winreg.QueryValueEx(auth, "BasicAuthLevel")
        _winreg.CloseKey(auth)
        if value != 2:
            auth = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,"SYSTEM\\CurrentControlSet\\Services\\WebClient\\Parameters",0,_winreg.KEY_ALL_ACCESS)
            _winreg.SetValueEx(auth, "BasicAuthLevel",0, _winreg.REG_DWORD, 0x00000002)
            _winreg.CloseKey(auth)
            tkMessageBox.showinfo("Restart", "You must restart your computer for changes to take affect")
            print "Changed the Value!"
        else:
            buildGUI()
