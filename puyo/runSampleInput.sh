#only runs sample files, does not generate them
for i in {0..1}
do
  echo $i
  node solutions/sol.js < samples/input/input$i.txt > samples/output/output$i.txt
done
