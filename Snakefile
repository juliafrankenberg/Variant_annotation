# Snakefile

rule all:
    input:
        "results/annotated_variants.vcf"

rule annotate_variants:
    input:
        vcf="data/NIST.vcf.gz"
    output:
        "results/annotated_variants.vcf"
    shell:
        """
        snpeff -Xmx4g GRCh38.86 {input.vcf} \
        > {output}
        """
