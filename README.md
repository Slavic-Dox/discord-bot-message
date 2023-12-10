# Mit Discord Bot Nachrichten im Server schreiben:

Bei der Ausführung des bereitgestellten Codes wird der Discord-Bot gestartet, und folgende Aktionen werden durchgeführt:

# Initialisierung:

Der Bot wird mit dem angegebenen Token initialisiert.
Die Intents werden aktiviert, insbesondere message_content, um Nachrichteninhalte zu verfolgen.
on_ready-Event:

Die Funktion on_ready wird aufgerufen, sobald der Bot erfolgreich gestartet ist.
Der Bot gibt eine Meldung aus, die den erfolgreichen Login des Bots mit dem Benutzernamen des Bots anzeigt.
Der Bot ruft das Channel-Objekt für den Ziel-Channel (ZIEL_CHANNEL_ID) ab.

# Nachricht senden:

Der Bot versucht, eine Nachricht in den Ziel-Channel zu senden.
Die Nachricht enthält den Text "Hello World :) @everyone".
