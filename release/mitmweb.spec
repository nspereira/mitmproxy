# -*- mode: python -*-

from PyInstaller.utils.hooks import collect_data_files

a = Analysis(['../mitmproxy/mitmweb'],
             binaries=None,
             datas=collect_data_files("libmproxy"),
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None)
pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mitmweb',
          debug=False,
          strip=None,
          upx=True,
          console=True )
