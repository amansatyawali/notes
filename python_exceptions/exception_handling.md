## The difference between using finally block and writing normal statements.

It makes a difference if you return early:

try:
    run_code1()
except TypeError:
    run_code2()
    return None   # The finally block is run before the method returns
finally:
    other_code()
Compare to this:

try:
    run_code1()
except TypeError:
    run_code2()
    return None

other_code()  # This doesn't get run if there's an exception.

# Other situations that can cause differences:

    If an exception is thrown inside the except block.
    If an exception is thrown in run_code1() but it's not a TypeError.
    Other control flow statements such as continue and break statements.