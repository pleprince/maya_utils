# philippe leprince
# Fri Nov 17 18:16:16 GMT 2017

import maya.cmds as mc


def scale_to_fit_in_cube(cube_size):
    obj = mc.ls(sl=True)[0]
    print 'selected: %s' % obj

    # center pivots
    mc.xform(obj, cpc=True)

    # translate to origin
    pivs = mc.xform(obj, q=True, piv=True)
    mc.setAttr('%s.tx' % obj, -pivs[0])
    mc.setAttr('%s.ty' % obj, -pivs[1])
    mc.setAttr('%s.tz' % obj, -pivs[2])

    # freeze transforms
    mc.makeIdentity(obj, apply=True, t=True, r=True, s=True, n=False, pn=True)

    # get bounding box
    bbs = mc.getAttr('%s.boundingBoxSize' % obj)
    print '  |_ size: %s' % bbs
    mx = max(bbs[0][0], bbs[0][1], bbs[0][2])
    print '  |_ max: %s' % mx

    # scale to fit cube
    scale_factor = float(cube_size) / mx
    print '  |_ scale_factor: %s' % scale_factor
    mc.setAttr('%s.sx' % obj, scale_factor)
    mc.setAttr('%s.sy' % obj, scale_factor)
    mc.setAttr('%s.sz' % obj, scale_factor)

    # offset so the bottom is aligned on the xz plane
    bbn = mc.getAttr('%s.boundingBoxMin' % obj)
    print '  |_ bbx min: %s' % bbn
    ymin = bbn[0][1]
    print '  |_ align on xz plane: -%s' % ymin
    mc.setAttr('%s.ty' % obj, -ymin)

    # freeze transforms
    mc.makeIdentity(obj, apply=True, t=True, r=True, s=True, n=False, pn=True)

    # zero pivots
    mc.xform(obj, ztp=True)
