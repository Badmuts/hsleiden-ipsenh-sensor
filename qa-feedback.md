# QA Feedback

De code ziet er goed gestructureerd uit. Verantwoordelijkheden worden verdeeld over verschillende componenten. Code is netjes geformuleerd en duidelijk naamgegeven. Foutafhandeling lijkt wat dunnetjes.

Helaas ontbreken geautomatiseerde testen. Voor zover mij bekend is er geen automatische kwaliteitsmeting.

### HIGH

- Geautomatiseerde testen ontbreken.

### MEDIUM

- Geef magic numbers betekenis. Wat betekenen 17 en 23 hier? [main.py](https://github.com/Badmuts/hsleiden-ipsenh-sensor/blob/master/src/main.py#L19)
- Handel fouten echt af (bijv door een exception te gooien) ipv een foutwaarde te returnen. Zo kun je eenvoudiger een duidelijke foutmelding tonen ipv een "ERROR000000" id. ([HubInformation.py:15](https://github.com/Badmuts/hsleiden-ipsenh-sensor/blob/master/src/hub/HubInformation.py#L15))

### LOW

- Singleton is (vaak) een anti-pattern. Probeer waar mogelijk van Dependency Injection gebruik te maken. [config.py:4](https://github.com/Badmuts/hsleiden-ipsenh-sensor/blob/master/src/config/config.py#L4)
- Getting started documentatie is aardig maar kan duidelijker.
