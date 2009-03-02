/*** Base page elements ***/

/* Display */
body { background: #ddd; }
#header, #menu, #content, #footer { padding: 1em; }
#header { background: #2457a0; color: white; }
#menu { border-right: 1px solid #2457a0; background: #c6d8f2; }
#content { background: white; }
#footer { border-top: 1px solid #2457a0; background: #ddd; }

/* Layout: any-order columns */
#header {}
#content-wrapper { float: left; width: 100%; }
#content { margin-left: 15em; }
#menu { float: left; width: 13em; margin-left: -100%; }

/* Layout: equal-height columns */
#body { overflow: hidden; }
#menu, #content { padding-bottom: 1004em; margin-bottom: -1000em; }

/* Basics */
h1 { font-size: 2em; margin: 0.5em 0 0.25em 0 /* 1em 0 0.5em 0 */; padding-bottom: 0.125em /* 0.25em */; border-bottom: 1px solid #2457a0; color: #2457a0; }
h2 { font-size: 1.67em; margin: 0.6em 0 0.3em 0 /* 1em 0 0.5em 0 */; color: #2457a0; }

img { vertical-align: middle; }

/* Definition lists via floats */
dl { overflow: hidden /* new float context */; }
dt { float: left; clear: left; width: 10em; }
dd:after { content: 'float clear'; display: block; clear: both; height: 0; visibility: hidden; }
dt, dd { line-height: 1.33; }
dt:hover + dd, dd:hover { background: #e8e8e8; }
