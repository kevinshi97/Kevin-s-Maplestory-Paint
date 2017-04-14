# stamp loops

    #,"luminous","aran","evan","mercedes","phantom","demonslayer","mage","pirate","thief","warrior","bowman"
                
    if tool == "luminous":
        screen.set_clip(canvas)
        if mb[0]==1:
            if click:#this way they can't drag the stamp across the canvas
                screen.blit(luminousstamp,(mx-100,my-100))
                screen.set_clip(None)
                
    if tool == "aran":
        screen.set_clip(canvas)
        if mb[0]==1:
            if click:
                screen.blit(aranstamp,(mx-100,my-100))
                screen.set_clip(None)
                
    if tool == "evan":
        screen.set_clip(canvas)
        if mb[0]==1:
            if click:
                screen.blit(evanstamp,(mx-100,my-100))
                screen.set_clip(None)

    if tool == "mercedes":
        screen.set_clip(canvas)
        if mb[0]==1:
            if click:
                screen.blit(mercedesstamp,(mx-100,my-100))
                screen.set_clip(None)

    if tool == "phantom":
        screen.set_clip(canvas)
        if mb[0]==1:
            if click:
                screen.blit(phantomstamp,(mx-100,my-100))
                screen.set_clip(None)

    if tool == "demonslayer":
        screen.set_clip(canvas)
        if mb[0]==1:
            if click:
                screen.blit(demonslayerstamp,(mx-100,my-100))
                screen.set_clip(None)

    if tool == "mage":
        screen.set_clip(canvas)
        if mb[0]==1:
            if click:
                screen.blit(magestamp,(mx-100,my-100))
                screen.set_clip(None)

    if tool == "pirate":
        screen.set_clip(canvas)
        if mb[0]==1:
            if click:
                screen.blit(piratestamp,(mx-100,my-100))
                screen.set_clip(None)
    if tool == "thief":
        screen.set_clip(canvas)
        if mb[0]==1:
            if click:
                screen.blit(thiefstamp,(mx-100,my-100))
                screen.set_clip(None)

    if tool == "warrior":
        screen.set_clip(canvas)
        if mb[0]==1:
            if click:
                screen.blit(warriorstamp,(mx-100,my-100))
                screen.set_clip(None)

    if tool == "bowman":
        screen.set_clip(canvas)
        if mb[0]==1:
            if click:
                screen.blit(bowmanstamp,(mx-100,my-100))
                screen.set_clip(None)
