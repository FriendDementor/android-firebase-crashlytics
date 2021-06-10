# Simple templated android ndk repository
This was made to help to implement the Firebase Crashlytics SDK
on a big project where the symbols don't appear on release builds

## Requirements
To build this project do you need python3 on your system
Also, do you need jinja2 installed with pip3

Once you have that, you need to create a .local folder with two files

### config.json

This file is for sign the apk on release builds. You can create this
with Android Studio on ```Build > Generate Signed Bundle / APK... ```
tool.

```JSON
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
This file should be generated on the Firebase console and can be downloaded from there


## Make the project
With the files on the .local folder you can run ```./generate.py``` then the out will be an android
studio project that you will build and generate a release signed apk ready for install on you
phone through adb, and you will see the problem of Crashlytics symbols

You also have ```./clean.py``` to delete all stuff without delete the .local folder
