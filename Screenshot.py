import pyscreenshot

# Take a screenshot
screenshot = pyscreenshot.grab()

# Display the screenshot
screenshot.show()

# Save the screenshot
screenshot.save("screenshot.png")