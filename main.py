import webview
from com.application import create_app

if __name__ == '__main__':
    app = create_app(__name__)
    window = webview.create_window(
        title='HA Monitor',
        url=app,
        confirm_close=True
    )
    cn = {
        'global.quitConfirmation': u'确定关闭窗口?'
    }
    webview.start(localization=cn, gui='mshtml', debug=False)
