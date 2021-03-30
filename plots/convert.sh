
dot ./tree.dot -Tpdf -o tree.pdf

for file in tree hist hist_means hist_less_rounds hist_means_less_rounds
do
  echo "File: $file"
  pdfcrop $file.pdf
  pdftoppm -png $file-crop.pdf $file
  mv $file-1.png $file.png
  rm $file-crop.pdf
done
