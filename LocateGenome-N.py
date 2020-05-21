from bioutils import multi_genes_dict
import sys

multi_genes_dict,name_list = multi_genes_dict(sys.argv[1])

for item in name_list:
    chr_seq = multi_genes_dict[item]

    index = -1
    start = -1
    end = -1
    for base in chr_seq:
        index = index + 1
        if base.upper() == "N" and start == -1:
            start = index
            end = index + 1

        elif base.upper() == "N" and start != -1:
            end = index + 1

        elif base.upper() != "N" and start != -1 and end != -1:
            print(item,str(start),str(end),sep="\t")
            start = -1
            end = -1
