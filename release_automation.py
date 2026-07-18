import os
import subprocess
import zipfile

def run(cmd):
    print("Running:", cmd)
    subprocess.run(cmd, shell=True, check=True)

# Ensure fresh compilation
run("make distclean")
run("make all")

# Package standard CTR release
ctr_zip = "harvard-ctr-release.zip"
if os.path.exists(ctr_zip):
    os.remove(ctr_zip)

with zipfile.ZipFile(ctr_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write("harvard-ctr.bbx")
    zipf.write("harvard-ctr.cbx")
    zipf.write("english-ctr.lbx")
    zipf.write("harvard-ctr.pdf")
    zipf.write("README.md")
print(f"Created {ctr_zip}")

# Package Warwick release
warwick_zip = "harvard-warwick-release.zip"
if os.path.exists(warwick_zip):
    os.remove(warwick_zip)

with zipfile.ZipFile(warwick_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write("harvard-warwick.bbx")
    zipf.write("harvard-warwick.cbx")
    zipf.write("english-warwick.lbx")
    zipf.write("harvard-warwick.pdf")
    zipf.write("README.md")
print(f"Created {warwick_zip}")

print("All releases packaged successfully!")
