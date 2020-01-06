from pathlib import Path
import context
pngfiles=context.root_dir.glob("**/*png")
with open("pngfilelist.txt",'w') as outfile:
    for thefile in pngfiles:
        outfile.write(f"{str(thefile)}\n")
        
