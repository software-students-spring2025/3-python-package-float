import src.mycodebuddyproject.get_debug_tips as debug
import src.mycodebuddyproject.get_help as get_help
import src.mycodebuddyproject.fun_facts as fun_facts
from src.mycodebuddyproject.study_timer import StudyTimer

# example uses
print("Get a debugging tip for runtime errors")
print(debug.debug_tip("runtime"))

print("# Get a documentation link for Python")
print(get_help.language_help("python"))

print("Get a fun fact about Python features")
print(fun_facts.get("features"))

print("Start a study timer for 2 minutes")
timer = StudyTimer()  # Create an instance of StudyTimer
timer.start(2)       # Start a 2-minute study session
timer.pause()         # Pause the session
timer.resume()        # Resume the session
timer.cancel()        # Cancel the session
