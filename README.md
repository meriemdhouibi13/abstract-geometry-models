# Abstract Modern Geometry: Axiom Systems & Models

This repository contains comprehensive solutions and models for abstract modern geometry problems, including axiom system consistency proofs, independence verification, isomorphism proofs, and group theory counterexamples.

## Problems Overview

### Problem 1: Axiom System 3.1-3.3 Consistency
**Axioms:**
- 3.1: There exists exactly three points
- 3.2: Two distinct points are incident with a unique line
- 3.3: Not all points are incident with the same line

**Task:** Prove the system is consistent by finding a model.

**Solution:** See `problem1_model.py`

### Problem 2: Axiom Independence
**Task:** Show each axiom is independent by negating each one and finding models for the remaining three axioms.

**Solution:** See `problem2_independence.py`

### Problem 3: Isomorphism of Models (4.1-4.3)
**Axioms:**
- 4.1: There exists exactly four points
- 4.2: Two distinct points are on exactly one line
- 4.3: Each line contains exactly two points

**Task:** Prove all models of this system are isomorphic.

**Solution:** See `problem3_isomorphism.py`

### Problem 4: Model for n=3
**Axioms A.1-A.4** with n=3 (a line with exactly 3 points)

**Task:** Find a model when n = 3.

**Solution:** See `problem4_model_n3.py`

### Problem 5: Hamming Distance Verification
**Task:** Verify that D is a distance function on X (the set of 7-tuples with coordinates 0 or 1), where D(x,y) = number of coordinates where x and y differ.

**Solution:** See `problem5_hamming_distance.py`

### Problem 6: Group Theory Counterexamples
**Task:** Find counterexamples to group properties for each non-group set.

**Solution:** See `problem6_group_counterexamples.py`

## Files

- `README.md` - This file
- `problem1_model.py` - Consistency proof with model
- `problem2_independence.py` - Independence proofs
- `problem3_isomorphism.py` - Isomorphism verification
- `problem4_model_n3.py` - Model for n=3
- `problem5_hamming_distance.py` - Distance function verification
- `problem6_group_counterexamples.py` - Group counterexamples

## Running the Code

Each Python file can be run independently:

```bash
python problem1_model.py
python problem2_independence.py
python problem3_isomorphism.py
python problem4_model_n3.py
python problem5_hamming_distance.py
python problem6_group_counterexamples.py
```

## Key Concepts

- **Consistency:** A system is consistent if there exists at least one model satisfying all axioms
- **Independence:** An axiom is independent if the remaining axioms do not prove it
- **Isomorphism:** Two models are isomorphic if there exists a structure-preserving bijection between them
- **Distance Function:** Must satisfy: non-negativity, identity, symmetry, and triangle inequality
- **Group Properties:** Closure, associativity, identity element, inverse elements

## Author
Created for Abstract Modern Geometry coursework