import src.mycodebuddyproject.get_debug_tips as debug
import src.mycodebuddyproject.get_help as get_help
import src.mycodebuddyproject.fun_facts as fun_facts
from src.mycodebuddyproject.study_timer import StudyTimer

# example uses
print(debug.debug_tip("runtime"))      # Get a debugging tip for runtime errors
print(get_help.language_help("python"))   # Get a documentation link for Python
print(fun_facts.get("features"))           # Get a fun fact about Python features

timer = StudyTimer()  # Create an instance of StudyTimer
timer.start(25)       # Start a 25-minute study session
timer.pause()         # Pause the session
timer.resume()        # Resume the session
timer.cancel()        # Cancel the session