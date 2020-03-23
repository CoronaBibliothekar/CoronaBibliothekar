# CoronaBibliothekar [#wirvsvirushack](https://twitter.com/hashtag/wirvsvirushack)
Falsche Informationen in Social Media mit guten Quellen kontern! 

## Inspiration
In der derzeitigen Situation rund um das Corona-Virus kommt es darauf an, richtige Informationen einheitlich und schnell zu verteilen. Durch viele verschiedene Informationsquellen entstehen überlastete Hotlines bei Behörden, verzögern sich die Effekte wirkungsvoller Maßnahmen und Falschmeldungen werden begünstigt. Bereits bestehende Chatbots zum Thema Corona sind oft einfache Klickbots ohne Interaktion mit dem Nutzer. Sie sind isoliert auf Websites zu finden und haben geringe Reichweite.

## Ziel
Mit dem Chatbot CoronaBibliothekar schaffen wir eine Anlaufstelle direkt im Posteingang auf dem Smartphone der Nutzer. Da in der Altersgruppe der 14 - 49jährigen über 95% und in der Altersgruppe bis 65 knapp 90% der Deutschen ein Smartphone nutzen, ist dies eine optimale Lösung für geprüfte und verzögerungsarme Informationen mit sehr großer Reichweite. Da WhatsApp einer der am häufigsten genutzten Messenger und damit leider auch Quelle von vielen Falschmeldungen (Fake News) ist, ist es das Ziel, den Chatbot CoronaBibliothekar über diesen Kanal nutzbar zu machen.

## Weg
Der Prototyp des CoronaBibliothekars wird mit Rasa, einem Open Source Chatbot-Framework, erstellt. Der Chatbot soll über Telegram und Facebook Messenger erreichbar und getestet werden. Aktuelle Daten werden von der Seite des RKI geladen.

## weitere Informationen
Weitere Informationen zu diesem Projekt finden sie auf [Devpost](https://devpost.com/software/1_039_staatlichekommunikation_coronabibliothekar)

## Setup
Tragen Sie alle Verbindungsinformationen zu Plattformen die sie mit dem Bot ausstatten wollen in die `credentials.yml` Datei ein. Eine genaue Anleitung finden sie unter [https://rasa.com/docs/rasa/user-guide/messaging-and-voice-channels]().<br /><br />
Um den Bot startklar zu machen, muss er zuerst trainiert werden: `rasa train`.<br /><br />
Starten Sie zudem den Action Server mit `rasa run actions`. Sollte ein `ModuleNotFoundError` auftreten vergewissern sie sich, dass das im Fehler genannte Python Modul auf ihrem System verfügbar ist.<br /><br />
Nachdem das Training abgeschlossen ist und der Action Server gestartet ist, können sie den bot mit `rasa run` starten.<br /><br />
Sollten sie keine credentials angegeben haben können sie den bot von der Kommandozeile aus testen. Verwenden sie hierfür den Befehl `rasa shell`