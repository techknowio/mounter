from distutils.core import setup
import py2exe
setup(windows=[
		{
			"script" :"c:\\Users\\John\\Desktop\\mounter.pyw",
			"icon_resources":[(1, "icon.ico")]
		}
	]
)