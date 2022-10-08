#!/user/bin/bash
#On windows, you can use the linux subsystem, then run testgen.sh

#first use dos2unix testgen.sh to get rid of windows characters

#remove existing input and output
[[ -e input/ ]] && rm -r input/ 
[[ -e output/ ]] && rm -r output/ 
mkdir -p input
mkdir -p output

python3 ./gen_samples.py 51

#copy over samples
[[ -e samples/input ]] && cp -r samples/input ./

for i in {0..50}
do
  python3 ./solutions/sol.py < input/input$i.txt > output/output$i.txt

  echo $i
done