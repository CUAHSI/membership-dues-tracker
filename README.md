# membership-dues-tracker
Workflows for tracking payments of CUAHSI membership dues over time.

## R Targets Pipeline

The main recipe file is `_targets.R`. This is what connects all of the individual
steps or "targets" and establishes any special settings. Make sure you have the 
packages listed in `_targets.R` as well as `targets` and `qs` installed.

Run `targets::tar_make()` to build the entire pipeline.
