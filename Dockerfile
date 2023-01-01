FROM ksyk/texlive:base

# installing dependencies
RUN tlmgr install cyrillic babel-russian mathtools pgfplots caption \
	ulem enumitem standalone parskip tikzmark svn-prov preprint cmcyr lh mathabx

# getting source code
RUN mkdir /root/src
WORKDIR /root/src

COPY defines.sty .
COPY scripts ./scripts
COPY src ./src

RUN python ./scripts/gen-makefile.py "zathura %S"

CMD ["make", "all-parallel"]
