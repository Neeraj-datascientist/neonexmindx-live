import subprocess
import shutil
import os

print("Mirroring deployment_NeoNex to finalised_deployment...")
# Use robocopy on windows
cmd = ["robocopy", "deployment_NeoNex", "finalised_deployment", "/MIR", "/XD", ".git"]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Robocopy exit code:", res.returncode)
# In robocopy codes 0-7 indicate success/copy
if res.returncode <= 7:
    print("Mirror successful!")
else:
    print("Robocopy failed:", res.stderr)
