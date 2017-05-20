# Advanced Data Management: Spark

Teil I:
* welches den Throughput pro Minute bildet
* serverseitiges Log - nur mw_trace50 nehmen
* darin nur res_snd Records beachten
* zählen, wie res_snd pro Minute anfielen (dazu den time-Wert ohne Rest durch 1000*60 dividieren).
* die Werte als CSV-Datei ausgibt
* Stellen Sie die Entwicklung mit geeigneten Mitteln graphisch dar - mit einem Tool Ihrer Wahl

Teil II:
* welches pro Minute den Mittelwert der Responsetime bildet
* clientseitiges Log client_trace50
* Differenz der time-Werte von Logsätzen, welche in client_id und loc_ts übereinstimmen (das sollten in der Log-Datei jeweils Paare sein)
* Den Mittelwert über alle Log-Sätze bilen, welche in der gleichen Minute anfielen (dazu, den time-Wert des Requests, d.h. den niedrigeren time-Wert des Logsatz-Paares, durch 1000*60 dividieren)
* die Werte als CSV-Datei ausgibt.
* Stellen Sie die Entwicklung mit geeigneten Mitteln graphisch dar - mit einem Tool Ihrer Wahl.
