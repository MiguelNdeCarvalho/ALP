# Antevisão AF + Python

1. Exercício. Implemente a função controls(delta) que devolve o conjunto dos estados de controlo. No exemplo acima controls(delta) == {0, 1, 2, 3}.

2. Exercício. Implemente a função leadsTo para determinar os estados que o símbolo s permite atingir. No exemplo acima leadsTo("a", delta) == {1, 2, 3} e leadsTo("b", delta) == {2,3}.

3. Exercício. Implemente a função symbols que devolve o conjunto dos símbolos. No exemplo acima symbols(delta) == {"a", "b"}.

4. Exercício. Implemente a função areNeighbours para determinar dois estados são vizinhos, isto é, se é possível passar de um para o outro em apenas um passo. No exemplo acima areNeighbours(0, 1, delta) e not areNeighbours(3, 2, delta).
