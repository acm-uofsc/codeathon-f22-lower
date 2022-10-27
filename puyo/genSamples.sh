#generates sample input and output

for i in {0..1}
do
  echo $i | python3.9 ./mkin.py > samples/input/input$i.txt
  java --class-path solutions/Java/ Puyo < samples/input/input$i.txt > samples/output/output$i.txt
done
