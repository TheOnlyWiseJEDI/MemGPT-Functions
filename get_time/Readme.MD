This MemGPT function checks for the current time from time.nist.gov and returns it to the AI.

It is currently set for Eastern Standard Time (EST) but this can be changed.
  On line 30 you will find 'est_time = ntp_time - timedelta(hours=5)'

This is the adjustment to compensate for UTC time. EST is 5 hours difference. CST is 6 hours etc.

