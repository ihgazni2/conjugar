#pip3 uninstall main
pip3 uninstall conjugar
git rm -r dist
git rm -r build
#git rm -r edict.egg-info
git rm -r conjugar.egg-info
rm -r dist
rm -r build
#rm -r elist.egg-info
rm -r conjugar.egg-info
git add .
git commit -m "remove old build"
