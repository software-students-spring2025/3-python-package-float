import time
import pytest
from src.mycodebuddyproject.study_timer import StudyTimer

@pytest.fixture
def timer():
    """fixture to create a new StudyTimer instance before each test"""
    return StudyTimer()

def test_start_timer(timer):
    """test if study session starts correctly"""
    timer.start()
    assert timer.running is True, "Expected timer.running to be True after start()"
    assert timer.elapsed_time == 0, "Expected elapsed_time to be 0 when starting"

def test_stop_timer_without_start(timer):
    """test stopping timer when it hasn't started"""
    timer.stop()
    assert timer.running is False, "Expected timer.running to remain False when stopping before start"  # timer should remain stopped

def test_stop_timer_after_start(timer, monkeypatch):
    """test stopping the study session and ensure elapsed time is tracked"""
    timer.start()
    time.sleep(2.1)  # simulate study time
    monkeypatch.setattr('builtins.input', lambda _: "no")  # no for break
    timer.stop()
    assert timer.running is False, "Expected timer.running to be False after stop()"
    assert timer.elapsed_time >= 2, "Expected elapsed_time to be at least 2 seconds"  # ensure time has passed

def test_resume_timer(timer):
    """test resuming the study session"""
    timer.resume()
    assert timer.running is True, "Expected timer.running to be True after resume()"

def test_multiple_start_calls(timer):
    """ensure calling start multiple times does not reset the timer"""
    timer.start()
    initial_time = timer.elapsed_time
    time.sleep(1)
    timer.start()  # should not restart/reset time
    assert timer.elapsed_time >= initial_time, "Expected elapsed_time to continue tracking"

def test_stop_then_resume(timer, monkeypatch):
    """test stopping and then resuming the timer"""
    timer.start()
    time.sleep(1)
    monkeypatch.setattr('builtins.input', lambda _: "no")  # no to break
    timer.stop()
    assert timer.running is False, "Expected timer.running to be False after stop()"

    timer.resume()
    assert timer.running is True, "Expected timer.running to be True after resume()"
