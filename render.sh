FILENAME=$1
dot -Tsvg -o ./static/images/dot_$FILENAME.svg static/$FILENAME
neato -Tsvg -o ./static/images/neato_$FILENAME.svg static/$FILENAME
twopi -Tsvg -o ./static/images/twopi_$FILENAME.svg static/$FILENAME
circo -Tsvg -o ./static/images/circo_$FILENAME.svg static/$FILENAME
fdp -Tsvg -o ./static/images/fdp_$FILENAME.svg static/$FILENAME
sfdp -Tsvg -o ./static/images/sfdp_$FILENAME.svg static/$FILENAME
