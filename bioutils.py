# 解析fasta文件，将其置入字典，同时为了能够按顺序读取，将序列ID置入列表
def multi_genes_dict(fasta_a):

    seq_line = ""
    seq_name = ""
    seq_dict = {}
    name_list = []

    for item1 in open(fasta_a):
        item2 = item1.strip()
        if item2[0] == ">" and seq_line == "":
            seq_name = item2.split('>')[1]
            name_list.append(seq_name)
        elif item2[0] == ">" and seq_line != "":
            seq_dict[seq_name] = seq_line
            seq_line = ""
            seq_name = item2.split('>')[1]
            name_list.append(seq_name)
        elif item2[0] != ">":
            seq_line = seq_line + item2
        else:
            print("Error: unexpected condition")
    seq_dict[seq_name] = seq_line

    return seq_dict, name_list

# 读取多列文件(以Tab分隔)至字典，令其中一列为键；所有的键置入列表；每一行的其他列置入列表，该列表作为字典的值
def columns_load_dict(file_a, col):

    col_dict = {}
    key_list = []

    for item1 in open(file_a):

        groupList = []

        item1 = item1.strip()
        if item1.startswith("#"):
            next
        else:
            item2 = item1.split("\t")
            for K in range(len(item2)):
                col_key = item2[int(col)]

                if K != int(col):
                    groupList.append(item2[K])

            col_dict[col_key] = groupList
            key_list.append(col_key)

    return col_dict, key_list

# 读取gff文件,gff指gff文件，feature代表mRNA或exon或CDS
def feature_load_dict(gff,feature):
    feature_dict = {}

    for item1 in open(gff):
        item1 = item1.strip()
        if item1.startswith("#"):
            next
        else:
            item2 = item1.split("\t")
            loci = []
            if item2[2] == feature:
                loci.append(item2[0])
                loci.append(item2[3])
                loci.append(item2[4])

                geneName = item2[8].split("Name=")[1].split(";")[0]
                feature_dict[geneName] = loci
    return feature_dict
