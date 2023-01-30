
def org_playlist(self):
    


    musicas_tocadas = [2,10,5,3]
    new_emb = musicas_tocadas
    new_emb = sorted(new_emb, key=int, reverse=True)
    emb = []

    if new_emb == []:
        return new_emb
    elif max(new_emb) == min(new_emb):
        return new_emb
    elif max(new_emb) > min(new_emb):
        emb.append(max(new_emb))
        emb.append(min(new_emb))
        del (new_emb[0])
        new_emb = new_emb[:-1]
        emb.append(max(new_emb))
        emb.append(min(new_emb))
        del (new_emb[0])
        new_emb = new_emb[:-1]
        if len(new_emb) > 0:
            emb.append(new_emb[0])
        return emb



