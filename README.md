#### Setup

Clone this repo as ~/Application Support/Sublime Text 2/Packages/User

#### Install Package Control

Open the console (cntl-`) and paste:

    import urllib2,os; pf='Package Control.sublime-package'; ipp=sublime.installed_packages_path(); os.makedirs(ipp) if not os.path.exists(ipp) else None; urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler())); open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read()); print('Please restart Sublime Text to finish installation')

Once ST2 opens, Package Control will install/update all the packages in `Package Control.sublime-settings`

#### License ST2

  Help > Enter License



