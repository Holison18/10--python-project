import time
import notify2
from topnews import topStories

# path to notification window icon
ICON_PATH = "coat-of-arms-of-ghana-logo.png"

# fetch news items
newsitems = topStories()

# Initialize the d-bus connection
notify2.init("News Notification App")

