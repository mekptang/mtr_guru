kill $(ps aux | grep '[p]ython data_extractor.py' | awk '{print $2}')
