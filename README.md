# CoronaBibliothekar [#wirvsvirushack](https://twitter.com/hashtag/wirvsvirushack)
Falsche Informationen in Social Media mit guten Quellen kontern! 

## Inspiration
In der derzeitigen Situation rund um das Corona-Virus kommt es darauf an, richtige Informationen einheitlich und schnell zu verteilen. Durch viele verschiedene Informationsquellen entstehen überlastete Hotlines bei Behörden, verzögern sich die Effekte wirkungsvoller Maßnahmen und Falschmeldungen werden begünstigt. Bereits bestehende Chatbots zum Thema Corona sind oft einfache Klickbots ohne Interaktion mit dem Nutzer. Sie sind isoliert auf Websites zu finden und haben geringe Reichweite.

## Ziel
Mit dem Chatbot CoronaBibliothekar schaffen wir eine Anlaufstelle direkt im Posteingang auf dem Smartphone der Nutzer. Da in der Altersgruppe der 14 - 49jährigen über 95% und in der Altersgruppe bis 65 knapp 90% der Deutschen ein Smartphone nutzen, ist dies eine optimale Lösung für geprüfte und verzögerungsarme Informationen mit sehr großer Reichweite. Da WhatsApp einer der am häufigsten genutzten Messenger und damit leider auch Quelle von vielen Falschmeldungen (Fake News) ist, ist es das Ziel, den Chatbot CoronaBibliothekar über diesen Kanal nutzbar zu machen.

## Weg
Der Prototyp des CoronaBibliothekars wird mit Rasa, einem Open Source Chatbot-Framework, erstellt. Der Chatbot soll über Telegram und Facebook Messenger erreichbar und getestet werden. Aktuelle Daten werden von der Seite des RKI geladen.

## weitere Informationen
Weitere Informationen zu diesem projekt finden sie auf [Devpost](https://devpost.com/software/1_039_staatlichekommunikation_coronabibliothekar)

## Setup
Zu starten des Projekts benötigen sie die Module `rasa`, `rasa-sdk` `BeautifulSoup4`, `requests`, `python-Levenshtein`, und `yaml`. <br />
Tragen sie alle verbindungsinformationen zu Platformen die sie mit dem Bot ausstatten wollen in die `credentials.yml` ein. Eine genaue anleitung finden sie unter [https://rasa.com/docs/rasa/user-guide/messaging-and-voice-channels]().<br />
Um den Bot startklar zu machen muss er zuerst trainiert werden: `rasa train`.<br />
Starten sie zudem den action server mit `rasa run actions`. Sollte ein `ModuleNotFoundError` auftreten vergewissern sie sich das das im Fehler genannte Python Modul auf ihrem System verfügbar ist.<br />
Aachdem das Traning abgeschlossen ist und der action server gestartet ist, können sie den bot mit `rasa run` starten.<br />
Sollten sie keine credentials angegeben haben können sie den bot von der commandozeile aus testen. verwenden sie hierfür den Befehl `rasa shell`
