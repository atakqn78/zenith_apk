[app]

# (str) Title of your application
title = Zenith

# (str) Package name
package.name = zenith

# (str) Package domain (needed for android packaging)
package.domain = org.zenith

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion patterns relative to the root directory
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let it empty to exclude nothing)
source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to exclude nothing)
source.exclude_dirs = tests, bin, .git, .github

# (list) List of exclusions in glob format
source.exclude_patterns = license,images/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (list) Custom source folders for dependencies
# Do not clobber
#requirements.source_dirs = ../=ext_dir

# (list) Permissions
#android.permissions = INTERNET

# (list) features (adds uses-feature -tags to manifest)
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AABB will support.
android.minapi = 24

# (int) Android SDK version to use
android.sdk = 33

# (str) Android Build Tools version to use (Sabitlendi - aidl hatasi icin)
android.build_tools_version = 33.0.0

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API your app will support, it should match your minapi.
#android.ndk_api = 21

# (str) ANT directory (if empty, it will be automatically downloaded)
#android.ant_path =

# (bool) If True, then try to attempt to update the Android SDK
#android.sdk_update = False

# (str) If using_jarjar is True, specify absolute path to jarjar.jar
#android.jarjar_path =

# (list) python-for-android branch
# p4a.branch = master

# (str) OUYA Console category. Should be either "NO|GAME|APP"
#android.ouya.category = GAME

# (str) OUYA Console icon path. (656x328)
#android.ouya.icon_path = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity>
#android.intent_filters =

# (list) Copy global manifests to the target
#android.manifest_copy_to_native =

# (str) Private key for signing (release mode)
#android.private_key =

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (bool) enables Android auto backup feature (Android API >= 23)
android.allow_backup = True

# (str) The format used to package the app for release/debug (aab or apk).
android.format = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1

# (str) Path to build artifact, local or remote
bin_dir = ./bin

# (str) Number of recent builds to keep in bin_dir (-1 = data is not limited)
#android.build_tools_version = 33.0.0

