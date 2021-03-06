# This file uses sage idiom to create a group that corresponds to the
# permutation group of the centers of the faces in the starminx III.
# In this dodecahedral puzzle each face has sixteen stickers.  Face
# (or central sticker) numbering follows the megaminx notation.

# The following five lines are taken verbatim from (heavily
# documented) files 'dodecahedron_group.py' and
# 'full_dodecahedron_group.py') but are included here in the interests
# of making starminx_III.py self-contained.  They define objects
# dod_face and full_dod_face which represent the dodecahedron group
# (which is the group of symmetries of the faces of a dodecahedron),
# and the full dodecahedron group (which includes reflections).

face1 = PermutationGroupElement([(2,3,4,5,6),(7,11,10,9,8)]) 
face2 = PermutationGroupElement([(3,1,2),(6,8,4),(9,7,5),(10,12,11)])
face_reflect = PermutationGroupElement([(3,6),(4,5),(8,9),(7,10)]) 
dod_face  = PermutationGroup([face1,face2])
full_dod_face  = PermutationGroup([face1,face2,face_reflect])


# The following 20 lines show the effect of turning one corner on the
# starminx III.  A dodecahedron has 20 vertices, we have one
# permutation group element for turning each vertex.

corner01 = PermutationGroupElement([( 1,  2,  3)])
corner02 = PermutationGroupElement([( 1,  3,  4)])
corner03 = PermutationGroupElement([( 1,  4,  5)])
corner04 = PermutationGroupElement([( 1,  5,  6)])
corner05 = PermutationGroupElement([( 1,  6,  2)])
corner06 = PermutationGroupElement([( 2,  9,  8)])
corner07 = PermutationGroupElement([( 2,  6,  9)])
corner08 = PermutationGroupElement([( 6, 10,  9)])
corner09 = PermutationGroupElement([( 6,  5, 10)])
corner10 = PermutationGroupElement([( 5, 11, 10)])
corner11 = PermutationGroupElement([( 5,  4, 11)])
corner12 = PermutationGroupElement([( 4,  7, 11)])
corner13 = PermutationGroupElement([( 4,  3,  7)])
corner14 = PermutationGroupElement([( 3,  8,  7)])
corner15 = PermutationGroupElement([( 3,  2,  8)])
corner16 = PermutationGroupElement([(12,  7,  8)])
corner17 = PermutationGroupElement([(12,  8,  9)])
corner18 = PermutationGroupElement([(12,  9, 10)])
corner19 = PermutationGroupElement([(12, 10, 11)])
corner20 = PermutationGroupElement([(12, 11,  7)])

# Then starminx is the group generated by moves above
starminx_centers  = PermutationGroup([
    corner01,
    corner02,
    corner03,
    corner04,
    corner05,
    corner06,
    corner07,
    corner08,
    corner09,
    corner10,
    corner11,
    corner12,
    corner13,
    corner14,
    corner15,
    corner16,
    corner17,
    corner18,
    corner19,
    corner20
])

starminx_centers.order()
starminx_centers.order().factor()

# Motivated by the fact that the order of starminx_centers =
# factorial(12)/2, we can ask whether the dodahedron group is a
# subgroup of the starminx centers:

dod_face.is_subgroup(starminx_centers)
# That gives 'True', so it is. 

# See whether the *full* dodahedron group is a subgroup of the
# starminx centers:
fuldod_face.is_subgroup(starminx_centers)
# That gives 'True' as well.


# OK, but is it normal?
dod_face.is_normal(starminx_centers)
fuldod_face.is_normal(starminx_centers)

# Both the above give 'False' (NB: had these returned 'True' I would
# have had no difficulty explaining that.  It would have been
# obviously true and I would have accepted its truth without
# question).

# Next question, is starminx_centers isomorphic to, say an
# alternating group?
starminx_centers.is_isomorphic(AlternatingGroup(12))


# This returns True, so yes it is!  In other words, we can execute
# any *even* permutation of the faces' centers by starminx III moves.  
