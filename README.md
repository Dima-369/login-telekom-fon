# login-telekom-fon
Login into Telekom_FON hotspots by Python and Selenium

# Call from Hammerspoon

hs.hotkey.bind(hyper, "c", function()
  hs.execute('python3 ~/login-telekom-fon/main.py', true)
end)
