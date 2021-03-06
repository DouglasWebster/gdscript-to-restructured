# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

APISOURCE := reference.json
MODULEDIR := $(SOURCEDIR)/module_exports


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

nap-apis:
ifeq (,$(wildcard $(SOURCEDIR)/$(APISOURCE)))
	@echo "reference.json (the source file for the API docs) does not exist."
	@echo "Use the Godot plugin to generate the file then re-run this make."
else
	@echo "reference.json found - building rst files"
	python -m gdscript_docs_maker $(SOURCEDIR)/$(APISOURCE) -p $(SOURCEDIR)/module_exports/
	$(MAKE) rstapis
endif
	
rstapis:
	m2r --overwrite $(wildcard $(MODULEDIR)/*.md) 

clean:
	rm -rf $(SOURCEDIR)/module_exports
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)