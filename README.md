# login-telekom-fon

Login into Telekom_FON hotspots by Python and Selenium

Change the `email` and `pw` variables to your credentials!

### Call from Hammerspoon

```lua
hs.hotkey.bind(hyper, "c", function()
  hs.execute('python3 ~/login-telekom-fon/main.py', true)
end)
```
### Another option which I found more reliable after some time

On macOS, a hotspot login window pops up on which you manually have to click the `Login` tab and use the script below.

The script does not work in Firefox; 
it writes everything in the Email input field without switching to the password field because `\t` does not work in Firefox to switch input fields.

```lua
hs.hotkey.bind(hyper, "g", function()
  pw = 'TODO'
  hs.eventtap.keyStrokes('mail@gmail.com')
  hs.eventtap.keyStrokes('\t')
  hs.eventtap.keyStrokes(pw)
  hs.eventtap.keyStroke({}, 'return')
  hs.alert.show('Wrote Telekom password')
end)
```
