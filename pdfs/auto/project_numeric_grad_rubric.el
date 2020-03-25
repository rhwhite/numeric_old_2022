(TeX-add-style-hook
 "project_numeric_grad_rubric"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("geometry" "landscape")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "geometry"))
 :latex)

