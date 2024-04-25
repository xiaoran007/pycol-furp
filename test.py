from complexity.Complexity import Complexity

# test: dataset from paper
complexity = Complexity("./Datasets/dataset/dataset from paper/61_iris.arff", distance_func="default", file_type="arff")


print(complexity.T1())

print(complexity.R_value())
print(complexity.D3_value())
print(complexity.CM())
print(complexity.kDN())
print(complexity.MRCA())
print(complexity.DBC())
print(complexity.SI())
print(complexity.input_noise())
print(complexity.borderline())
print(complexity.deg_overlap())

print(complexity.ICSV())
print(complexity.NSG())

print(complexity.C1())
print(complexity.C2())
print(complexity.Clust())
print(complexity.purity())
print(complexity.neighbourhood_separability())
print(complexity.N1())
print(complexity.N2())
print(complexity.N3())
print(complexity.N4())
print(complexity.LSC())


#print(complexity.T1())



print(complexity.F1())
print(complexity.F1v())
print(complexity.F2())
print(complexity.F3())
print(complexity.F4())