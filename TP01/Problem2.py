total_seconds = 9875
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print("9875 seconds =",hours,"h", minutes, "m",seconds,"s")
print("Check:",hours*3600 + minutes*60 + seconds == total_seconds)

