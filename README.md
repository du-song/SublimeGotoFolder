## Summary

SublimeGotoFolder plugin lists folders similar to the handy Goto Anything, and opens selected folder in a separate window by your command.

## How to Use

Customize with GotoFolder.sublime-settings, otherwise this plugin will start with default settings of scaning all Sublime Text 2 plugins.

Press _Ctrl + P_ or click menu _Goto_ -> _Goto Folder_

## Example Configuration
create GotoFolder.sublime-settings with content like this:

```
{
    "root_folders": [{
    	"folder": "/Users/freewizard/Projects/as3", //required
    	"extra": ["/Users/freewizard/Projects/as3/common"], //optional
    	"alias": "AS3" //optional
    },{
    	"folder": "/Users/freewizard/Projects/cocoa",
    	"extra": ["/Users/freewizard/Projects/cocoa/common"],
    	"alias": "iOS"
    },{
    	"folder": "/Users/freewizard/Projects/android",
    	"extra": ["/Users/freewizard/Projects/android/common"],
    	"alias": "Android"
    },
    "cache": true //set cache to true to save scan time
}
```

all sub-folders in as3/cocoa/android will be listed in Goto Folder; when pressing enter, the common folder will be opened together with the selected folder

## License

[MIT LICENSE](https://github.com/holtwick/xobjc/blob/master/LICENSE-MIT.txt)
