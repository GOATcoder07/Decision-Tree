import treelib
tree = treelib.Tree()

tree.create_node("John", "john")  
tree.create_node("Mayoo",  "mayoo"   , parent="john")
tree.create_node("Ed",  "ed"   , parent="john")
tree.create_node("Kode", "kode"  , parent="mayoo")
tree.create_node("Mary",  "mary"   , parent="kode")
tree.create_node("Mark",  "mark"   , parent="mayoo")

tree.show()