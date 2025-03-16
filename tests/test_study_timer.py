import time
import pytest
from study_timer import StudyTimer

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
    time.sleep(2)  # simulate study time
    monkeypatch.setattr('builtins.input', lambda _: "no")  # no for break
    timer.stop()
    assert timer.running is False, "Expected timer.running to be False after stop()"
    assert timer.elapsed_time >= 2, "Expected elapsed_time to be at least 2 seconds"  # ensure time has passed

def test_start_break(timer, monkeypatch):
    """test starting a break and verify it sets the break flag"""
    monkeypatch.setattr('builtins.input', lambda _: "2")  # simulate 2-minute break input
    timer.start_break()
    assert timer.on_break is False, "Expected timer.on_break to be False after break ends"

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

def test_invalid_break_input(timer, monkeypatch):
    """test handling of invalid break input"""
    monkeypatch.setattr('builtins.input', lambda _: "invalid")
    timer.start_break() 
    assert timer.on_break is False, "Expected timer.on_break to remain False after invalid input" 

def test_stop_then_resume(timer, monkeypatch):
    """test stopping and then resuming the timer"""
    timer.start()
    time.sleep(1)
    monkeypatch.setattr('builtins.input', lambda _: "no")  # no to break
    timer.stop()
    assert timer.running is False, "Expected timer.running to be False after stop()"

    timer.resume()
    assert timer.running is True, "Expected timer.running to be True after resume()"

def test_timer_does_not_run_during_break(timer, monkeypatch):
    """ensure timer doesn't count study time while on break"""
    timer.start()
    time.sleep(1)
    monkeypatch.setattr('builtins.input', lambda _: "1")  # simulate 1-minute break
    timer.start_break()
    study_time = timer.elapsed_time
    time.sleep(1)
    assert timer.elapsed_time == study_time, "Expected elapsed_time to remain the same during break"

