#!/usr/bin/env python3

import os
import subprocess
from shutil import copy2

os.chdir("out/template")

subprocess.run(['./gradlew', 'assembleRelease'])
subprocess.run(['./gradlew', 'uploadCrashlyticsSymbolFileRelease'])

#subprocess.run(['adb', 'install', '-r', 'app/build/outputs/apk/release/app-release.apk'])

