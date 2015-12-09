# BlockCursorEverywhere

A block cursor for Sublime Text 2 and 3.

![Screenshot](http://f.cl.ly/items/42131K2X1h0j0P2m1O2B/Screen%20Shot%202011-12-02%20at%202.36.54%20AM.png)

The default cursor in Sublime Text is a thin line with low visibility. Command mode in the Vintage and Vintageous plugins decreases the visibility even further. This plugin displays the cursor as a rectangular block, increasing its prominence on the screen.

## Installation

### With Package Control

The easiest way to install Block Cursor Everywhere is via [Package Control](http://wbond.net/sublime_packages/package_control) for Sublime Text.

Once you install Package Control, restart Sublime Text and bring up the Command Palette with <kbd>Command</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on OS X or <kbd>Control</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on Linux/Windows.

Select `Package Control: Install Package`, wait while Package Control fetches the latest package list, then select `Block Cursor Everywhere` when the list appears. Package Control will automatically keep the package up-to-date.

### Without Package Control

Go to your Sublime Text Packages directory:

	Windows: %USERPROFILE%\AppData\Roaming\Sublime Text 3\Packages\
	Mac: ~/Library/Application Support/Sublime Text 3/Packages/

and clone the repository there.

## Configuration

Change the style of the block cursor by adding a section to your color scheme file like the following.

```xml
<dict>
	<key>name</key>
	<string>Block Cursor</string>
	<key>scope</key>
	<string>block_cursor</string>
	<key>settings</key>
	<dict>
		<key>foreground</key>
		<string>#000000</string>
		<key>background</key>
		<string>#FF1111</string>
	</dict>
</dict>
```

The path to your color scheme file can be specified with the `color_scheme` key in your user preferences:

```json
{
	"color_scheme": "Packages/User/Monokai (Block Cursor Everywhere).tmTheme"
}
```

If you don't have a color scheme file yet, you can create one in your `Packages/User` directory from [this gist](https://gist.github.com/karlhorky/804b6d1fc12f2b9f504e).
