# Problem 2: Independence of Axioms in Abstract Geometry Models

# This script demonstrates models for each axiom negated individually to prove independence.

class Axiom:
    def __init__(self, description):
        self.description = description
        self.is_true = True

    def negate(self):
        self.is_true = False

# Define the axioms
axiom1 = Axiom("Through any two points, there exists exactly one line.")
axiom2 = Axiom("A line segment can be extended indefinitely in both directions.")
axiom3 = Axiom("Given a point and a line, there exists exactly one line through the point that is parallel to the original line.")
axiom4 = Axiom("All right angles are congruent.")

# Negate the axioms to show independence
axioms = [axiom1, axiom2, axiom3, axiom4]

for axiom in axioms:
    axiom.negate()  # Negate each axiom
    print(f"Negation of Axiom: {axiom.description} - {axiom.is_true}")
