## Summary

SublimeGotoFolder plugin lists folders and projects similar to the handy Goto Anything, and opens selected folder in a separate window by your command.

## Install
Search and install **Goto Folder** via [Package Control](http://wbond.net/sublime_packages/package_control)

## How to Use

Customize with GotoFolder.sublime-settings, otherwise this plugin will start with default settings of scaning all Sublime Text 2 plugins.

Press `Ctrl + P` or click menu `Goto` -> `Goto Folder`

## Example Configuration
create `GotoFolder.sublime-settings` with content like this:

```
{
    "root_folders": [{
        //required, all sub-folders and *.sublime-projects inside will be indexed, except .*
        "folder": "/Users/freewizard/Projects/as3",

        //optional, will be opened together with one of sub-folders
        "extra": ["/Users/freewizard/Projects/as3/common"],

        //optional, will be used in display panel, e.g. AS3:SubFolderName
        "alias": "AS3" 
    },{
        "folder": "/Users/freewizard/Projects/cocoa",
        "alias": "iOS"
    },{
        "folder": "/Users/freewizard/Projects/android",
        "alias": "Android"
    }],

    //optional, set to true to save scan time, but requires ST re-launch when folder list change
    "cache": false 
}
```

all sub-folders and *.sublime-projects in as3/cocoa/android will be listed in Goto Folder; when pressing enter, the common folder will be opened together with the selected folder

## License

[MIT LICENSE](https://github.com/holtwick/xobjc/blob/master/LICENSE-MIT.txt)
