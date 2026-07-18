import os
import subprocess
import zipfile

def run(cmd):
    print("Running:", cmd)
    subprocess.run(cmd, shell=True, check=True)

# Ensure fresh compilation
run("make distclean")
run("make all")

# Package Overleaf release (minimal)
overleaf_zip = "../releases/warwickbib-overleaf.zip"
if os.path.exists(overleaf_zip):
    os.remove(overleaf_zip)

with zipfile.ZipFile(overleaf_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write("harvard-ctr.bbx")
    zipf.write("harvard-ctr.cbx")
    zipf.write("english-ctr.lbx")
    zipf.write("harvard-warwick.bbx")
    zipf.write("harvard-warwick.cbx")
    zipf.write("english-warwick.lbx")
    zipf.write("../README.md", "README.md")
print(f"Created {overleaf_zip}")

# Package CTAN release (full source + docs)
ctan_zip = "../releases/warwickbib-ctan.zip"
if os.path.exists(ctan_zip):
    os.remove(ctan_zip)

with zipfile.ZipFile(ctan_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Source
    zipf.write("harvard-ctr.dtx")
    zipf.write("harvard-warwick.dtx")
    zipf.write("Makefile")
    # Docs
    zipf.write("../README.md", "README.md")
    zipf.write("harvard-ctr.pdf")
    zipf.write("harvard-warwick.pdf")
    # Generated Engine
    zipf.write("harvard-ctr.bbx")
    zipf.write("harvard-ctr.cbx")
    zipf.write("english-ctr.lbx")
    zipf.write("harvard-warwick.bbx")
    zipf.write("harvard-warwick.cbx")
    zipf.write("english-warwick.lbx")
print(f"Created {ctan_zip}")

print("All releases packaged successfully!")
