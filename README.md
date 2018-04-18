# Eulerian
# Eulerian Network

 Repository of Eulerian functions

 File 01: toEulerian 
 Given a non-eulerian graph G=(V,E), returns G'=(V,EUZ) where Z is the set of edges and G' is Eulerian.
 The input is an adjacency matrix M

 Sample run
 >> toEuler(M)


 File 02: heir 
 implements the Hierholzers algorithm. Given a simple graph G, extracts the Eulerian circuit.
 The input is an adjacency matrix M

 Sample run
 >> from toEulerian import am2ag
 >> hier(M)
