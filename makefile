all: catalog.txt

catalog.pdf:
	curl http://anderson.edu/uploads/catalog/2020-21-undergrad-catalog.pdf > $@

catalog.txt: catalog.pdf
	pdftotext -layout -nopgbrk catalog.pdf

clean:
	rm -f catalog.pdf catalog.txt
