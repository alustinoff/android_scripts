# android_scripts

exp_act.py - shows exported activity from AndroidManifest.xml  
deeplink.py - shows deeplinks from AndroidManifest.xml

## Usage

Oneliners:
```
androguard axml com.reddit.frontpage_2022.44.0-664348.apk | sed -r "s:\x1B\[[0-9;]*[mK]::g" | python3 exp_act.py

androguard axml com.reddit.frontpage_2022.44.0-664348.apk | sed -r "s:\x1B\[[0-9;]*[mK]::g" | python3 deeplinks.py
```

Using AnrdoidManifest.xml file:
```
python3 exp_act.py --file manifest.xml


python3 deeplinks.py --file manifest.xml
```

## Examples

```
# Show exported activity

$ androguard axml com.reddit.frontpage_2022.44.0-664348.apk | sed -r "s:\x1B\[[0-9;]*[mK]::g" | python3 exp_act.py
Activity:  com.zoho.notebook.activities.NoteBookActivity
Is exported:  true
Intent action:  android.intent.action.MAIN
___________________________________________________________________________ 

Activity:  com.zoho.notebook.activities.ExplicitShareActivity
Is exported:  true
Intent action:  android.intent.action.PROCESS_TEXT
Intent action:  android.intent.action.SEND
Intent action:  android.intent.action.SEND_MULTIPLE
Intent action:  android.intent.action.SEND
Intent action:  com.google.android.gms.actions.CREATE_NOTE
___________________________________________________________________________ 

Activity:  com.zoho.notebook.activities.HandleRedirectActivity
Is exported:  true
Intent action:  android.intent.action.VIEW
___________________________________________________________________________ 

Activity:  androidx.core.google.shortcuts.TrampolineActivity
Is exported:  true
Intent action:  androidx.core.content.pm.SHORTCUT_LISTENER
___________________________________________________________________________ 


```



```
# Show deeplinks

$ androguard axml com.reddit.frontpage_2022.44.0-664348.apk | sed -r "s:\x1B\[[0-9;]*[mK]::g" | python3 deeplinks.py
Activity:  com.zoho.notebook.activities.WidgetLaunchActivityNotes
Deeplink: zohonotebook://notes
_________________ 

Deeplink: zohonotebook://view
_________________ 

Deeplink: https://notebook.zoho.com
Deeplink: https://one.zoho.com
_________________ 

Deeplink: https://notebook.zoho.eu
Deeplink: https://one.zoho.eu
_________________ 

Deeplink: https://notebook.zoho.com.cn
Deeplink: https://one.zoho.com.cn
_________________ 

...
```
