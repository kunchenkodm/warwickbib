import os
import shutil
import re
import subprocess

def run(cmd):
    print("Running:", cmd)
    subprocess.run(cmd, shell=True, check=True)

def process_standard_bbx(bbx_path, edition):
    with open(bbx_path, "r") as f:
        bbx = f.read()
    
    # URL and accessed replacements
    bbx = bbx.replace(r"\DeclareFieldFormat{url}{Available at: \url{#1}}", r"\DeclareFieldFormat{url}{\url{#1}}")
    bbx = bbx.replace(r"Available at\addcolon\space\url{https://doi.org/#1}", r"\url{https://doi.org/#1}")
    bbx = bbx.replace(r"urlseen = {Accessed: },", r"urlseen = {accessed },")
    
    # Update language mappings to use english-ctr instead of english-warwick
    bbx = bbx.replace("{english-warwick}", "{english-ctr}")
    
    if edition == 13:
        # Clear location for books in standard 13th edition
        bbx += "\n\\AtEveryBibitem{\\ifentrytype{book}{\\clearlist{location}}{}}\n"
            
    # Also process the lbx file if it exists
    lbx_path = bbx_path.replace("harvard-ctr.bbx", "english-ctr.lbx")
    if os.path.exists(lbx_path):
        with open(lbx_path, "r") as f:
            lbx = f.read()
        lbx = lbx.replace(r"Accessed\addcolon\space", r"accessed ")
        with open(lbx_path, "w") as f:
            f.write(lbx)

def process_standard_csl(csl_path, edition):
    with open(csl_path, "r") as f:
        csl = f.read()
    
    # URL and accessed replacements
    csl = csl.replace('value="Available at: "', 'value=""')
    csl = csl.replace('prefix=" (Accessed: "', 'prefix=" (accessed "')
    
    if edition == 13:
        # Remove publisher-place
        csl = re.sub(r'<group delimiter=":\s*">\s*<text variable="publisher-place"/>\s*<text variable="publisher"/>\s*</group>', '<text variable="publisher"/>', csl)
        
    with open(csl_path, "w") as f:
        f.write(csl)

def build_branch(base_branch, new_branch, edition, is_standard):
    run(f"git checkout {base_branch}")
    # Delete branch if exists locally
    subprocess.run(f"git branch -D {new_branch}", shell=True, stderr=subprocess.DEVNULL)
    run(f"git checkout -b {new_branch}")
    
    if is_standard:
        # Rename files to harvard-ctr instead of harvard-warwick
        if os.path.exists("harvard-warwick.bbx"):
            run("git mv harvard-warwick.bbx harvard-ctr.bbx")
        if os.path.exists("harvard-warwick.cbx"):
            run("git mv harvard-warwick.cbx harvard-ctr.cbx")
        if os.path.exists("english-warwick.lbx"):
            run("git mv english-warwick.lbx english-ctr.lbx")
        if os.path.exists("csl/harvard-warwick.csl"):
            run("git mv csl/harvard-warwick.csl csl/harvard-ctr.csl")
        elif os.path.exists("csl/harvard-university-of-bath.csl"):
            run("git mv csl/harvard-university-of-bath.csl csl/harvard-ctr.csl")
        
        # Modify for standard format
        if os.path.exists("harvard-ctr.bbx"):
            process_standard_bbx("harvard-ctr.bbx", edition)
        if os.path.exists("csl/harvard-ctr.csl"):
            process_standard_csl("csl/harvard-ctr.csl", edition)
            
        run("git commit -am 'Configure for standard Cite Them Right format (non-Warwick)'")

def create_zip_for_branch(branch, edition, is_standard):
    run(f"git checkout {branch}")
    
    prefix = "harvard-ctr" if is_standard else "harvard-warwick"
    
    # Overleaf standalone zip (just bbx, cbx, lbx)
    overleaf_zip = f"overleaf-package-v{edition}-{'standard' if is_standard else 'warwick'}.zip"
    if os.path.exists(overleaf_zip): os.remove(overleaf_zip)
    run(f"zip -r {overleaf_zip} {prefix}.bbx {prefix}.cbx english-{'ctr' if is_standard else 'warwick'}.lbx")
    
    # Complete zip (bbx, cbx, lbx, csl)
    complete_zip = f"biblatex-csl-package-v{edition}-{'standard' if is_standard else 'warwick'}.zip"
    if os.path.exists(complete_zip): os.remove(complete_zip)
    run(f"zip -r {complete_zip} {prefix}.bbx {prefix}.cbx english-{'ctr' if is_standard else 'warwick'}.lbx csl/{prefix}.csl")
    
    return overleaf_zip, complete_zip

def publish_release(tag, title, notes, files):
    # Create tag
    # GH release create
    run(f"git tag -f {tag}")
    run(f"git push -f origin refs/tags/{tag}")
    
    # Delete existing release if it exists
    subprocess.run(f"gh release delete {tag} -y", shell=True, stderr=subprocess.DEVNULL)
    
    files_str = " ".join(files)
    run(f'gh release create {tag} -t "{title}" -n "{notes}" {files_str}')

# Setup 13th Edition Warwick
build_branch("ctr_13th_edition_updates", "v13-warwick", 13, False)
files_13w = create_zip_for_branch("v13-warwick", 13, False)
publish_release("v13.0.0-warwick", "Cite Them Right 13th Edition (Warwick Economics)", "Implementation of the 13th Edition with Warwick overrides.", files_13w)

# Setup 13th Edition Standard
build_branch("ctr_13th_edition_updates", "v13-standard", 13, True)
files_13s = create_zip_for_branch("v13-standard", 13, True)
publish_release("v13.0.0-standard", "Cite Them Right 13th Edition (Standard)", "Implementation of the standard 13th Edition format.", files_13s)

# Setup 12th Edition Warwick
build_branch("cite_them_right_12th", "v12-warwick", 12, False)
files_12w = create_zip_for_branch("v12-warwick", 12, False)
publish_release("v12.0.0-warwick", "Cite Them Right 12th Edition (Warwick Economics)", "Implementation of the 12th Edition with Warwick overrides.", files_12w)

# Setup 12th Edition Standard
build_branch("cite_them_right_12th", "v12-standard", 12, True)
files_12s = create_zip_for_branch("v12-standard", 12, True)
publish_release("v12.0.0-standard", "Cite Them Right 12th Edition (Standard)", "Implementation of the standard 12th Edition format.", files_12s)

# Cleanup
run("git checkout master")
print("All releases published successfully!")
