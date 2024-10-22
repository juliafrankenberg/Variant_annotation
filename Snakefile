# Snakefile

rule all:
    input:
        "results/annotated_variants.vcf"

rule annotate_variants:
    input:
        vcf="data/NIST.vcf.gz" #change this to the appropriate file name
    output:
        "results/annotated_variants.vcf"
    shell:
        """
        snpeff -Xmx4g GRCh38.86 {input.vcf} \
        > {output}
        """
#TO-DO: change output location of extra files generated (snpEff_genes.txt and snEff_summary.html)
#TO-DO: add annotation of frequency in database (e.g. gnOMAD usng bcftools)