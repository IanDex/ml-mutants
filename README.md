# ml-mutants

run app localhost

    git clone https://github.com/IanDex/ml-mutants
	cd ml-mutants
	pipenv shell
	python app.py
	
## Http Requests

### /mutant/
**POST** → https://melii-app.herokuapp.com/mutant/
Body:

    { 
	    "dna": [ 
		    "ATGCGA", 
		    "CCGTGC", 
		    "TTATGT", 
		    "AGAAGG", 
		    "CACCTA", 
		    "TCACTG" 
		 ] 
	}

response → 200 is mutant, 403 not is mutant


### /stats/
**POST** → https://melii-app.herokuapp.com/stats/
No Body

response:

    { 
	    "count_human_dna": 102, 
	    "count_mutant_dna": 42, 
	    "ratio": 0.41 
	}

## Test
in progress.


