all: catalog.md

catalog.pdf:
	curl http://anderson.edu/uploads/catalog/2020-21-undergrad-catalog.pdf > $@

catalog.txt: catalog.pdf
	pdftotext -layout -nopgbrk catalog.pdf

catalog.md: catalog.txt reformat.py
	python3 reformat.py > $@
	npx prettier --write --prose-wrap never $@

clean:
	rm -f catalog.pdf catalog.txt
