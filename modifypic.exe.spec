# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
add_files = [ ('./RFB.ui', '.'), ('./img/duck.png', '.') ]

a = Analysis(['main.py'],
             pathex=['/Users/raffin/PycharmProjects/modifier_pic'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          icon='./duck.png',
          name='modifypic.exe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
app = BUNDLE(exe,
             name='modifypic.exe.app',
             icon=None,
             bundle_identifier=None)
