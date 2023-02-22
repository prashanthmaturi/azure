Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@prashanthmaturi 
KarthikeyaVaitla16
/
lab4
Public
Fork your own copy of KarthikeyaVaitla16/lab4
Code
Issues
Pull requests
Actions
Projects
Security
Insights
lab4/helloworld.py /
@KarthikeyaVaitla16
KarthikeyaVaitla16 Update helloworld.py
Latest commit 6e08e6e on Jan 7
 History
 1 contributor
34 lines (29 sloc)  680 Bytes

# This program prints Hello, world!

print('Hello, world!')
trigger:
- main

pool:
  vmImage: ubuntu-latest
strategy:
  matrix:
    Python27:
      python.version: '2.7'
    Python35:
      python.version: '3.5'
    Python36:
      python.version: '3.6'
    Python37:
      python.version: '3.7'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '$(python.version)'
  displayName: 'Use Python $(python.version)'

- script: | python "helloworld.py"
    python -m pip install --upgrade pip
    pip install -r requirements.txt
  displayName: 'Install dependencies'

- script: |helloworld.py
    pip install pytest pytest-azurepipelines
    pytest
  displayName: 'pytest'
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
lab4/helloworld.py at main · KarthikeyaVaitla16/lab4
