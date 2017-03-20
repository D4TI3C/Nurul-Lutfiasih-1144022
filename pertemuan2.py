graph = {
             'Poltekpos': ['Sarijadi'],
             'Sarijadi': ['Jalan Layang Pasupati'],
             'Jalan Layang Pasupati': ['Jalan Cihampelas'],
             'Jalan Cihampelas': ['Jalan Ir.H.Djuanda'],
             'Jalan Ir.H.Djuanda': ['Gedung Sate'],

        }

def mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[]):
        jalur = jalur + [jalanawal]
        if jalanawal == jalantujuan:
            return jalur
            if not graph.has_key(jalanawal):
                    return None
        jalurpendek = None
        for node in graph[jalanawal]:
            if node not in jalur:
                newjalur = mencari_jalur_terpendek(graph, node, jalantujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Poltekpos sampai Gedung Sate")
print("(Poltekpos, Sarijadi, Jalan Layang Pasupati)")
print("(Jalan Cihampelas, Jalan Ir.H.Djuanda, Gedung Sate)")
print("\n")
jalanawal = raw_input("Masukan jalanawal : ")
jalantujuan = raw_input("Masukan jalantujuan : ")
hasil = mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[])
print "Jalur Terpendek", hasil
