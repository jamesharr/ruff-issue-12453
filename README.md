See bug details in `tests/test_mod1.py`

```sh
# In terminal 1
find . -name .ruff_cache -exec rm -vfr {} +  # Clear out .ruff_cache, as a precaution

watchexec -w . -- ruff check --no-cache  # Watch in a loop, tests will initially fail
ruff check --no-cache                    # Alternately, run this every time you make a change
ruff check --no-cache --watch            # Note: This will NOT identify the creation/removal of 'mod1' directory

# In terminal 2:
mkdir mod1  # Test will pass after directory creation

$EDITOR tests/test_mod1.py
# Try messing with ordering / blank lines, etc as noted in tests/test_mod1.py, which clears up the issue
# Try 'rmdir mod1', which clears up the issue
```
