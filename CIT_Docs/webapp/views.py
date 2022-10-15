from flask import Blueprint,render_template

views = Blueprint('views',__name__)
'''
@views.route('/')
def home():
    return render_template('home.html')



@views.route('/helpdesk')
def helpdesk():
    return render_template('helpdesk.html') 
'''

@views.route('/windows')
def windows():
    return render_template('windows.html')

@views.route('/')
def base():
    return render_template('base.html')

@views.route('/fs')
def fs():
    return render_template('fs.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')
##### GHD

@views.route('/intune')
def intune():
    return render_template('intune.html')

@views.route('/shared')
def shared():
    return render_template('shared.html')

@views.route('/b2b')
def b2b():
    return render_template('b2b.html')

@views.route('/vpn')
def vpn():
    return render_template('vpn.html')

@views.route('/pbx')
def pbx():
    return render_template('pbx.html')

@views.route('/sbn')
def sbn():
    return render_template('sbn.html')

@views.route('/sws')
def sws():
    return render_template('sws.html')

@views.route('/monitoring')
def monitoring():
    return render_template('monitoring.html')

@views.route('/sysaid')
def sysaid():
    return render_template('sysaid.html')

@views.route('/lotus')
def lotus():
    return render_template('lotus.html')

##### FS_DE
@views.route('/bitlocker')
def bitlocker():
    return render_template('bitlocker.html')

@views.route('/unlock')
def unlock():
    return render_template('unlock.html')

@views.route('/2FA')
def twoFactor():
    return render_template('2FA.html')

@views.route('/DE_shared')
def de_shared():
    return render_template('DE_shared.html')

@views.route('/Citrix')
def citrix():
    return render_template('citrix.html')

@views.route('/xpert')
def xpert():
    return render_template('xpert.html')

@views.route('/external')
def external():
    return render_template('external.html')
@views.route('/elearning')
def e_learning():
    return render_template('elearning.html')

