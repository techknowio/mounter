; -- 64Bit.iss --
; Demonstrates installation of a program built for the x64 (a.k.a. AMD64)
; architecture.
; To successfully run this installation and the program it installs,
; you must have a "x64" edition of Windows.

; SEE THE DOCUMENTATION FOR DETAILS ON CREATING .ISS SCRIPT FILES!

[Setup]
AppName=Techknow WebDav Mounter
AppVersion=0.0.2
DefaultDirName={pf}\Techknow Webdav Mounter
DefaultGroupName=Techknow Webdav Mounter
UninstallDisplayIcon={app}\mounter.exe
Compression=lzma2
SolidCompression=yes
;OutputDir=userdocs:Inno Setup Examples Output
; "ArchitecturesAllowed=x64" specifies that Setup cannot run on
; anything but x64.
ArchitecturesAllowed=x64
; "ArchitecturesInstallIn64BitMode=x64" requests that the install be
; done in "64-bit mode" on x64, meaning it should use the native
; 64-bit Program Files directory and the 64-bit view of the registry.
ArchitecturesInstallIn64BitMode=x64

[Files]
DestDir: {app}; Source: C:\Users\John\Desktop\dist\*; Excludes: "*.m,.svn,private"; Flags: recursesubdirs

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "Do you want to create desktop icon?"; Flags: checkablealone

[Icons]
Name: "{group}\Techknow Webdav Mounter"; Filename: "{app}\mounter.exe"
Name: "{commondesktop}\Techknow Webdav Mounter"; Filename: "{app}\mounter.exe"; Tasks: desktopicon; IconFilename: "C:\Users\John\Desktop\icon.ico"