# Time Converter

**Date:** December 2024

## What I Learned
- Floor division (`//`) for getting whole numbers
- Modulo operator (`%`) for getting remainders
- Input validation using `while` loops
- Zero-padded number formatting (`:02d`)

## Concepts Covered
- Floor division vs regular division
- Modulo operations
- While loops for validation
- Formatted output with padding

## The Math Behind It
```
1 hour = 3600 seconds
1 minute = 60 seconds

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60
```

## How to Run
```bash
python time_converter.py
```

## Example Usage
```
=== Time Converter ===
Convert seconds to hours, minutes, and seconds

Please enter the time in seconds: 3725

----------------------------------------
Input: 3725 seconds
----------------------------------------
Hours:   1
Minutes: 2
Seconds: 5
----------------------------------------
Formatted: 01:02:05
----------------------------------------
```
