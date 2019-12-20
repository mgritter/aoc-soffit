
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for depth in [3, 2, 1, 0]:
    src_node = "ROOT[root{}]".format( depth )
    right_side = []
    right_side.append( "ROOT[node]" )

    child_type = "node"
    if depth > 0:
        child_type = "root{}".format( depth - 1 )
    
    for c in alphabet:        
        right_side.append( "C{0}[{1}]".format( c, child_type ) )
        right_side.append( "ROOT->C{0} [{0}]".format( c ) )

    print( '"{}" : "{}",'.format( src_node, "; ".join( right_side ) ) )
