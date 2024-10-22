# VCF annotation

This is a pipeline for basic annotation of VCF files, using snakemake, and that can be run with an API. 

 * The snakefile contains the pipeline for annotating the variants, so far using Snpeff tool. The output is a new VCF file with information on gene names and dbSNP IDs.

TO-DO: add information about frequency in a database (e.g gnOMAD using bcftools) - haven't managed to download database

 * The app.py is the API that can execute this snakemake, as well as display the results in a html format (as per html templates), including filtration of variants by DP. To run: 

    python app.py

then open: http://127.0.0.1:5000 and follow instructions.

Can also check jsonify objects to check API is running properly. e.g. open http://127.0.0.1:5000/get_vcf?format=json



## Dependency manager

I used conda, all packages listed in environment.yml; 

TO-DO: get docker image to work...
I've created a docker image "variant_ann", but haven't managed to get it to work...had some issue with ports, and cannot find snpeff command now, despite it apparently being there?



## Repository structure

```

├── README.md          <- The top-level README for developers using this project.
|
├── data <- input VCF files should be saved here.
|
├── results         <- annotated VCF file (output of pipeline) will be saved here 
│ 
├── templates <- html templates are saved here                     
│
├── app.py <- API script
│ 
│
├── Snakefile <- snakefile for execution of pipeline
│ 
│
├── environment.yml <- with information of packages installed via conda
│ 
├── Dockerfile   <- for building a docker image of the project (.dockerignore also there)

```