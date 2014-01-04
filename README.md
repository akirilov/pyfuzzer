pyfuzzer
========

A simple python fuzzer inspired by Charlie Miller's talk

TODO:
-----
- ~~Add ability to launch application with a given file~~
- ~~Save fuzzed files, deletion if no crash~~
- Place above in loop and detect crash
- Add ability to use more than 1 template file (randomly select template)
- Add ability to attach debugger on crash (WinDbg?)
- Automate debugger with scipts to log useful info + minidump
- Automate explotability analysis
- Automatically attempt repro to eliminate one-off crashes
