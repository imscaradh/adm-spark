# Advanced Data Management: Spark

## Teil I: Throughput pro Minute (serverseitig)
* darin nur res_snd Records beachten
* zählen, wie res_snd pro Minute anfielen (dazu den time-Wert ohne Rest durch 1000*60 dividieren).
* die Werte als CSV-Datei ausgibt
* Stellen Sie die Entwicklung mit geeigneten Mitteln graphisch dar - mit einem Tool Ihrer Wahl

## Teil II: Mittelwert pro Minute der Responsetime (clientseitig)
* Differenz der time-Werte von Logsätzen, welche in client_id und loc_ts übereinstimmen (das sollten in der Log-Datei jeweils Paare sein)
* Den Mittelwert über alle Log-Sätze bilen, welche in der gleichen Minute anfielen (dazu, den time-Wert des Requests, d.h. den niedrigeren time-Wert des Logsatz-Paares, durch 1000*60 dividieren)
* die Werte als CSV-Datei ausgibt.
* Stellen Sie die Entwicklung mit geeigneten Mitteln graphisch dar - mit einem Tool Ihrer Wahl.

## Ausführung
Zur Verwendung der Scripts müssen folgende Schritte getätigt werden:
* HDFS starten
* PySpark starten
* Aus PySpark folgender Befehl ausführen: `execfile('project/part1.py')`. Wichtig dabei ist die Ausführung auf derselben Struktur, wie Spark gestartetn wurde (`/home/hadoop/spark`)
