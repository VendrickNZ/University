ARGS = -V geometry:margin=3cm -V colorlinks=true -V linkcolor=blue

SPECS = $(wildcard *.md)

all: $(SPECS:.md=.pdf)

%.pdf: %.md
	pandoc $(ARGS) -o $@ $<

.PHONY: clean
clean:
	rm *.pdf
