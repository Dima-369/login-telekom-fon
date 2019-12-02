# login-telekom-fon

Login into Telekom_FON hotspots by Python and Selenium

Change the `email` and `pw` variables to your credentials!

# Call from Hammerspoon

```lua
hs.hotkey.bind(hyper, "c", function()
  hs.execute('python3 ~/login-telekom-fon/main.py', true)
end)
```
