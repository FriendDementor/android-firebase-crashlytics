# Simple templated android ndk repository
This was maked for help to implement the Firebase Crashlytics SDK
on a big projec where the simbols don't appears on release builds

## Requirements
To build this project do you need python3 on you system
Also do you need jinja2 installed with pip3

Once you have that, you need create .local folder with two files

### config.json

This file is for sign the apk on release builds. You can create this
with Android Studio on ```Build > Generate Signed Bundle / APK... ```
tool.

```json
{
    "signing": {
        "storeFile": "<path to keystorage>",
        "storePassword": "<store password>",
        "keyAlias": "<key alias>",
        "keyPassword": "<key password>"
    }
}

```

### google-services.json
This file should be generated on Firebase console and can be downloaded from there


## Make the project
With the files on .local folder you can run ```./generate.py``` then the out will be an android
studio project that you will bulid and generate a release signed apk ready for install on you
phone trought adb, and you will can see the problem of Crashlytics symbols

You also have ```./clean.py``` to delete all stuff without delete .local folder


