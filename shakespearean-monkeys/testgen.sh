#!/user/bin/bash
#On windows, you can use the linux subsystem, then run testgen.sh

#first use dos2unix testgen.sh to get rid of windows characters

#remove existing input and output
[[ -e cases/ ]] && rm -r cases/  
mkdir -p cases
mkdir -p cases/input
mkdir -p cases/output

#copy over samples
[[ -e samples/input ]] && cp -r samples/input ./cases/
[[ -e samples/output ]] && cp -r samples/output ./cases/

for i in {1..50}
do
  echo $i | python3 ./mkin.py > cases/input/input$i.txt
  python3 ./solutions/sol.py < cases/input/input$i.txt > cases/output/output$i.txt

  echo $i
done

rm -rf cases/cases.zip