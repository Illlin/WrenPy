import pkgutil 
pages = []
__path__ = pkgutil.extend_path(__path__, __name__)
for importer, modname, ispkg in pkgutil.walk_packages(path=__path__, prefix=__name__+'.'):
      __import__(modname)
      name = modname.split(".")[1:][0]
      pages.append((name,globals()[name]))
del ispkg, pkgutil, modname, importer, name