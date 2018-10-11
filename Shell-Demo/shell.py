# -*- coding: utf-8 -*-
"""
Copyright 2018
Dan Aukes, Cole Brauer
"""

import coloredlogs
import model_tools as model
import mesh_tools as mesh
import opengl_plot_tools as plot
  
if __name__=='__main__':
    coloredlogs.install(level='DEBUG')

    # Import model ##############################################################
    joint1 = model.import_vox('joint5.vox')

    outsideShell = model.shell_outside(joint1)

    # Initialize application 1
    app1, w1 = plot.prep()

    # Convert model to mesh data
    v, vc, t = mesh.create_from_model(model.union(joint1, outsideShell))

    # Create mesh item and add to plot
    mi = plot.make_mi(v, t, vc, drawEdges = True, edgeColor=(1,1,1,0.5))
    w1.addItem(mi)

    # Show plot 1
    plot.show(w1, joint1)

    # Save screenshot of plot 1
    #w1.paintGL()
    #w1.grabFrameBuffer().save('shell-fig1.png')

    # Isolate flexible components ###############################################
    flexComponents = model.isolate_material(joint1, 217)
    outsideShell = model.shell_outside(flexComponents)

    # Initialize application 2
    w2 = plot.add_widget()

    # Convert model to mesh data
    v, vc, t = mesh.create_from_model(model.union(flexComponents, outsideShell))

    # Create mesh item and add to plot
    mi = plot.make_mi(v, t, vc, drawEdges=True, edgeColor=(1, 1, 1, 0.5))
    w2.addItem(mi)

    # Show plot 2
    plot.show(w2, flexComponents)

    # Save screenshot of plot 2
    #w2.paintGL()
    #w2.grabFrameBuffer().save('shell-fig2.png')

    app1.exec_()