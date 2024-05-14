#! /bin/bash

# clean up
rm -f host1/map_results/*.txt
rm -f host2/map_results/*.txt
rm -f map_results/*.txt
rm -f reduce_results/results.txt

# Run the map workers in parallel, each of one, maps letters to coincidences for text lines
HOST=host1 python3 map.py & HOST=host2 python3 map.py &

# wait for them to be done
wait

# Take outputs from mappers and aggregate results for key in a single folder
HOSTS=host1,host2 python3 shuffle.py

# Take aggregated outputs and it summarizes info to be consumed
python3 reduce.py

# display result
cat reduce_results/results.txt


python3 plot.py