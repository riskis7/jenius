#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy
__title__ = "Jenius (Play Video with QPython)"
__doc__ ="""
This is an example script which teach you how to use jnius to call android APIs from QPython.

@Author: riskis7
@Date: 2018-07-21
"""

try:
    import androidhelper
    droid = androidhelper.Android()
except:
    pass

def first_welcome():
    msg = __doc__+"\n\n"\
        +"To run it, you need install Pyjnius and Android library from QPYPI first"
    droid.dialogCreateAlert(__title__, msg)
    droid.dialogSetPositiveButtonText('OK')
    droid.dialogSetNegativeButtonText('NO')
    droid.dialogShow()
    response = droid.dialogGetResponse().result
    if response['which'] == 'positive':
        sys.exit()

    else:
        sys.exit()


try:
    import jnius
except ImportError:
    first_welcome()

from jnius import cast
from jnius import autoclass
from jnius import JavaException
from android import AndroidBrowser
from urllib2 import urlopen

print("[Play Video with qpython]")

# get and parse video link
response = urlopen('http://www.qpython.org/a8.json')
if response:
    content = response.read()
    import json
    data = json.loads(content)
    link = data['link']

    # get android object
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')
    Uri = autoclass('android.net.Uri')
    Toast = autoclass('android.widget.Toast')


    # play the url
    intent = Intent()
    intent.setAction(Intent.ACTION_VIEW)
    intent.setDataAndType(Uri.parse(link), 'video/*')
    currentActivity = cast('android.app.Activity', PythonActivity.mActivity)

    try:
        s = "Play Video: %s..." % link
        print(s)
        currentActivity.startActivity(intent)
    except JavaException:
        s = "Need install A8 Player App first"
        browser = AndroidBrowser()
        browser.open("http://play.tubebook.net/a8-video-player.html")

else:

    print("Maybe network error, could not get the parameters for play")
