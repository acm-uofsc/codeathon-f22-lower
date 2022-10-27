#!/user/bin/bash
#generates sample input and output

for i in 0
do
  echo $i | python3 ./mkin.py > samples/input/input$i.txt
  python3 solutions/sol.py < samples/input/input$i.txt > samples/output/output$i.txt
done