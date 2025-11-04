PLANTUML = java -jar ../plantuml-gplv2-1.2025.9.jar

IMAGES = legacy_capture dsl_model
PNG_IMAGES = $(addsuffix .png, ${IMAGES})
TIKZ_IMAGES = $(addsuffix .tikz, ${IMAGES})

presentation.pdf : presentation.tex ${TIKZ_IMAGES} ${PNG_IMAGES}
	pdflatex -shell-escape presentation.tex
	pdflatex -shell-escape presentation.tex

%.tex : %.puml
	${PLANTUML} -progress -tlatex:nopreamble $<

%.tikz : %.puml
	${PLANTUML} -progress -tlatex:nopreamble $<
	mv $(basename $<).tex $@

%.png : %.puml
	${PLANTUML} -progress -tpng $<
