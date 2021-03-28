pdfcrop hist.pdf
pdftoppm -png hist-crop.pdf hist
mv hist-1.png hist.png

pdfcrop hist_means.pdf
pdftoppm -png hist_means-crop.pdf hist_means
mv hist_means-1.png hist_means.png
